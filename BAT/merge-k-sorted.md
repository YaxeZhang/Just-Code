### 合并k个排序列表
#### 题目
合并k个排序的链表，并将其作为一个排序表返回。分析并描述其复杂性。
#### 解法
**分析：**

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = list(filter(None,lists))
        if not lists:
            return None
        dummy = res = ListNode(0)
        while lists:
            tmp = [l.val for l in lists]
            idx = tmp.index(min(tmp))
            res.next = lists[idx]
            res = res.next
            lists[idx] = lists[idx].next
            lists = list(filter(None,lists))
        return dummy.next
```

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
```

```python
class Solution(object):
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
```

```python
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = None
        r = None
        q = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(q, (lists[i].val, i))

        while q:
            _, i = heapq.heappop(q)
            tmp, lists[i] = lists[i], lists[i].next
            if lists[i] is not None:
                heapq.heappush(q, (lists[i].val, i))
            tmp.next = None
            if r is None:
                r = tmp
                res = r
            else:
                r.next = tmp
                r = r.next

        return res
```
