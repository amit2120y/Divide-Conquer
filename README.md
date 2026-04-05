# 🎯 DAA Algorithms Playground

An interactive web-based simulator for **Design & Analysis of Algorithms**. Features implementations of algorithms across four major paradigms: Divide & Conquer, Greedy, Dynamic Programming, and Backtracking.

## 📋 Features

- **Dynamic Algorithm Selection**: Choose paradigm → select specific algorithm
- **Real-Time Execution**: Run algorithms with custom input and see results instantly
- **Time Complexity Display**: Theoretical complexity + measured execution time
- **Input Format Guide**: Clear instructions for each algorithm's input format
- **Responsive Design**: Works on desktop and mobile browsers
- **Python-Based Algorithms**: Server-side Python execution via Flask

## 🏗️ Project Structure

```
.
├── app.py                      # Flask application & API endpoints
├── algorithms/                 # Algorithm implementations
│   ├── divide_conquer.py      # Merge Sort, Quick Sort, Binary Search
│   ├── greedy.py              # Fractional Knapsack, Activity Selection
│   ├── dynamic.py             # Fibonacci, 0/1 Knapsack, LCS
│   └── backtracking.py        # N-Queens
├── templates/
│   └── index.html             # Main UI template
├── static/
│   ├── script.js              # Client-side JavaScript logic
│   └── style.css              # Styling
├── README.md                  # This file
└── requirements.txt           # Python dependencies (if exists)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. **Clone/Navigate to project**:
```bash
cd "e:\code\.vscode\Webs\Divide & Conquer"
```

2. **Install dependencies**:
```bash
pip install flask
```

3. **Run the Flask app**:
```bash
python app.py
```

4. **Open in browser**:
Navigate to `http://localhost:5000`

## 📚 Supported Algorithms

### Divide & Conquer
| Algorithm | Input Format | Example |
|-----------|--------------|---------|
| Merge Sort | Comma-separated list | `5,3,1,2` |
| Quick Sort | Comma-separated list | `5,3,1,2` |
| Binary Search | `array;target` | `1,2,3,4;3` |

### Greedy
| Algorithm | Input Format | Example |
|-----------|--------------|---------|
| Fractional Knapsack | `values;weights;capacity` | `60,100;10,20;50` |
| Activity Selection | `starts;finishes` | `0,1,2,3;1,2,3,4` |

### Dynamic Programming
| Algorithm | Input Format | Example |
|-----------|--------------|---------|
| Fibonacci (DP) | Single integer | `10` |
| 0/1 Knapsack | `values;weights;capacity` | `60,100;10,20;50` |
| Longest Common Subsequence | `string1;string2` | `AGGTAB;GXTXAYB` |

### Backtracking
| Algorithm | Input Format | Example |
|-----------|--------------|---------|
| N-Queens | Single integer | `8` |

## 💡 Usage Examples

### Example 1: Merge Sort
1. Select **Divide & Conquer** paradigm
2. Select **Merge Sort** algorithm
3. Enter: `5,3,8,1,2`
4. Click **Run Algorithm**
5. See output: `[1, 2, 3, 5, 8]` with O(n log n) complexity

### Example 2: Fibonacci (DP)
1. Select **Dynamic Programming** paradigm
2. Select **Fibonacci (DP)** algorithm
3. Enter: `10`
4. Click **Run Algorithm**
5. See output: `55` (10th Fibonacci number)

### Example 3: N-Queens
1. Select **Backtracking** paradigm
2. Select **N-Queens Problem** algorithm
3. Enter: `8`
4. Click **Run Algorithm**
5. See number of solutions for 8-Queens puzzle

## 🎨 Interface Highlights

- **Category Dropdown**: Filter algorithms by paradigm
- **Algorithm Dropdown**: Dynamically populated based on selected category
- **Input Textarea**: Clear placeholder and format guide
- **Run Button**: Executes the selected algorithm
- **Results Panel**: Shows output, theoretical complexity, execution time, and explanation

## 📊 Output Information

Each result displays:
- **Output**: The actual result of the algorithm
- **Time Complexity**: Theoretical complexity analysis
- **Execution Time**: Measured runtime in milliseconds
- **Explanation**: Brief description of how the algorithm works

## 🔧 Configuration

To run on a different port, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

## 📝 Notes

- All algorithms are implemented in Python for consistency
- Measured execution times are in milliseconds
- For very small inputs, execution time may be dominated by overhead
- The app uses Flask's built-in server (not recommended for production)

## 🎓 Learning Resources

This playground is designed to help understand:
- Algorithm efficiency and time complexity analysis
- Different algorithmic paradigms and their characteristics
- Real-world performance vs. theoretical analysis
- Trade-offs between different algorithmic approaches

## 📄 License

This project is open for educational use.
