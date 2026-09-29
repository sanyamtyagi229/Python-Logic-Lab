import java.util.ArrayList;
import java.util.List;

class Solution {
    public List getRow(int rowIndex) {
        List row = new ArrayList<>();
        long val = 1; // Use long to prevent integer overflow during multiplication
        
        for (int i = 0; i <= rowIndex; i++) {
            row.add((int) val);
            // Calculate the next value based on the current value
            val = val * (rowIndex - i) / (i + 1);
        }
        
        return row;
    }
}