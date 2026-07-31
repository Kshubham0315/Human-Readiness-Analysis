import math

# MediaPipe canonical face mesh landmark indices
NOSE_IDX = 1


class EngagementTracker:
    """Sustained face-hiding detector producing an engagement_score 0-100.

    Usage::

        tracker = EngagementTracker()
        score   = tracker.process(face_landmarks_list, hand_landmarks_list)
        ratio   = tracker.hidden_ratio
    """

    BUFFER_SIZE = 150
    PROXIMITY_THRESHOLD = 0.12
    HIDDEN_ONSET = 0.40
    SCORE_FLOOR = 20.0
    EMA_ALPHA = 0.20

    def __init__(self) -> None:
        self._hidden_counter: float = 0.0
        self._score: float = 100.0

    @property
    def score(self) -> float:
        """Current engagement score 0-100."""
        return self._score

    @property
    def hidden_ratio(self) -> float:
        """0.0 = fully visible every frame, 1.0 = hidden every frame."""
        return self._hidden_counter / self.BUFFER_SIZE

    def process(self, face_landmarks_list, hand_landmarks_list) -> float:
        """Update and return engagement score based on current frame landmarks.

        Args:
            face_landmarks_list: From FaceLandmarker result.face_landmarks.
            hand_landmarks_list: From HandLandmarker result.hand_landmarks,
                                 or None/empty.

        Returns:
            Engagement score 0-100.
        """
        hidden = self._is_hidden(face_landmarks_list, hand_landmarks_list)

        if hidden:
            self._hidden_counter = min(self.BUFFER_SIZE, self._hidden_counter + 1.0)
        else:
            self._hidden_counter = max(0.0, self._hidden_counter - 1.0)

        ratio = self.hidden_ratio

        if ratio <= self.HIDDEN_ONSET:
            target = 100.0
        else:
            t = (ratio - self.HIDDEN_ONSET) / (1.0 - self.HIDDEN_ONSET)
            target = max(self.SCORE_FLOOR, 100.0 - (100.0 - self.SCORE_FLOOR) * t)

        self._score = float(
            (1.0 - self.EMA_ALPHA) * self._score + self.EMA_ALPHA * target
        )
        return self._score

    def _is_hidden(self, face_landmarks_list, hand_landmarks_list) -> bool:
        """Return True when the face appears occluded this frame."""
        if not face_landmarks_list:
            return True

        face = face_landmarks_list[0]
        nose = face[NOSE_IDX]

        if hand_landmarks_list:
            for hand in hand_landmarks_list:
                for lm in hand:
                    dist = math.sqrt((lm.x - nose.x) ** 2 + (lm.y - nose.y) ** 2)
                    if dist < self.PROXIMITY_THRESHOLD:
                        return True

        return False
