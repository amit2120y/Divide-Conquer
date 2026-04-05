# 🚀 Quick Start Guide

## Installation & Running (60 seconds)

### 1. Install Flask
```bash
pip install flask
```

### 2. Start the App
```bash
python app.py
```

Output should show:
```
 * Running on http://127.0.0.1:5000
```

### 3. Open Browser
Go to: **http://localhost:5000**

---

## Try These Examples

### Example 1: Merge Sort
```
Category: Divide & Conquer
Algorithm: Merge Sort
Input: 5,3,8,1,2
Click: Run Algorithm
```

### Example 2: Fibonacci
```
Category: Dynamic Programming
Algorithm: Fibonacci (DP)
Input: 10
Click: Run Algorithm
Result: 55
```

### Example 3: N-Queens
```
Category: Backtracking
Algorithm: N-Queens Problem
Input: 8
Click: Run Algorithm
Result: 92 solutions
```

---

## File Structure at a Glance

- **app.py** — Flask server (run this!)
- **algorithms/** — Python algorithm code
- **templates/index.html** — Web interface
- **static/script.js** — Frontend logic
- **static/style.css** — Styling

---

## Troubleshooting

**Port 5000 already in use?**
Edit app.py last line:
```python
app.run(debug=True, port=8000)  # Change to 8000
```

**Module not found?**
Make sure you're in the project folder:
```bash
cd "path/to/Divide & Conquer"
python app.py
```

---

## Full Documentation
See `README.md` for complete details on all 9 algorithms.

Enjoy! 🎉
