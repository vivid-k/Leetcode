# coding=utf-8
'''
@Author: lost-person
@Date: 2020-01-31 10:46:17
@Description: 
@LastEditTime : 2020-02-14 17:29:10
@FilePath: \leetcode\test.py
'''

import math
import bisect
from collections import Counter, defaultdict, deque
from typing import List
from queue import PriorityQueue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class UnionFind:
    def __init__(self, n):
        super().__init__()
        self.cnt = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def get_cnt(self):
        return self.cnt

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def is_connect(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return

        if self.rank[root_p] > self.rank[root_q]:
            self.parent[q] = root_p
            self.rank[p] += self.rank[q]
        else:
            self.parent[p] = root_q
            self.rank[q] += self.rank[p]
        self.cnt -= 1

class Trie:
    def __init__(self):
        super().__init__()
        self.look_up = {}
    
    def insert(self, s: str):
        trie = self.look_up
        for c in s:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        # 结束符
        trie['#'] = '#'

class Solution:
    def lower_bound(self, array, left, right, target):
        while left < right: # 返回[first, last)内第一个不小于value的值的位置
            mid = left + ((right - left) >> 1) # 搜索区间[first, last)不为空
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return array[left]
       
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(2)
t5 = TreeNode(1)
t6 = TreeNode(3)
t7 = TreeNode(3)
t8 = TreeNode(-2)
t9 = TreeNode(1)
# t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5
# t3.right = t6
# t4.left = t7
# t4.right = t8
# t5.right = t9
t1.left = t3
t1.right = t2

t4.left = t5
t4.right = t6

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
s = Solution()
print(s.lower_bound([5, 10, 15, 20, 25, 30, 35, 40, 45, 50], 0, 9, 43))
