Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1)
Constant time to add to array 
2. What is the space complexity of your ring buffer's `append` function?
O(1)
Only using one space at most
3. What is the runtime complexity of your ring buffer's `get` method?
O(n)
It increases in linear fashion as capacity increases
4. What is the space complexity of your ring buffer's `get` method?
O(n)
n values in array
5. What is the runtime complexity of the provided code in `names.py`?
O(n^2)
nested for loop - for each item in one list, loop entire other list
6. What is the space complexity of the provided code in `names.py`?
O(n)
n values for each duplicate
7. What is the runtime complexity of your optimized code in `names.py`?
O(n)
It runs for the min length of n elements in either set
8. What is the space complexity of your optimized code in `names.py`?
O(n)
going over each element once in shorter list
