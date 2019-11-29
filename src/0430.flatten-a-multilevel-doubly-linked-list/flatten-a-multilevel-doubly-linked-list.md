<p>You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.</p>

<p>Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

<strong>Output:</strong>
1-2-3-7-8-11-12-9-10-4-5-6-NULL
</pre>

<p>&nbsp;</p>

<p><strong>Explanation for the above example:</strong></p>

<p>Given the following multilevel doubly linked list:</p>

<pre>
<img src="https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlist.png" style="width: 640px;" /></pre>

<p>&nbsp;</p>

<p>We should return the following flattened doubly linked list:</p>

<pre>
<img src="https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlistflattened.png" style="width: 1100px;" /></pre>
