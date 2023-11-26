# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# class Solution:

def addTwoNumbers(l1, l2):
    
    for i in range(len(l1)):
        for j in i:
            l3 = l1[i]+l2[j]
    print(l3)

l1 = [2,4,3]
l2 = [5,6,4]
l3 = addTwoNumbers(l1,l2)

