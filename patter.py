class ArrayAlgorithms:
    def __init__(self, data):
        self.data = data

    def sliding_window_max_sum(self, k):
        """Finds the maximum sum of a subarray of size k."""
        if not self.data or k > len(self.data):
            return 0
        
        max_sum = current_sum = sum(self.data[:k])
        for i in range(len(self.data) - k):
            current_sum = current_sum - self.data[i] + self.data[i + k]
            max_sum = max(max_sum, current_sum)
        return max_sum

    def two_pointer_sum(self, target):
        """Checks if two numbers in a sorted list add up to target."""
        left, right = 0, len(self.data) - 1
        while left < right:
            s = self.data[left] + self.data[right]
            if s == target:
                return True, (self.data[left], self.data[right])
            elif s < target:
                left += 1
            else:
                right -= 1
        return False
