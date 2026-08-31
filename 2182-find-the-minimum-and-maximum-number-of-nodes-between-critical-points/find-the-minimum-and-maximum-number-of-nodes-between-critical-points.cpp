/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        if (!head || !head->next || !head->next->next) {
            return {-1, -1};
        } // ADDED MISSING CLOSING BRACE HERE

        int min_dist = INT_MAX;
        int first_idx = -1;
        int prev_idx = -1;
        ListNode* prev = head;
        ListNode* curr = head->next;
        int idx = 1;

        while (curr->next) {
            ListNode* nxt = curr->next;
            bool is_maxima = (curr->val > prev->val) && (curr->val > nxt->val);
            bool is_minima = (curr->val < prev->val) && (curr->val < nxt->val);
            
            if (is_maxima || is_minima) {
                if (first_idx == -1) {
                    first_idx = idx;
                } else {
                    min_dist = min(min_dist, idx - prev_idx);
                }
                prev_idx = idx;
            }

            prev = curr;
            curr = nxt;
            idx++;
        }
        
        if (min_dist == INT_MAX) {
            return {-1, -1};
        }
        
        int max_dist = prev_idx - first_idx;
        return {min_dist, max_dist}; 
    }
};