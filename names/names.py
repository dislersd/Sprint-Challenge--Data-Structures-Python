import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#  Slow Solution O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#  Fast Solution 1 runtime = 0.00585 
# def compare(x, y):
#     return set(x).intersection(y)

# duplicates = compare(names_1, names_2)

# Stretch solution
def intersection(x, y):
    result = []
    for elem in x:
        if elem in y:
            result.append(elem)
    return result

duplicates = intersection(names_1, names_2)

# List Comprehension
# duplicates = [x for x in names_1 if x in names_2]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

