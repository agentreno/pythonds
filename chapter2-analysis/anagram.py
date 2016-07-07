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

