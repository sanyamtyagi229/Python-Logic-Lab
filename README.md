# Python-Logic-Lab
Implementation of efficient algorithmic patterns in Python
🪟 Sliding Window
Instead of recalculating the sum from scratch for every window (which is $O(n \times k)$), we "slide" the window by adding the next element and subtracting the previous one. This reduces the complexity to $O(n)$.


👈👉 Two-Pointer:
Placing pointers at both ends of a sorted array, we can converge on a solution in $O(n)$ time by moving pointers inward based on the current sum relative to the target.
