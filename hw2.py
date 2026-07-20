# Store a short paragraph using a multiline string
paragraph = """
Python is a popular programming language.
This Python course teaches the basics of Python,
including variables, loops, functions, and strings.
It is easy to learn and suitable for beginners.
"""

# Display the length of the paragraph
print("Length of paragraph:", len(paragraph))

# Display the first and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# Slice and print the first 50 characters
print("\nPreview:")
print(paragraph[:50])

# Replace "Python" with "PYTHON"
updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing 'Python' with 'PYTHON':")
print(updated_paragraph)

# Convert the paragraph to lowercase
lowercase_paragraph = paragraph.lower()
print("\nParagraph in lowercase:")
print(lowercase_paragraph)

# Remove extra whitespaces from the start and end
trimmed_paragraph = paragraph.strip()
print("\nParagraph after removing extra spaces:")
print(trimmed_paragraph)

# Split the paragraph into words
words = trimmed_paragraph.split()
print("\nList of words:")
print(words)

# Check if the word "course" exists
if "course" in trimmed_paragraph:
    print("\nThe word 'course' was found in the paragraph.")
else:
    print("\nThe word 'course' was not found in the paragraph.")

# Display the final message using format()
print("\nThe course description is {} characters long and has {} words."
      .format(len(trimmed_paragraph), len(words)))