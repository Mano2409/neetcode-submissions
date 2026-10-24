<h2><a href="https://www.naukri.com/code360/problems/insert-at-end-of-doubly-linked-list_8160464" target="_blank" rel="noopener noreferrer">Insert at end of Doubly Linked List</a></h2>

| | |
|---|---|
| **Difficulty** | Easy |
| **Language** | Python3 |
| **Verdict** | Accepted |
| **Problem Link** | [Code360](https://www.naukri.com/code360/problems/insert-at-end-of-doubly-linked-list_8160464) |

## Topics
_No topics available_

---

## Problem Statement

<h4 id="a-doubly-linked-list-is-a-data-structure-that-consists-of-sequentially-linked-nodes-and-the-nodes-have-reference-to-both-the-previous-and-the-next-nodes-in-the-sequence-of-nodes">A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.</h4>

<p><Br></p>

<h4 id="given-a-doubly-linked-list-and-a-value-k-insert-a-node-having-value-k-at-the-end-of-the-doubly-linked-list">Given a doubly-linked list and a value ‘k’, insert a node having value ‘k’ at the end of the doubly linked list.</h4>

<p><br/></p>

<h5 id="note">Note:</h5>

<pre><code>You need not print anything. You’re given the head of the linked list. Return the head of the modified list.
</code></pre>

<p><br/></p>

<h5 id="example">Example:</h5>

<pre><code>Input: Linked List: 4 &lt;-&gt; 10 &lt;-&gt; 3 &lt;-&gt; 5 and ‘k’ = 20

Output: Modified Linked List: 4 &lt;-&gt; 10 &lt;-&gt; 3 &lt;-&gt; 5 &lt;-&gt; 20

Explanation: A new node having value ‘k’ = 20 is inserted at the end of the linked list.
</code></pre>

<h5 id="input-format">Input Format:</h5>

<pre><code>The first line contains an integer ‘N’, the number of elements initially in the linked list.
The next line contains ‘N’ numbers, the linked list.
The third line contains an integer ‘k’, the value to be added.
</code></pre>

<p><br/></p>

<h5 id="output-format">Output format:</h5>

<pre><code>Return the head of the modified linked list.
</code></pre>


<h5 id="sample-input-1">Sample Input 1:</h5>

<pre><code>4
4 10 3 5
20
</code></pre>

<p><br/></p>

<h5 id="sample-output-1">Sample Output 1:</h5>

<pre><code>4 10 3 5 20
</code></pre>

<p><br/></p>

<h5 id="explanation-of-sample-input-1">Explanation Of Sample Input 1 :</h5>

<pre><code>A new node having value ‘k’ = 20 is inserted at the end of the linked list.
</code></pre>

<p><br/></p>

<h5 id="sample-input-2">Sample Input 2 :</h5>

<pre><code>0

5
</code></pre>

<p><br/></p>

<h5 id="sample-output-2">Sample Output 2 :</h5>

<pre><code>5
</code></pre>

<p><br/></p>

<h5 id="explanation-of-sample-input-2">Explanation Of Sample Input 2 :</h5>

<pre><code>The linked list was empty. So the new node is the only node in the modified linked list.
</code></pre>

<p><br/></p>

<h5 id="expected-time-complexity">Expected time complexity:</h5>

<pre><code>The expected time complexity is O(N).
</code></pre>

<p><br/></p>

<h5 id="constraints">Constraints:</h5>

<pre><code>0 &lt;= ‘N’ &lt;= 100000
1 &lt;= Value in linked list &lt;= 10^9
1 &lt;= ‘k’ &lt;= 10^9

Time limit: 1 second
</code></pre>
