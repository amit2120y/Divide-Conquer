# 🎯 DAA Algorithms Playground - Complete Edition

An interactive web-based simulator for **Design & Analysis of Algorithms** with **17 algorithms** across four major paradigms: Divide & Conquer, Greedy, Dynamic Programming, and Backtracking.

## 📋 Features

- **Dynamic Algorithm Selection**: Choose paradigm → select specific algorithm
- **Real-Time Execution**: Run algorithms with custom input and see results instantly
- **Time Complexity Analysis**: Theoretical complexity + Number of operations
- **Input Format Guide**: Clear instructions for each algorithm's input format
- **Responsive Design**: Works on desktop and mobile browsers
- **Python-Based Algorithms**: Server-side Python execution via Flask

## 🏗️ Project Structure

```
.
├── app.py                      # Flask application & API endpoints
├── algorithms/                 # Algorithm implementations
│   ├── divide_conquer.py      # Merge Sort, Quick Sort, Binary Search, Heap Sort, Strassen
│   ├── greedy.py              # Fractional Knapsack, Activity Selection, Kruskal, Prim, Optimal Merge
│   ├── dynamic.py             # Fibonacci, 0/1 Knapsack, LCS, Matrix Chain, TSP
│   └── backtracking.py        # N-Queens, Naive String, Rabin-Karp, KMP
├── templates/
│   └── index.html             # Main UI template (Jinja2)
├── static/
│   ├── script.js              # Client-side JavaScript logic
│   └── style.css              # Styling
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. **Clone/Navigate to project**:
```bash
cd "path/to/Divide & Conquer"
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

## 📚 All Implemented Algorithms

### **Divide & Conquer (5 algorithms)**

| Algorithm | Input Format | Complexity | Example |
|-----------|--------------|-----------|---------|
| **Merge Sort** | Comma-separated list | O(n log n) | `5,3,1,2` |
| **Quick Sort** | Comma-separated list | O(n log n) avg | `5,3,1,2` |
| **Binary Search** | `array;target` | O(log n) | `1,2,3,4;3` |
| **Heap Sort** | Comma-separated list | O(n log n) | `5,3,8,1,2` |
| **Strassen's Matrix Multiply** | `size;matrix_values` | O(n^2.807) | `2;1,2,3,4,5,6,7,8` |

### **Greedy (5 algorithms)**

| Algorithm | Input Format | Complexity | Example |
|-----------|--------------|-----------|---------|
| **Fractional Knapsack** | `values;weights;capacity` | O(n log n) | `60,100;10,20;50` |
| **Activity Selection** | `start_times;finish_times` | O(n log n) | `0,1,2,3;1,2,3,4` |
| **Kruskal's Algorithm** | `vertices;edges` | O(E log E) | `4;0,1,1:0,2,4:1,2,2` |
| **Prim's Algorithm** | `vertices;edges` | O(E log V) | `4;0,1,1:0,2,4:1,2,2` |
| **Optimal Merge Pattern** | Comma-separated file sizes | O(n log n) | `10,20,30,40` |

### **Dynamic Programming (5 algorithms)**

| Algorithm | Input Format | Complexity | Example |
|-----------|--------------|-----------|---------|
| **Fibonacci (DP)** | Single integer | O(n) | `10` |
| **0/1 Knapsack** | `values;weights;capacity` | O(n × W) | `60,100;10,20;50` |
| **LCS** | `string1;string2` | O(n × m) | `AGGTAB;GXTXAYB` |
| **Matrix Chain Multiply** | Comma-separated dimensions | O(n^3) | `10,20,30,40` |
| **TSP (Travelling Salesman)** | Distance matrix (comma-separated) | O(n^2 × 2^n) | `0,2,9,10:2,0,10,3:9,10,0,7:10,3,7,0` |

### **Backtracking (4 algorithms)**

| Algorithm | Input Format | Complexity | Example |
|-----------|--------------|-----------|---------|
| **N-Queens Problem** | Single integer (n) | O(N!) | `8` |
| **Naive String Matching** | `text;pattern` | O((n-m+1)×m) | `ABCCDDEFF;CDD` |
| **Rabin-Karp Matching** | `text;pattern` | O(n+m) avg | `ABCCDDEFF;CDD` |
| **KMP Algorithm** | `text;pattern` | O(n+m) | `ABCCDDEFF;CDD` |

## 💡 Usage Examples

### Example 1: Merge Sort
1. Select **Divide & Conquer** paradigm
2. Select **Merge Sort** algorithm
3. Enter: `5,3,8,1,2`
4. Click **Run Algorithm**
5. Output: `[1, 2, 3, 5, 8]` with O(n log n) complexity

### Example 2: Kruskal's Algorithm
1. Select **Greedy** paradigm
2. Select **Kruskal's Algorithm**
3. Enter: `4;0,1,1:0,2,4:0,3,3:1,2,2:1,3,5:2,3,1`
   - 4 vertices
   - edges: (0-1, weight 1), (0-2, weight 4), etc.
4. Output: MST edges and total weight

### Example 3: TSP
1. Select **Dynamic Programming** paradigm
2. Select **TSP**
3. Enter: `0,10,15,20:10,0,35,25:15,35,0,30:20,25,30,0`
   - 4x4 distance matrix
4. Output: Minimum cost tour and path

### Example 4: KMP String Matching
1. Select **Backtracking** paradigm
2. Select **Knuth-Morris-Pratt**
3. Enter: `ABCCDDEFF;CDD`
4. Output: Indices where pattern is found

## 🎨 Interface Highlights

- **Category Dropdown**: Filter algorithms by paradigm
- **Algorithm Dropdown**: Dynamically populated based on selected category
- **Input Textarea**: Clear placeholder and format guide
- **Run Button**: Executes the selected algorithm
- **Results Panel**: Shows output, theoretical complexity, operations count, and explanation

## 📊 Output Information

Each result displays:
- **Output**: The actual result of the algorithm
- **Time Complexity**: Theoretical complexity analysis
- **Number of Operations**: Calculated based on input size and complexity formula
- **Execution Time**: Actual measured runtime in milliseconds
- **Explanation**: Detailed description of how the algorithm works

## 🔧 Configuration

To run on a different port, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Change to 8000
```

## 📝 Algorithm Details

### Divide & Conquer
- **Merge Sort**: Divides array, sorts recursively, merges results
- **Quick Sort**: Partitions around pivot, recursively sorts parts
- **Binary Search**: Finds element in sorted array by halving search space
- **Heap Sort**: Builds heap, extracts max repeatedly
- **Strassen**: Matrix multiplication using 7 recursive calls instead of 8

### Greedy
- **Fractional Knapsack**: Picks items by value-to-weight ratio
- **Activity Selection**: Picks activities by earliest finish time
- **Kruskal**: Builds MST by selecting edges in weight order
- **Prim**: Builds MST by growing from a starting vertex
- **Optimal Merge**: Merges files in order of smallest size first

### Dynamic Programming
- **Fibonacci**: Builds table to avoid recomputation
- **0/1 Knapsack**: DP table for max value with weight constraint
- **LCS**: 2D table to find longest common subsequence
- **Matrix Chain**: DP to find optimal multiplication order
- **TSP**: Bitmask DP to find shortest tour visiting all cities

### Backtracking
- **N-Queens**: Places queens safely using backtracking
- **Naive String Matching**: Checks every position
- **Rabin-Karp**: Uses rolling hash for fast matching
- **KMP**: Uses failure function to skip redundant comparisons

## 🧪 Test Cases

### Divide & Conquer: Merge Sort
```
Input: 9,5,2,7,1,8,3
Expected: [1, 2, 3, 5, 7, 8, 9]
Complexity: O(n log n)
```

### Greedy: Activity Selection
```
Input: 0,1,2,3;1,2,3,4
Expected: [(0,1), (2,3)]
Complexity: O(n log n)
```

### Dynamic Programming: LCS
```
Input: AGGTAB;GXTXAYB
Expected: 5 (LCS is "GTAB")
Complexity: O(n × m)
```

### Backtracking: KMP
```
Input: ABABAB;AB
Expected: [0, 2, 4]
Complexity: O(n+m)
```

## 🎓 Learning Resources

This playground helps understand:
- Algorithm efficiency and time complexity analysis
- Different algorithmic paradigms and their characteristics
- Real-world performance vs. theoretical analysis
- Trade-offs between different algorithmic approaches
- Graph algorithms (Kruskal, Prim)
- String matching techniques
- Travelling Salesman Problem solutions

## 📄 License

This project is open for educational use.

---

**Now featuring 17 algorithms across 4 paradigms!** 🚀
