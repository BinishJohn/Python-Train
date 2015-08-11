#
from collections import deque

def deque_functions():
  d = deque('Binish')
  for elem in d:
     print elem

if __name__ == '__main__':
  deque_functions()

'''
Deque objects support the following methods:

append(x)

    Add x to the right side of the deque.

appendleft(x)

    Add x to the left side of the deque.

clear()

    Remove all elements from the deque leaving it with length 0.

count(x)

    Count the number of deque elements equal to x.

    New in version 2.7.

extend(iterable)

    Extend the right side of the deque by appending elements from the iterable argument.

extendleft(iterable)

    Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

pop()

    Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft()

    Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value)

    Removed the first occurrence of value. If not found, raises a ValueError.

    New in version 2.5.

reverse()

    Reverse the elements of the deque in-place and then return None.

    New in version 2.7.

rotate(n)

    Rotate the deque n steps to the right. If n is negative, rotate to the left. Rotating one step to the right is equivalent to: d.appendleft(d.pop()).

'''
