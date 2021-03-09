/*
* 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int num = 0;
        int num1 = 0;
        string t = "";
        for (int i = 0; i < s.length(); i++) {
            bool flag = false;
            int j = 0;
            for (j = 0; j < t.length(); j++) {
                if (s[i] == t[j]) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                t += s[i];
                num1++;
            }
            else {
                if (num1 > num) {
                    num = num1;
                }
                t = t.substr(j + 1, t.length() - 1) + s[i];
                num1 = t.length();
                flag = false;

            }
        }
        if (num < num1) {
            num = num1;
        }
        return num;
    }
};
