from flask import Flask, render_template, request, jsonify
import time
import traceback

from algorithms.divide_conquer import merge_sort, quick_sort, binary_search
from algorithms.greedy import fractional_knapsack, activity_selection
from algorithms.dynamic import fibonacci, knapsack_dp, lcs
from algorithms.backtracking import n_queens

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    data = request.json
    category = data.get('category')
    algo = data.get('algorithm')
    input_data = data.get('input', '').strip()

    if not input_data:
        return jsonify({"error": "Input data cannot be empty"})

    start = time.time()
    output = None
    complexity = ""
    explanation = ""

    try:
        if category == "divide":
            if algo == "merge_sort":
                arr = list(map(int, input_data.split(',')))
                output = merge_sort(arr)
                n = len(arr)
                complexity = "O(n log n)"
                operations = int(n * (len(bin(n)) - 2))  # n * log2(n)
                explanation = f"Divide the array into halves, recursively sort each half, then merge them back together. With n={n}, operations ≈ {operations}"

            elif algo == "quick_sort":
                arr = list(map(int, input_data.split(',')))
                output = quick_sort(arr)
                n = len(arr)
                complexity = "O(n log n) average, O(n²) worst case"
                operations = int(n * (len(bin(n)) - 2))  # n * log2(n) for average case
                explanation = f"Uses a pivot element to partition the array recursively. With n={n}, avg operations ≈ {operations}"

            elif algo == "binary_search":
                parts = input_data.split(';')
                if len(parts) != 2:
                    return jsonify({"error": "Binary search requires format: 'array;target' (e.g., '1,2,3,4;3')"})
                arr = sorted(list(map(int, parts[0].split(','))))
                target = int(parts[1])
                result = binary_search(arr, target)
                output = f"Found at index {result}" if result != -1 else "Not found"
                n = len(arr)
                complexity = "O(log n)"
                operations = len(bin(n)) - 2  # log2(n)
                explanation = f"Eliminates half of the remaining elements in each iteration. With n={n}, operations ≈ {operations}"

            else:
                return jsonify({"error": f"Unknown algorithm: {algo}"})

        elif category == "greedy":
            if algo == "fractional_knapsack":
                parts = input_data.split(';')
                if len(parts) != 3:
                    return jsonify({"error": "Fractional knapsack requires format: 'values;weights;capacity' (e.g., '60,100;10,20;50')"})
                values = list(map(int, parts[0].split(',')))
                weights = list(map(int, parts[1].split(',')))
                capacity = int(parts[2])
                output = fractional_knapsack(values, weights, capacity)
                n = len(values)
                complexity = "O(n log n)"
                operations = int(n * (len(bin(n)) - 2))  # n * log2(n) for sorting
                explanation = f"Greedily selects items with the highest value-to-weight ratio first. With n={n} items, operations ≈ {operations}"

            elif algo == "activity_selection":
                parts = input_data.split(';')
                if len(parts) != 2:
                    return jsonify({"error": "Activity selection requires format: 'start_times;finish_times' (e.g., '0,1,2,3;1,2,3,4')"})
                start_times = list(map(int, parts[0].split(',')))
                finish_times = list(map(int, parts[1].split(',')))
                result = activity_selection(start_times, finish_times)
                output = str(result)
                n = len(start_times)
                complexity = "O(n log n)"
                operations = int(n * (len(bin(n)) - 2))  # n * log2(n) for sorting
                explanation = f"Sorts activities by finish time and greedily selects non-overlapping ones. With n={n} activities, operations ≈ {operations}"

            else:
                return jsonify({"error": f"Unknown algorithm: {algo}"})

        elif category == "dynamic":
            if algo == "fibonacci":
                try:
                    n = int(input_data)
                    if n < 0:
                        return jsonify({"error": "Fibonacci index must be non-negative"})
                    output = fibonacci(n)
                    complexity = "O(n)"
                    operations = n
                    explanation = f"Uses dynamic programming table to compute fib({n}) without recomputation. With n={n}, operations = {operations}. Result = {output}"
                except ValueError:
                    return jsonify({"error": "Fibonacci requires a single integer"})

            elif algo == "knapsack":
                parts = input_data.split(';')
                if len(parts) != 3:
                    return jsonify({"error": "0/1 Knapsack requires format: 'values;weights;capacity' (e.g., '60,100;10,20;50')"})
                values = list(map(int, parts[0].split(',')))
                weights = list(map(int, parts[1].split(',')))
                capacity = int(parts[2])
                output = knapsack_dp(values, weights, capacity)
                n = len(values)
                w = capacity
                complexity = "O(n × W)"
                operations = n * w
                explanation = f"Uses DP table dp[i][w] = max value with first i items and weight w. With n={n} items, W={w}, operations ≈ {operations}"

            elif algo == "lcs":
                parts = input_data.split(';')
                if len(parts) != 2:
                    return jsonify({"error": "LCS requires format: 'string1;string2' (e.g., 'AGGTAB;GXTXAYB')"})
                s1, s2 = parts[0], parts[1]
                output = lcs(s1, s2)
                n = len(s1)
                m = len(s2)
                complexity = "O(n × m)"
                operations = n * m
                explanation = f"Finds longest subsequence common to both strings using 2D DP. String1 length={n}, String2 length={m}, operations ≈ {operations}. LCS length = {output}"

            else:
                return jsonify({"error": f"Unknown algorithm: {algo}"})

        elif category == "backtracking":
            if algo == "nqueens":
                try:
                    n = int(input_data)
                    if n <= 0:
                        return jsonify({"error": "N-Queens requires a positive integer"})
                    result = n_queens(n)
                    output = f"Found {len(result)} solution(s) for {n}-Queens"
                    complexity = "O(N!)"
                    operations = 1
                    for i in range(1, n + 1):
                        operations *= i  # Calculate factorial
                    explanation = f"Tries all possible placements of {n} queens, pruning branches where conflicts occur. With n={n}, operations ≈ {operations} (factorial)"
                except ValueError:
                    return jsonify({"error": "N-Queens requires a single integer"})

            else:
                return jsonify({"error": f"Unknown algorithm: {algo}"})

        else:
            return jsonify({"error": f"Unknown category: {category}"})

        end = time.time()
        elapsed = f"{(end - start) * 1000:.2f} ms"

        return jsonify({
            "output": output,
            "complexity": complexity,
            "operations": operations,
            "time": elapsed,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": f"Execution error: {str(e)}\n{traceback.format_exc()}"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)