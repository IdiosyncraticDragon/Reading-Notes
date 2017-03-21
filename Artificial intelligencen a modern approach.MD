# Artificial intelligencen a modern approach
> author: Stuart J.Russell and Peter Norvig
> version: 2nd edition, 2003
> newest version: 3nd edition

## Informed Search and Exploration

### concepts
- <strong>city block distance</strong> or <strong>Manhattan distance</strong>: Consider the 2-d checkboard, the <font color="red">Manhattan distance</font> means the sum of the horizontal and vertical distances.
- <strong>Informed Search</strong>: one that uses problem-specific knowledge beyond the definition of the prblem itself.
- <strong>Best First Search</strong>: choose the node that appears to be best according to the evaluation function.
- <strong>Greedy best-first search</strong>: try to expand the node that is closet to goal. it evaluates nodes by using just the heuristic function: h(n)=f(n).
- <strong>Heuristic function f(n)</strong> aims at estimating the cost of the cheapest path from node n to a goal node
- Heuristic functions are the most common form in which additional knowledge of the problem is imparted to the search algorithm;
- A heuristic function h(x) takes a node as input, but it depends only on the state at that node.
- admissible heuristic -- that is, provided that h(n) never overestimates the cost to reach the goal. Admissible heuristics are by nature optimistic, because they think the cost of solving the problem is less than it actually is.
- $A^*$ search: it evaluates nodes by combining g(n), the cost to reach the node, and h(n) [maybe the heuristic], the cost to get from the node to the goal: $f(n) = g(n) + h(n)$
- $A^*$ is optimal if $h(n)$ is an admissible heuristic.
- Admissible heuristic: $h(n)$ never overestimates the cost to reach the goal;

### useful expressions

```
in order to shed light on the nature of heuristics in general;
can lead the search astray;
without ever doing sth;
by testing them against the goal;
```
