## 📘 `README.md` — *Blueberry Bloom: A Learning Garden for the Neurodivergent Mind*

### 🌿 Overview

**Blueberry Bloom** is a neurodivergence-friendly Pomodoro productivity and learning app that integrates principles from the **"Learning How to Learn"** course. It transforms focused time into a virtual garden, where users grow blueberries as a visual metaphor for building stronger neural pathways. Each Pomodoro session rewards users with growth progress, motivational quotes, and cognitive science-based learning tips (like chunking, active recall, and spaced repetition).

The app is designed using visual storytelling inspired by plant-growing games to reduce cognitive overload and increase engagement for neurodivergent learners.

---

### 🎯 Purpose

This project aims to:

* Demonstrate learning and application of key cognitive strategies.
* Help others visualize and interact with abstract concepts from the course.
* Serve as a motivational and organizational tool tailored for neurodivergent users.

---

### 🧠 Course Concepts Addressed

* **Chunking**: Users collect "blueberries" as symbols for learning chunks.
* **Spaced Repetition**: Knowledge snippets resurface over time with interactive feedback.
* **Focused and Diffuse Modes**: Timer cycles guide users through deep focus and brain-relaxation phases.
* **Procrastination and Habit Formation**: Integrated rewards and reminders reinforce consistent usage.

---

### 🌱 How It’s Used in Real Life

I use **Blueberry Bloom** daily to manage my attention and structure my learning time. The visual metaphor of cultivating blueberries mirrors the real effort and satisfaction that comes from growing my understanding. It helps me stay grounded, motivated, and connected to the learning process.

---

### ✨ Features

* 🌳 Grow blueberry bushes with each Pomodoro cycle.
* 🧠 Random motivational quotes and tips using spaced repetition techniques.
* 🧩 Unlockable chunks (knowledge berries) stored in a visual "brain map".
* 📅 Custom schedule planner to match focus rhythms.
* 🎨 Interface designed in Photoshop — smooth edges, no harsh boxes.

---

## 📄 Use Case Diagram

```plaintext
                +---------------------+
                |     Neurodivergent  |
                |       Learner       |
                +---------------------+
                          |
     +--------------------+-------------------+
     |                    |                   |
[Start Timer]     [View Brain Map]     [Review Tips]
     |                    |                   |
[Earn Blueberries]   [Track Learning]   [Motivation / Recall]
```

---

## 🔁 Sequence Diagram

```plaintext
User -> UI: Start Pomodoro
UI -> Timer: Start 25-minute focus timer
Timer -> UI: Countdown and progress feedback
Timer -> MotivationEngine: Fetch quote/snippet
MotivationEngine -> UI: Display motivational quote/snippet
Timer -> UI: Notify session complete
UI -> GrowthEngine: Add blueberry growth
GrowthEngine -> UI: Animate visual growth
```

---

## 🧩 Class Diagram

```plaintext
+------------------+
|     User         |
+------------------+
| +id              |
| +settings        |
| +brainMap        |
+------------------+
        |
        |
        v
+------------------+        +------------------+
|    Timer         |        | MotivationEngine |
+------------------+        +------------------+
| +startSession()  |        | +getQuote()      |
| +endSession()    |        | +getSnippet()    |
+------------------+        +------------------+

        |                            |
        v                            v

+------------------+        +------------------+
|  GrowthEngine    |        |   LearningChunk  |
+------------------+        +------------------+
| +growBerry()     |        | +title           |
| +updateGarden()  |        | +content         |
+------------------+        | +nextReviewDate  |
                            +------------------+

        ^                             ^
        |                             |
+------------------+         +-------------------+
|    GardenView    |         |   BrainMapView    |
+------------------+         +-------------------+
| +renderGarden()  |         | +renderChunks()   |
+------------------+         +-------------------+
```

---

## 📝 Final Notes

This app, though conceptual in this form, demonstrates the connection between behavior, attention, motivation, and learning using the brain-based techniques from *Learning How to Learn*. It transforms time and learning into something you can **see grow** — one blueberry at a time.

---
