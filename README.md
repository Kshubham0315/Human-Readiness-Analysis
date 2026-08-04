<div align="center">


### AI-Powered Multimodal Behavioral Readiness Analysis



# Overview

AI-powered multimodal behavioral intelligence platform that estimates **behavioral confidence** in real time by analyzing observable human signals instead of attempting to predict emotions, personality, or psychological states.

Unlike conventional "emotion recognition" systems, It focuses on measurable behavioral consistency across multiple modalities.

The system combines:

- 👁️ Eye Gaze Stability
- 🎙️ Speech Decisiveness
- ✋ Gesture Firmness
- 🧠 Face Engagement

into a single interpretable **Behavioral Readiness Index**, providing users with transparent and explainable feedback.

---


# Why It?

Current AI interview tools often rely on emotion detection or black-box personality prediction, both of which are difficult to justify scientifically.

It follows a different philosophy.

Instead of asking:

> "What emotion is this person feeling?"

it asks

> "How behaviorally stable is this person's communication?"

This makes the system:

- Explainable
- Lightweight
- Privacy Friendly
- Ethically Designed
- Easy to Interpret

---

# Key Features

✅ Real-time webcam processing (25–30 FPS)

✅ Multimodal confidence estimation

✅ Adaptive score fusion

✅ Personal gaze calibration

✅ Speech hesitation detection

✅ Tremble & gesture consistency analysis

✅ Face engagement tracking

✅ Session history

✅ Automatic JSON report generation

✅ Streamlit dashboard

✅ CPU friendly (No GPU Required)

---

# Behavioral Signals

| Module | What It Measures | Weight |
|---------|------------------|---------|
| 👁 Gaze Stability | Eye fixation consistency | 35% |
| 🎙 Speech | Speech continuity & hesitation | 30% |
| ✋ Gesture | Smoothness & tremble detection | 20% |
| 🧠 Engagement | Face visibility & engagement | 15% |

If the microphone is unavailable, It automatically switches to a three-signal fusion strategy.

---

# System Pipeline

```text
           Webcam + Microphone
                    │
                    ▼
        Frame & Audio Acquisition
                    │
     ┌──────────────┼──────────────┐
     │              │              │
     ▼              ▼              ▼
 Eye Module    Speech Module   Hand Module
     │              │              │
     └──────────────┼──────────────┘
                    ▼
          Engagement Detection
                    ▼
        Behavioral Score Fusion
                    ▼
      Behavioral Readiness Index
                    ▼
      Streamlit Live Dashboard
                    ▼
        Session Report (JSON)
```

---

# Confidence Fusion

The overall score is computed using a weighted multimodal fusion model.

```text
Confidence Score

= 0.35 × Eye Stability
+ 0.30 × Speech Score
+ 0.20 × Gesture Score
+ 0.15 × Engagement
```

When audio is unavailable:

```text
0.50 × Eye
+0.30 × Gesture
+0.20 × Engagement
```

---

# Algorithms Used

## 👁 Eye Stability

- MediaPipe FaceLandmarker
- Iris Landmark Tracking
- Personal Calibration
- Head-relative Coordinate Normalization
- Distance-based Confidence Mapping

---

## 🎙 Speech Analysis

Rather than speech-to-text, It analyzes:

- RMS Energy
- Pause Density
- Speaking Continuity
- Live Silence Penalty

No spoken content is stored or interpreted.

---

## ✋ Gesture Analysis

The hand module combines:

- Wrist Velocity
- Jerk Detection
- Exponential Motion Decay
- Rolling Tremble Detection

allowing intentional gestures while detecting persistent nervous movement.

---

## 🧠 Engagement Analysis

Engagement is measured using:

- Face Visibility
- Face Occlusion
- Hand-over-face Detection
- Sustained Absence Tracking

Brief occlusions are ignored to reduce false positives.

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Computer Vision | MediaPipe |
| Video Processing | OpenCV |
| Audio Processing | sounddevice |
| Numerical Computing | NumPy |
| Dashboard | Streamlit |

---

# Project Structure

```text
It/

├── app.py
├── core/
│   ├── confidence_engine.py
│   ├── fusion.py
│   ├── engagement_module.py
│   ├── session_manager.py
│   └── camera_manager.py
│
├── vision/
│   ├── eye_module.py
│   ├── hand_module.py
│   └── frame_analyzer.py
│
├── audio/
│   └── speech_module.py
│
├── models/
│
├── data/
│
├── utils/
│
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/It.git

cd It
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

MediaPipe models are downloaded automatically during the first execution.

---

# Responsible AI

It is intentionally designed **not** to:

- Detect emotions
- Predict personality
- Estimate intelligence
- Diagnose mental health
- Make hiring decisions

The platform only evaluates observable behavioral signals using transparent mathematical scoring.

# Author

**Shubham Kumar**

AI Engineer | Machine Learning | Computer Vision

Building practical AI systems focused on explainability, human-centered design, and real-world deployment.

---

## ⭐ If you found this project interesting, consider giving it a star.
