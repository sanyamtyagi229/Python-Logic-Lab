class Solution {
public:
    int minimumIndex(vector<int>& capacity, int itemSize) {
        pair<int, int> ans{1e9, 1e9};
        for (int i = 0; i < capacity.size(); i++) {
            if (capacity[i] >= itemSize)
                ans = min(ans, {capacity[i], i});
        }
        if (ans.first == 1e9)
            return -1;
        return ans.second;
    }
};