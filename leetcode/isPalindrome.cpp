/*
* ����һ������ x ����� x ��һ���������������� true �����򣬷��� false ��
* ��������ָ���򣨴������ң��͵��򣨴������󣩶�����һ�������������磬121 �ǻ��ģ��� 123 ���ǡ�
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