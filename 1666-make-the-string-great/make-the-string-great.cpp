class Solution {
public:
    string makeGood(string s) {
        string ans;
        int i=0;
        while(i!=s.length()){
            if(ans.empty()){
                ans.push_back(s[i]);
            }
            else if(ans.back()==s[i]+32||ans.back()==s[i]-32){
                ans.pop_back();
            }
            else {
                ans.push_back(s[i]);
            }
            i++;

        }
        return ans;
    }
};