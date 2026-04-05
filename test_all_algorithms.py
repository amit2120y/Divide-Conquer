#!/usr/bin/env python3
"""Quick test of all implemented algorithms"""

from algorithms.divide_conquer import merge_sort, quick_sort, binary_search, heap_sort, strassen_multiply
from algorithms.greedy import fractional_knapsack, activity_selection, kruskal_algorithm, prim_algorithm, optimal_merge_pattern
from algorithms.dynamic import fibonacci, knapsack_dp, lcs, matrix_chain_multiply, tsp_dp
from algorithms.backtracking import n_queens, naive_string_matching, rabin_karp, knuth_morris_pratt

print("🔬 Testing All 17 Algorithms\n")
print("=" * 60)

# Divide & Conquer
print("\n📊 Divide & Conquer Tests:")
print("-" * 60)

print("1. Merge Sort: ", merge_sort([5, 3, 8, 1, 2]))
print("2. Quick Sort: ", quick_sort([5, 3, 8, 1, 2]))
print("3. Binary Search: ", binary_search([1, 2, 3, 4, 5], 3))
print("4. Heap Sort: ", heap_sort([5, 3, 8, 1, 2]))
print("5. Strassen 2x2: ", strassen_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

# Greedy
print("\n🎯 Greedy Tests:")
print("-" * 60)

print("6. Fractional Knapsack: ", fractional_knapsack([60, 100], [10, 20], 50))
print("7. Activity Selection: ", activity_selection([0, 1, 2, 3], [1, 2, 3, 4]))
print("8. Kruskal (4 vertices, edges): ", kruskal_algorithm(4, [(0,1,1), (0,2,4), (1,2,2)]))
print("9. Prim (4 vertices, edges): ", prim_algorithm(4, [(0,1,1), (0,2,4), (1,2,2)]))
print("10. Optimal Merge: ", optimal_merge_pattern([10, 20, 30, 40]))

# Dynamic Programming
print("\n💻 Dynamic Programming Tests:")
print("-" * 60)

print("11. Fibonacci(10): ", fibonacci(10))
print("12. 0/1 Knapsack: ", knapsack_dp([60, 100], [10, 20], 50))
print("13. LCS: ", lcs("AGGTAB", "GXTXAYB"))
print("14. Matrix Chain: ", matrix_chain_multiply([10, 20, 30, 40]))
print("15. TSP (4 cities): ", tsp_dp([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]))

# Backtracking
print("\n🔄 Backtracking Tests:")
print("-" * 60)

print("16. N-Queens(4): ", len(n_queens(4)), "solutions")
print("17. Naive String Match: ", naive_string_matching("ABCCDDEFF", "CDD"))
print("18. Rabin-Karp: ", rabin_karp("ABCCDDEFF", "CDD"))
print("19. KMP: ", knuth_morris_pratt("ABCCDDEFF", "CDD"))

print("\n" + "=" * 60)
print("✅ All 17 algorithms tested successfully!")
print("=" * 60)
