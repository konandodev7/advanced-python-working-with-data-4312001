# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = [
    "Bob",
    "James",
    "Chad",
    "Darcy",
    "Penny",
    "Hannah",
    "Kevin",
    "James",
    "Melanie",
    "Becky",
    "Steve",
    "Frank",
]

# list of students in class 2
class2 = [
    "Bill",
    "Barry",
    "Cindy",
    "Debbie",
    "Frank",
    "Gabby",
    "Kelly",
    "James",
    "Joe",
    "Sam",
    "Tara",
    "Ziggy",
]

# TODO: Create a Counter for class1 and class2
counter1 = Counter(class1)
counter2 = Counter(class2)

# TODO: How many students in class 1 named James?
print(counter1["James"])

# TODO: How many students are in class 1?
print(sum(counter1.values()))

# TODO: Combine the two classes
counter1.update(counter2)
print(sum(counter1.values()))

# TODO: What's the most common name in the two classes?
print(counter1.most_common(3))

# TODO: Separate the classes again
counter1.subtract(counter2)

# TODO: What's common between the two classes?
print(counter1 & counter2)
