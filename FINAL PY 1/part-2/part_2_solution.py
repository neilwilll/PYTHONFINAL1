### Step 1 - Lists ###


my_authors = ["Charles Dickens", "Jules Verne", "Mark Twain", "Jane Austen", "Mary Shelley", "Edgar Allen Poe", "Victor Hugo", "Virginia Woolf"]


my_authors.append("Leo Tolstoy")
print(my_authors)


my_authors.remove("Mark Twain")
print(my_authors)


print(my_authors[2])



print(my_authors[2:5])



### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
my_author_tuple = ("Charles Dickens", "Jules Verne", "Mark Twain", "Jane Austen", "Mary Shelley", "Edgar Allen Poe", "Victor Hugo", "Virginia Woolf")


### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
my_author_set = {"Charles Dickens", "Jules Verne", "Mark Twain", "Jane Austen", "Mary Shelley", "Edgar Allen Poe", "Victor Hugo", "Virginia Woolf"}


# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_author_set.add("Fyodor Dostoevsky")
print(my_author_set)


# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
my_author_set.add("Fyodor Dostoevsky")
print(my_author_set)



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

for book in my_authors:
    print(book)

for book in my_author_tuple:
    print(book)

for book in my_author_set:
    print(book)