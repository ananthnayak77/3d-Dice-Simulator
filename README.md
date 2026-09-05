# 3D-Dice-Simulator     //wait a while still under progress yet to be deployed on Vercel 
this is basically my skill test game developed by me which mainly roles out the 3d dice and tracks your target score 
🎲 Interactive 3D Dice Simulator

A modern, responsive dice game built with a lightweight Flask API and a custom CSS-powered 3D die. Configure a target score and a roll limit, then watch the die tumble in real time as the game tracks every roll, your running total, and the remaining attempts.

The project is deliberately built without a 3D rendering library: the dice effect is created with native CSS 3D transforms and keyframe animations, making it a compact demonstration of how polished interactive motion can be achieved with familiar web technologies.

## ✨ Highlights

- **Custom game rules** — choose the maximum number of rolls and the score required to win before starting a round.
- **Animated 3D dice** — a six-sided cube built from HTML and CSS that rotates dynamically on each roll.
- **Live game state** — see the latest roll, accumulated score, rolls remaining, and game result immediately.
- **Responsive dashboard** — a layout designed to stay clear and usable from smaller screens through desktop displays.
- **Backend-backed simulation** — Flask handles dice-roll requests and supplies validated results to the interface.
- **Friendly game flow** — controls guide the player through setup, rolling, win/loss feedback, and starting a new game.

## 🚀 Live Demo

> Add the deployed Vercel frontend URL here once available.

**[Open the live demo](PASTE_YOUR_VERCEL_LINK_HERE)**

## 🧩 How It Works

1. Set a **target score** — the total you want to reach.
2. Set a **maximum roll count** — the number of chances available for that round.
3. Start the game and press **Roll Dice**.
4. The interface asks the Flask backend for a result, animates the 3D cube, and updates the dashboard.
5. Win by reaching the target before your rolls run out. Otherwise, reset the game and try a new strategy.

## 🏗️ Project Structure

```text
.
├── index.html             # Responsive game interface, styles, and client-side logic
├── dice_simulation.py     # Flask API and dice simulation endpoints
├── README.md              # Project documentation
└── original-scripts/      # Optional early CLI prototypes and experiments
```

> The `original-scripts/` folder is optional; include it only if you want to preserve the prototype scripts in this repository.

## 🛠️ Tech Stack

| Area | Technologies | Purpose |
| --- | --- | --- |
| Frontend | HTML5, CSS3, JavaScript (ES6+) | Game UI, 3D dice, animation, state updates, and API calls |
| Animation | CSS 3D transforms and keyframes | Creates the rotating cube effect without external 3D libraries |
| Backend | Python and Flask | Serves simulation routes and returns dice-roll results |
| Communication | Fetch API, Async/Await, JSON | Connects the browser interface to the backend |
| Deployment | Vercel (frontend) | Hosts the static client application |

## ⚙️ Run Locally

### Prerequisites

- Python 3.9 or newer
- A modern web browser
- `pip` for installing Python packages

### 1. Clone the repository

```bash
git clone <https://github.com/ananthnayak77/3d-Dice-Simulator>
cd interactive-3d-dice-simulator-a-modern
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Flask

```bash
pip install flask flask-cors
```

### 4. Start the backend

```bash
python dice_simulation.py
```

By default, Flask commonly runs on `http://127.0.0.1:5000`. Check the terminal output for the exact address.

### 5. Open the frontend

Open `index.html` in your browser, or serve the folder with a local static server. If the browser blocks requests from a local file, using a static server is recommended:

```bash
python -m http.server 5500
```

Then visit `http://127.0.0.1:5500`.

## 🔌 API Contract

The frontend and backend communicate through JSON. Keep the route name and response field names in this section aligned with the implementation in `dice_simulation.py`.

### Roll a die

```text
POST /roll
```

Example response:

```json
{
  "roll": 4
}
```

The browser uses the returned value to select a matching cube orientation, update the score, decrease the remaining roll count, and decide whether the game has ended.

## 🎨 3D Dice Implementation

Each die face is an element positioned in 3D space. CSS applies `translateZ`, `rotateX`, and `rotateY` transforms to form a cube, while a roll animation combines rotations around multiple axes. After the animation, JavaScript applies a final orientation corresponding to the rolled number.

This approach keeps the experience fast, dependency-free, and easy to customize. You can change the die color, shadows, animation timing, or face-dot styling directly in the stylesheet.

## 🧠 Game Rules

- Each roll returns a random integer from **1 to 6**.
- The rolled value is added to the current score.
- One roll is removed from the available total after each attempt.
- The player wins as soon as the score reaches or exceeds the target.
- The player loses when no rolls remain before reaching the target.
- A new game clears the score and restores the configured roll count.

## 📱 Responsive Design Notes

The interface is intended to use flexible containers, scalable spacing, and mobile-friendly control sizes. On narrower screens, the game panels can stack vertically so the dice, score information, and rule inputs remain comfortably accessible.

## 🔒 CORS and Configuration

When the frontend and backend run from different origins—such as a Vercel deployment calling a hosted Flask API—the backend must allow the frontend origin through CORS. During development, configure this deliberately and restrict allowed origins in production rather than leaving the API open to every site.

Also update the frontend API base URL for production. A practical pattern is to keep it in one constant or an environment-specific configuration value, so local and deployed versions can point to different backend addresses cleanly.

## 🗺️ Future Improvements

- Add roll history with timestamps and result statistics.
- Introduce selectable game modes, such as exact-target or high-score challenges.
- Save best scores locally or in a database.
- Add sound effects, reduced-motion support, and additional accessibility controls.
- Add automated tests for backend random-value validation and frontend game-state transitions.
- Containerize the Flask API and deploy it alongside the frontend.

## 🤝 Contributing

Contributions are welcome. For a focused change:

1. Fork the project and create a branch.
2. Make and test the change locally.
3. Keep the interface responsive and preserve the game rules.
4. Open a pull request with a short explanation and screenshots for UI changes.

## 📄 License

NO LICENSE ASSIGNED YET

## 🙌 Acknowledgements

Built as an exploration of interactive browser interfaces, CSS 3D transforms, and lightweight full-stack game design.

A modern, responsive full-stack web application that allows users to play an interactive dice game. Users can set their own custom rules (maximum rolls and target scores) and watch a custom-built 3D dice tumble dynamically in real-time.

## 🚀 Live Demo
*Check out the live frontend interface deployed here:* **[PASTE YOUR VERCEL LINK HERE]**

## 🛠️ Project Architecture & Files
This repository contains the complete evolutionary code for the game:
* **`index.html` (Frontend):** A fully styled game dashboard featuring a custom 3D animated CSS cube dice, live state tracking (score accumulator and roll counts remaining), and dynamic layout safety features.
* **`dice_simulation.py` (Flask Backend):** A Python web server handling CORS request validation handles backend simulation routing logic.
* **Original Scripts**: Early-stage CLI logic used during the initial engine prototyping phase.

## 💻 Tech Stack Used
* **Frontend**: HTML5, CSS3 (3D Transforms & Keyframe Animations), JavaScript (ES6+ Fetch API, Async/Await)
* **Backend**: Python, Flask Framework
