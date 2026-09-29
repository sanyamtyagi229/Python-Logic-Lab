class Solution {
    public boolean hasValidPath(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // A valid path must have an even length.
        if ((m + n - 1) % 2 != 0) {
            return false;
        }
        
        // Start or end cells are impossible to balance
        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
            return false;
        }
        
        // Max possible open brackets we could ever have in a valid path is exactly half the total path length
        int maxOpen = (m + n - 1) / 2;
        boolean[][][] visited = new boolean[m][n][maxOpen + 1];
        
        return dfs(grid, 0, 0, 0, visited, maxOpen);
    }
    
    private boolean dfs(char[][] grid, int r, int c, int openCount, boolean[][][] visited, int maxOpen) {
        int m = grid.length;
        int n = grid[0].length;
        
        if (grid[r][c] == '(') {
            openCount++;
        } else {
            openCount--;
        }
        
        // 1. Cannot have negative open brackets (e.g., "())")
        // 2. Cannot exceed the maximum possible open brackets overall
        if (openCount < 0 || openCount > maxOpen) {
            return false;
        }
        
        // 3. Cannot have more open brackets than the exact number of remaining cells to close them
        int remainingSteps = (m - 1 - r) + (n - 1 - c);
        if (openCount > remainingSteps) {
            return false;
        }
        
        // Reached the destination
        if (r == m - 1 && c == n - 1) {
            return openCount == 0;
        }
        
        // If already visited this exact state, avoid recomputing
        if (visited[r][c][openCount]) {
            return false;
        }
        visited[r][c][openCount] = true;
        
        // Move down
        if (r < m - 1 && dfs(grid, r + 1, c, openCount, visited, maxOpen)) {
            return true;
        }
        // Move right
        if (c < n - 1 && dfs(grid, r, c + 1, openCount, visited, maxOpen)) {
            return true;
        }
        
        return false;
    }
}