# Initial Grocery List
grocery_list = ["milk", "bread", "eggs"]

# Function to add an item
def add_item(item):
    grocery_list.append(item)

# Function to remove the last item
def remove_last_item():
    if grocery_list:
        grocery_list.pop()
    else:
        print("The grocery list is empty.")

# Lambda function to display each item
display_items = lambda: [print(f"Item: {item}") for item in grocery_list]

# Recursive function to count total characters
def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

# Example Usage
print("Initial Grocery List:")
display_items()

# Add an item
add_item("butter")
print("\nAfter adding an item:")
display_items()

# Remove the last item
remove_last_item()
print("\nAfter removing the last item:")
display_items()

# Total characters in all item names
print("\nTotal characters:", count_characters(grocery_list))