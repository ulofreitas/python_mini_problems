"""
You're given strings jewels representing the types of stones that are jewels, and stones
representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".


Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "abc", stones = "ABC"
Output: 0

Example 3:
Input: jewels = "AbC", stones = "ABC"
Output: 2

Example 4:
Input: jewels = "py", stones = "Python is a language, but python is also a snake!"
Output: 3

Example 5:
Input: jewels = "sTrInG", stones = "STRINGS are really cool!"
Output: 5
"""

def numJewelsInStones(jewels, stones):
  """
  Input:
    jewels: a string
    stones: a string
  Output:
    number of jewels: integer
  """
  # Remove this and add your own code!
  return 0


# Testing
assert(numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3)
assert(numJewelsInStones(jewels="abc", stones="ABC") == 0)
assert(numJewelsInStones(jewels="AbC", stones="ABC") == 2)
assert(numJewelsInStones(jewels="py", stones="Python is a language, but python is also a snake!") == 3)
assert(numJewelsInStones(jewels="sTrInG", stones="STRINGS are really cool!") == 5)
# TODO: add more tests!

# If you see this message, that means your code works :D
print("✅✅ All tested passed ✅✅")