# First solution for anagram checking
# Checks off each character from first in second string
# Each n character in s1 results in up to n checks in s2
# Running time is sum of consecutive integers which is O(n^2)
def isAnagramCheckoff(s1, s2):
   otherchars = list(s2)
   pos1 = 0
   stillOK = True

   while pos1 < len(s1) and stillOK:
      pos2 = 0
      found = False
      while pos2 < len(otherchars) and not found:
         print("Comparing " + s1[pos1] + " to " + otherchars[pos2])
         if s1[pos1] == otherchars[pos2]:
            found = True
            otherchars[pos2] = None
         else:
            pos2 = pos2 + 1

      if found:
         otherchars[pos2] = None
      else:
         stillOK = False

      pos1 = pos1 + 1

   return stillOK

# Second solution for anagram checker
# Sorts the strings then compares them
# Running time equivalent to that of the sorting algorithm which is O(n log n)
def isAnagramSort(s1, s2):
   alist1 = list(s1)
   alist2 = list(s2)

   alist1.sort()
   alist2.sort()

   pos = 0
   matches = True

   while pos < len(s1) and matches:
      if alist1[pos] == alist2[pos]:
         pos = pos + 1
      else:
         matches = False

   return matches

def isAnagramBrute(s1, s2):
   # Generate every permutation of s1 and compare to s2
   pass

# Fourth solution for anagram checker
# Stores a character count map for each string and compares
# Each map creation is based on n and the map comparison is 26 compares
# Running time is 2n + 26 or linear, O(n) at the cost of map storage
def isAnagramCounts(s1, s2):
   c1 = [0] * 26
   c2 = [0] * 26

   for i in range(len(s1)):
      pos = ord(s1[i]) - ord('a')
      c1[pos] = c1[pos] + 1

   for i in range(len(s2)):
      pos = ord(s2[i]) - ord('a')
      c2[pos] = c2[pos] + 1

   j = 0
   stillOK = True
   while j < 26 and stillOK:
      if c1[j] == c2[j]:
         j = j + 1
      else:
         stillOK = False

   return stillOK

