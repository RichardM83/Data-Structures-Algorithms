/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0) {
            return head;
        }

        int length = 1;
        ListNode curr = head;

        while (curr.next != null) {
            length++;
            curr = curr.next;
        }

        k = k % length;
        curr.next = head;
        curr = head;

        for (int i = 0; i<length-k-1; i++){
            curr = curr.next;
        }
        head = curr.next;
        curr.next = null;
        return head;

    }
}







