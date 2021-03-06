/*
* 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
* 请你将两个数相加，并以相同形式返回一个表示和的链表。
* 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
*/

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head1 = l1;
        ListNode* head2 = l2;
        ListNode* res = new ListNode;
        ListNode* next = new ListNode;
        ListNode* now = res;
        res->next = next;
        int r1 = 0;
        int r2 = 0;
        while (head1 != nullptr && head2 != nullptr) {
            int t1 = head1->val + head2->val + r2;
            if (t1 >= 10) {
                r1 = t1 % 10;
                r2 = t1 / 10;
            }
            else {
                r1 = t1;
                r2 = 0;
            }
            next->val = r1;
            ListNode* next2 = new ListNode;
            next->next = next2;
            now = next;
            next = next2;
            head1 = head1->next;
            head2 = head2->next;
        }
        if (head1 != nullptr) {
            while (head1 != nullptr) {
                int t1 = head1->val + r2;
                if (t1 >= 10) {
                    r1 = t1 % 10;
                    r2 = t1 / 10;
                }
                else {
                    r1 = t1;
                    r2 = 0;
                }
                next->val = r1;
                head1 = head1->next;
                ListNode* next2 = new ListNode;
                next->next = next2;
                now = next;
                next = next2;
            }
        }
        if (head2 != nullptr) {
            while (head2 != nullptr) {
                int t1 = head2->val + r2;
                if (t1 >= 10) {
                    r1 = t1 % 10;
                    r2 = t1 / 10;
                }
                else {
                    r1 = t1;
                    r2 = 0;
                }
                next->val = r1;
                head2 = head2->next;
                ListNode* next2 = new ListNode;
                next->next = next2;
                now = next;
                next = next2;
            }
        }
        if (r2 != 0) {
            next->val = r2;
            ListNode* next2 = new ListNode;
            next->next = next2;
            now = next;
            next = next2;
        }
        res = res->next;
        now->next = nullptr;
        return res;
    }
};