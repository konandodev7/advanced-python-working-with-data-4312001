# deque objects are like double-ended queues

import collections
import string


# initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# deques support the len() function
print("Item count: " + str(len(d)))

# TODO: deques can be iterated over
for elem in d:
    print(elem.upper())

# TODO: manipulate items from either end
d.pop()
print(d)
d.popleft()
print(d)
d.append(2)
print(d)


# TODO: use an index to get a particular item
d.rotate(1)
print(d)
print(d[1])
