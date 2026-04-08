from patterns import ArrayAlgorithms

# Sample Data
nums = [2, 1, 5, 1, 3, 2]
algo = ArrayAlgorithms(nums)

# Test Sliding Window
print(f"Max Sum (k=3): {algo.sliding_window_max_sum(3)}") # Expected: 9
