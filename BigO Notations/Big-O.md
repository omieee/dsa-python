# Big-O Notes

Reference: [NeetCode Big-O Notation](https://neetcode.io/courses/lessons/big-o-notation)

## What is Big-O notation?

Big-O notation describes how the time or space used by an algorithm grows as the input size grows.

In interviews, we usually use Big-O to explain the worst-case or expected growth of an algorithm.

Big-O ignores:

* machine speed
* small constants
* lower-order terms

Example:

```text
O(2n + 5) becomes O(n)
O(n² + n) becomes O(n²)
```

## Common Big-O complexities

| Notation   | Meaning           | Common example                                   |
| ---------- | ----------------- | ------------------------------------------------ |
| O(1)       | Constant time     | Accessing `arr[3]`, dictionary lookup on average |
| O(log n)   | Logarithmic time  | Binary search                                    |
| O(n)       | Linear time       | Looping through an array once                    |
| O(n log n) | Linearithmic time | Sorting                                          |
| O(n²)      | Quadratic time    | Nested loop over all pairs                       |
| O(2^n)     | Exponential time  | Trying all subsets                               |
| O(sqrt n)  | Square-root time  | Checking divisors up to square root              |
| O(n!)      | Factorial time    | Trying all permutations                          |

## O(1)

O(1) means the operation takes the same amount of time regardless of input size.

Examples:

```python
arr[3]
arr[3] = 10
student["name"]
student["name"] = "Om"
arr.append(3)
arr.pop()
```

Notes:

* `arr.append()` is usually O(1), technically amortized O(1).
* `arr.pop()` from the end is O(1).
* `arr.pop(0)` is not O(1). It is O(n), because elements must shift.

## O(log n)

O(log n) usually means the input is reduced by half each step.

Common example: binary search.

Binary search works only when the data is sorted.

Example idea:

```text
Search in 16 items
Check middle
Remaining search space becomes 8
Then 4
Then 2
Then 1
```

So instead of checking all `n` items, we repeatedly cut the search space in half.

Sorting is not O(log n). Sorting is usually O(n log n).

## O(n)

O(n) means runtime grows directly with input size.

If the input has 10 items, we may do about 10 operations.
If the input has 1,000 items, we may do about 1,000 operations.

Example:

```python
arr = [1, 2, 3]

for value in arr:
    print(value)
```

Other examples:

```python
target in arr
sum(arr)
max(arr)
```

These scan the list.

Important correction:

```python
arr[3] = 10
```

This is O(1), not O(n).

But this is O(n):

```python
del arr[3]
```

because elements after index `3` must shift left.

## O(n log n)

O(n log n) commonly appears in efficient sorting algorithms.

Examples:

```python
sorted(arr)
arr.sort()
```

For interview-level Python notes, treat sorting as O(n log n).

Common algorithms:

* merge sort
* heap sort
* most practical comparison sorting

## O(n²)

O(n²) usually appears when we compare every item with every other item.

Example:

```python
arr = [1, 2, 3]

for i in arr:
    for j in arr:
        print(i, j)
```

If `n = 3`, work is about `3 * 3 = 9`.

If `n = 1000`, work is about `1000 * 1000 = 1,000,000`.

This becomes slow quickly.

## O(2^n)

O(2^n) means exponential time.

This is not “two times n.”

It means the work roughly doubles when `n` increases by 1.

Example:

```text
n = 5  -> 32 possibilities
n = 10 -> 1024 possibilities
n = 20 -> 1,048,576 possibilities
```

Common example:

* generating all subsets of a set

## O(sqrt n)

O(sqrt n) means the work grows with the square root of `n`.

Common example: checking if a number is prime by testing divisors only up to `sqrt(n)`.

Why?

If `n = a * b`, then at least one of `a` or `b` must be less than or equal to `sqrt(n)`.

## O(n!)

O(n!) means factorial time.

Common example:

* generating all permutations

For `n = 5`:

```text
5! = 5 * 4 * 3 * 2 * 1 = 120
```

For `n = 10`:

```text
10! = 3,628,800
```

This becomes unusable very fast.

## Current weak areas

I need more practice with:

* binary search and why it is O(log n)
* why sorting is O(n log n)
* nested loops and O(n²)
* subsets and O(2^n)
* permutations and O(n!)

## Interview explanation template

For any DSA problem, explain complexity like this:

```text
Time complexity is O(__) because ...
Space complexity is O(__) because ...
```

Example:

```text
Time complexity is O(n) because we loop through the array once.
Space complexity is O(n) because we store values in a set.
```
