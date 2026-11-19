import unittest
from dsa.sorting import quicksort, mergesort
from dsa.graphs import dijkstra, bfs
from dsa.dp import longest_common_subsequence, knapsack

class TestDSA(unittest.TestCase):
    def test_sorting(self):
        data = [9, 3, 7, 1, 5, 8, 2, 6, 4]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(quicksort(data), expected)
        self.assertEqual(mergesort(data), expected)

    def test_dijkstra(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        distances = dijkstra(graph, 'A')
        self.assertEqual(distances['D'], 4)

    def test_dp(self):
        self.assertEqual(longest_common_subsequence("abcde", "ace"), 3)
        self.assertEqual(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5), 7)

if __name__ == "__main__":
    unittest.main()
