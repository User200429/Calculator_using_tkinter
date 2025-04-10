# 🧮 Tkinter Calculators

A collection of beginner-friendly calculator apps built with Python's Tkinter library. These apps showcase GUI design using both static layouts and dynamic grid geometry managers.

---

## 📂 Project Files

- `basic_calculator.py` – Calculator with separate frames for display and buttons. Buttons are added manually.
- `grid_calculator.py` – More scalable version using loops to generate buttons via a grid layout.

---

## 🧾 Extended Descriptions

### `basic_calculator.py` – Frame-Based Static Calculator

#### 🧩 Overview
Implements a simple calculator GUI using manual layout control. The interface is divided into two clearly defined frames — one for the display and another for button controls.

#### 🧱 Structure
- **Top Frame (`frame1`)**: Contains a label to display the current input and result.
- **Bottom Frame (`frame2`)**: Contains a 4x5 grid of buttons, each manually positioned.
- **Buttons**: Created one by one using `tk.Button()` and `.grid()` layout.
- **Functions**:
  - `clear()`: Clears all input
  - `backspace()`: Deletes the last character
  - `number_operators(n)`: Appends digits or operators
  - `answer()`: Evaluates the expression and shows the result

#### 🛠️ Features
- Basic arithmetic operations: `+`, `-`, `*`, `/`, `%`
- `Clear` and `Backspace (<-)` buttons
- `eval()` for evaluating expressions
- Error handling for invalid expressions
- Uses `tk.Frame`, `tk.Label`, and `tk.Button`
- Demonstrates a combination of `.pack()` and `.grid()`

#### 🎯 Best For
- Beginners learning the basics of GUI layout in Tkinter
- Projects where layout needs to be controlled manually

---

### `grid_calculator.py` – Dynamic Grid-Based Calculator

#### 🧩 Overview
A cleaner, more scalable calculator that generates buttons dynamically using a nested list and loops. Focuses on code efficiency and DRY principles.

#### 🧱 Structure
- **Top Frame (`frame1`)**: Contains a display label, packed and sized flexibly.
- **Bottom Frame (`frame2`)**: Button layout is created from a 2D list.
- **Button Logic**: All buttons are managed through a single `action(c)` function.

#### 🛠️ Features
- All features from `basic_calculator.py`
- Button grid defined as a list of lists
- Buttons created dynamically with `enumerate()` and `lambda`
- Layout responds to resizing with `.rowconfigure()` and `.columnconfigure()`
- Simplified logic with a single handler function

#### 🎯 Best For
- Developers building scalable Tkinter apps
- Reducing redundancy using loops and data structures
- Exploring grid-based layouts in real applications

---

## 🔬 Comparison

| Feature                      | `basic_calculator.py`         | `grid_calculator.py`               |
|-----------------------------|-------------------------------|------------------------------------|
| Button Creation             | Manually defined              | Generated via loop and list        |
| Layout Approach             | Static + manual grid          | Fully grid-based & dynamic         |
| Display Update Method       | Direct `.config()` calls      | Single `action()` function         |
| Code Reusability            | Less DRY (more repetition)    | DRY (centralized logic)            |
| Ideal Use Case              | Learning basic layouts        | Scalable GUIs & cleaner structure  |

---

## ▶️ How to Run

Make sure Python (3.x) is installed.

```bash
python basic_calculator.py
# or
python grid_calculator.py
