# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

def sameTree(p,q):
    if len(p) != len(q):
        return False
    for i in range(len(p)):
        for j in range(i):
            if p[i] != q[j]:
                rr =  False
            else:
                rr =  True
        
    return rr

p = [1,3]
q = [1,2,3]

response = sameTree(p,q)
print(response)