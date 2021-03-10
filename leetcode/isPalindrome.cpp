/*
* 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
* 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
*/

class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> xList = {};
        int xT = x;
        if (x >= 0) {
            while (xT / 10 != 0) {
                xList.push_back(xT % 10);
                xT /= 10;
            }
            xList.push_back(xT);
            for (int i = 0; i < xList.size() / 2; i++) {
                if (xList[i] != xList[xList.size() - i - 1]) {
                    return false;
                }
            }
            return true;
        }
        else {
            return false;
        }
    }
};