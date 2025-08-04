# Task 1
numbers = input("Enter a list of integers separated by spaces: ")
int_list = [int(num) for num in numbers.split()]
total = sum(int_list)
print("Sum of the integers:", total)

# Task 2
favorite_books = (
    "1984",
    "To Kill a Mockingbird",
    "Pride and Prejudice",
    "The Hobbit",
    "The Catcher in the Rye"
)

print("\nMy Favorite Books:")
for book in favorite_books:
    print(book)

# Task 3
person_info = {}
person_info["name"] = input("Enter your name: ")
person_info["age"] = input("Enter your age: ")
person_info["favorite_color"] = input("Enter your favorite color: ")

print("\nPerson Information:")
print(person_info)

# Task 4
set1 = set(map(int, input("Enter the first set of integers (space-separated): ").split()))
set2 = set(map(int, input("Enter the second set of integers (space-separated): ").split()))

common = set1.intersection(set2)
print("Common elements:", common)

# Task 5
words = ["apple", "banana", "kiwi", "orange", "grape", "fig", "melon"]
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)
