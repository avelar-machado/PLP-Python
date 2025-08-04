# Task 1
my_list = []
other_list = [50, 60, 70]

# Task 2
for i in range(1, 5):
    my_list.append(i * 10)

# Task 3
my_list[1] = 15

# Task 4
my_list.extend(other_list)

# Task 5
my_list.pop()

# Task 6
my_list.sort()

# Task 7
print("Index of 30:", my_list.index(30))

print("\nFinal list: ", my_list)