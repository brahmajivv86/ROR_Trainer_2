# ⚓ ROR Trainer 2 — COLREGs & IALA Flashcard Trainer

A modern, standalone interactive study application for maritime **COLREGs (Collision Regulations)** Day & Night Signals, **IALA Buoyage Systems**, and **International Code Flags**.

Extracted and verified from the official Bhandarkar ROR Card Dataset.

---

## 🌟 Key Features

* 🌙 **Night Signals (1–226):** Full 226 night lights & vessel aspects.
* ☀️ **Day Signals (1–27):** Day shapes, restricted maneuvering status, and lights.
* 🔴🟢 **IALA Buoyage System (1–40):** Lateral, Cardinal, Safe Water, and Special Marks.
* 🚩 **International Code Flags (1–40):** Single-flag signals and meanings.
* ⚡ **Interactive Modes:**
  * **Trainer Mode:** Interactive flashcards with hover/click flip animations and keyboard navigation (Space to flip, Left/Right arrows to navigate).
  * **Quiz Mode:** Practice evaluation with scoring and performance summary.

---

## 🚀 Quick Start & Deployment

### Option 1: GitHub Pages (Recommended)
1. Push this folder to your GitHub repository.
2. Go to **Repository Settings** -> **Pages**.
3. Select `main` branch and `/ (root)` folder, then save.
4. Access your live trainer web app anywhere!

### Option 2: Local Python Server
Run the batch file `run.bat` or launch via Python:
```bash
python server.py
```
Open your browser at `http://localhost:8000`.

---

## 📁 Repository Structure

```
ROR_Trainer_2/
├── index.html        # Main HTML layout with dark mode glassmorphism
├── app.js            # Quiz & Trainer interactive logic
├── app.css           # Premium styling & animations
├── cards.json        # 100% clean official Bhandarkar card dataset
├── images/           # Complete image assets
│   ├── day/          # Day signal images (DayImage1.gif .. 30.gif)
│   ├── night/        # Night signal images (NightSignal1.gif .. 226.gif)
│   ├── iala/         # IALA buoyage images (bouysimage1.gif .. 40.gif)
│   └── flags/        # Code flag images (flag_an_0.gif .. 39.gif)
├── server.py         # Local Python HTTP server
└── run.bat           # Local launcher script
```

---

*Generated for Educational Purpose Only.*
