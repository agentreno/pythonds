def merge_sort(items):
   if len(items) > 1:
      mid = len(items) / 2
      left = items[0:mid]
      right = items[mid:]

      merge_sort(left)
      merge_sort(right)

      leftindex = 0
      rightindex = 0
      for i in range(len(items)):
         lval = left[leftindex] if leftindex < len(left) else None
         rval = right[rightindex] if rightindex < len(right) else None

         if (lval and rval and lval < rval) or rval is None:
            items[i] = lval
            leftindex += 1
         elif (lval and rval and lval > rval) or lval is None:
            items[i] = rval
            rightindex += 1
         else:
            raise Exception('Could not merge, sub array sizes do not match')

def kthsmallest_merge(items, k):
   merge_sort(items)
   return items[k - 1]
