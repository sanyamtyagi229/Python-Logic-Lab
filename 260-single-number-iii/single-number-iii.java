class Solution {
    public int[] singleNumber(int[] nums) {
        // Step 1: Get the XOR of the two unique numbers
        int xorAll = 0;
        for (int num : nums) {
            xorAll ^= num;
        }
        
        // Step 2: Find the rightmost set bit to use as a mask
        // This bit is 1, meaning the two unique numbers differ at this position
        int mask = xorAll & (-xorAll);
        
        // Step 3: Partition the numbers into two groups and XOR them
        int num1 = 0;
        int num2 = 0;
        for (int num : nums) {
            if ((num & mask) == 0) {
                num1 ^= num;  // Group with the bit set to 0
            } else {
                num2 ^= num;  // Group with the bit set to 1
            }
        }
        
        return new int[]{num1, num2};
    }
}