# Create an empty inventory list
inventory = []

# Function to add an item
def add_item(item):
    inventory.append(item)

# Recursive function to count items
def count_items(items):
    if not items:      # Base case
        return 0
    return 1 + count_items(items[1:])   # Recursive step

# Main function
def main():
    # Add items
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    # Lambda function to display items
    show_item = lambda item: print(f"Item in Stock: {item}")

    # Display all items
    print("Pet Store Inventory:")
    for item in inventory:
        show_item(item)

    # Count and display total items
    total = count_items(inventory)
    print(f"\nTotal Number of Items: {total}")

# Run the program
main()