def isAnagramCheckoff(s1, s2):
   otherchars = list(s2)
   pos1 = 0
   stillOK = True

   while pos1 < len(s1) and stillOK:
      pos2 = 0
      found = False
      while pos2 < len(otherchars) and not found:
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
