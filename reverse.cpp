/*
* 给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
* 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
* 假设环境不允许存储 64 位整数（有符号或无符号）。
*/

class Solution {
public:
    int reverse(int x) {
        int xT = x;
        vector<long> xList = {};
        while (xT / 10 != 0) {
            xList.push_back(xT % 10);
            xT = xT / 10;
        }
        xList.push_back(xT);
        float ii = 0.1;
        long res = 0;
        for (int i = xList.size() - 1; i >= 0; i--) {
            ii = ii * 10;
            int it = ii;
            res += xList[i] * it;
        }
        return (int)res == res ? (int)res : 0;
    }
};