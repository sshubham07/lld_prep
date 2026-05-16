Com+shift+v - to see markdown mode
# Rotated Sorted Array — Complete Revision Notes

---

# Core Idea

In every rotated sorted array:

```text
At least ONE HALF is always properly sorted.
```

Example:

```python
[4,5,6,7,0,1,2]
```

If mid = 7:

```text
Left  = [4,5,6,7]  -> sorted
Right = [0,1,2]    -> sorted
```

Your whole job:

```text
1. Find which half is sorted
2. Decide whether answer lies there
3. Eliminate one half
```

---

# MASTER TEMPLATE

```python
l, r = 0, len(nums)-1
ans = something

while l <= r:

    mid = (l + r) // 2

    # identify sorted half

    if nums[l] <= nums[mid]:

        # left sorted

    else:

        # right sorted
```

---

# HOW TO IDENTIFY SORTED HALF

## Left Sorted

```python
if nums[l] <= nums[mid]:
```

Means:

```text
Left side is perfectly sorted
```

Example:

```python
[4,5,6,7,0,1,2]
 l     mid
```

Since:

```python
4 <= 7
```

Left is sorted.

---

## Otherwise Right Sorted

```python
else:
```

Means:

```text
Right side is sorted
```

Example:

```python
[6,7,0,1,2,4,5]
      mid     r
```

---

# FIND MINIMUM IN ROTATED SORTED ARRAY

Problem:

```python
[4,5,6,7,0,1,2]
```

Answer:

```python
0
```

---

# Logic

## Case 1 — Left Half Sorted

```python
if nums[l] <= nums[mid]:
```

Example:

```python
[4,5,6,7]
```

IMPORTANT:

If left side is sorted:

```text
Smallest element of THIS HALF = nums[l]
```

Because sorted array's smallest element is first element.

So:

```python
ans = min(ans, nums[l])
```

Now:

```text
Minimum cannot be hidden INSIDE this left sorted half
```

Because we already took its smallest.

So move right:

```python
l = mid + 1
```

---

## Case 2 — Right Half Sorted

Else:

```text
Rotation/minimum lies in left side
```

Example:

```python
[6,7,0,1,2]
```

Here:

```python
nums[mid]
```

can be minimum candidate.

So:

```python
ans = min(ans, nums[mid])
```

Then search left:

```python
r = mid - 1
```

---

# Final Code

```python
def findMin(nums):

    l, r = 0, len(nums)-1

    ans = float('inf')

    while l <= r:

        mid = (l + r) // 2

        # LEFT HALF SORTED
        if nums[l] <= nums[mid]:

            ans = min(ans, nums[l])

            l = mid + 1

        # RIGHT HALF SORTED
        else:

            ans = min(ans, nums[mid])

            r = mid - 1

    return ans
```

---

# DRY RUN

```python
nums = [4,5,6,7,0,1,2]
```

## Iteration 1

```python
l = 0
r = 6
mid = 3
nums[mid] = 7
```

Check:

```python
nums[l] <= nums[mid]
4 <= 7 -> TRUE
```

Left sorted.

```python
ans = min(inf, 4) = 4
```

Move right:

```python
l = mid + 1 = 4
```

---

## Iteration 2

```python
l = 4
r = 6
mid = 5
nums[mid] = 1
```

Check:

```python
0 <= 1 -> TRUE
```

Left sorted.

```python
ans = min(4,0) = 0
```

Move right:

```python
l = 6
```

Done.

Answer:

```python
0
```

---

# MOST COMMON CONFUSION

Question:

```text
"Left sorted hai to minimum right me hi kyu?"
```

IMPORTANT:

We are NOT saying:

```text
minimum definitely right me hi hai
```

We are saying:

```text
left sorted half ka minimum already nums[l] hai
```

So no need to search entire left half anymore.

We safely discard it after storing its minimum candidate.

THAT is the real logic.

---

# SEARCH TARGET IN ROTATED SORTED ARRAY

Problem:

```python
nums = [4,5,6,7,0,1,2]
target = 0
```

---

# Main Logic

Instead of minimum:

We check:

```text
Target sorted half ke andar hai ya nahi
```

---

# Case 1 — Left Half Sorted

```python
if nums[l] <= nums[mid]:
```

Now check:

```python
nums[l] <= target < nums[mid]
```

If true:

```text
Target lies inside left half
```

Move left:

```python
r = mid - 1
```

Else:

```text
Target must be right side
```

Move right:

```python
l = mid + 1
```

---

# Case 2 — Right Half Sorted

Check:

```python
nums[mid] < target <= nums[r]
```

If true:

```python
l = mid + 1
```

Else:

```python
r = mid - 1
```

---

# Final Code

```python
def search(nums, target):

    l, r = 0, len(nums)-1

    ans = -1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == target:
            ans = mid
            break

        # LEFT SORTED
        if nums[l] <= nums[mid]:

            if nums[l] <= target < nums[mid]:

                r = mid - 1

            else:

                l = mid + 1

        # RIGHT SORTED
        else:

            if nums[mid] < target <= nums[r]:

                l = mid + 1

            else:

                r = mid - 1

    return ans
```

---

# EASY INTERVIEW MEMORY TRICK

## For MINIMUM

```text
Sorted side ka smallest le lo
Then opposite side search karo
```

---

## For TARGET SEARCH

```text
Check whether target belongs to sorted half
If yes -> go there
Else -> opposite
```

---

# DUPLICATES CASE

Problem:

```python
[1,1,1,0,1]
```

Now:

```python
nums[l] == nums[mid] == nums[r]
```

You cannot identify sorted side.

---

# Fix

Add this before everything:

```python
if nums[l] == nums[mid] == nums[r]:

    l += 1
    r -= 1

    continue
```

This shrinks useless duplicates.

---

# FULL UNIVERSAL TEMPLATE

```python
while l <= r:

    mid = (l + r) // 2

    # duplicate handling
    if nums[l] == nums[mid] == nums[r]:

        l += 1
        r -= 1
        continue

    # left sorted
    if nums[l] <= nums[mid]:

        # logic

    # right sorted
    else:

        # logic
```

---

# BIGGEST INTERVIEW MISTAKES

## Mistake 1

Using:

```python
while l < r
```

and getting confused.

Stick to:

```python
while l <= r
```

---

## Mistake 2

Forgetting:

```python
mid = (l + r) // 2
```

inside loop.

---

## Mistake 3

Confusing:

```python
nums[l]
```

vs

```python
nums[mid]
```

Remember:

```text
Sorted left half ka smallest = nums[l]
Sorted right half ka smallest = nums[mid]
```

---

# FINAL MENTAL MODEL

Whenever you see rotated sorted array:

Immediately think:

```text
One half sorted hai.
Bas wahi identify karna hai.
```

Then:

## For Search

```text
Target sorted half me hai?
```

## For Minimum

```text
Sorted half ka minimum leke dusri side jao
```

That is literally the entire topic.


## For Duplicate Elements
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        l=0
        h = len(nums)-1
        while l<=h:
            mid = h-(h-l)//2
            if nums[l] == nums[mid] == nums[h]:
                ans = min(ans, nums[l]) # safeguard: check the boundary element too
                l += 1
                h -= 1
                continue
            if nums[mid]>=nums[l]:
                ans = min(ans,nums[l])
                l=mid+1
            else:
                ans = min(ans,nums[mid])
                h=mid-1
        return ans
```
