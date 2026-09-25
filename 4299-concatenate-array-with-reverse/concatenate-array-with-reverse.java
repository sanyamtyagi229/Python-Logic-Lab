class Solution {
    public int[] concatWithReverse(int[] nums) {
        int n = nums.length;
        int[] result = new int[2 * n];
        
        for (int i = 0; i < n; i++) {
            result[i] = nums[i];
            result[2 * n - 1 - i] = nums[i]; 
        }
        
        return result;
    }
}