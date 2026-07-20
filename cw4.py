# Step 1: Create separate lists
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Water", "Juice", "Milk"]

# Step 2: Add a new item to the fruits list
fruits.append("Mango")

# Step 3: Insert a new item at the second position of the vegetables list
vegetables.insert(1, "Onion")

# Step 4: Remove the last item from the beverages list
beverages.pop()

# Step 5: Combine all lists into a nested list
inventory = [fruits, vegetables, beverages]

# Step 6: Print the first two fruits using slicing
print("First two fruits:", fruits[:2])

# Step 7: Access the last vegetable using negative indexing
print("Last vegetable:", vegetables[-1])

# Step 8: Create a list of lengths of all fruit names
fruit_lengths = [len(fruit) for fruit in fruits]
print("Lengths of fruit names:", fruit_lengths)

# Step 9: Check if 'Water' is in the beverages list
print("Is 'Water' in beverages?", "Water" in beverages)

# Step 10: Create a tuple of the first item from each section
first_items = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items)

# Print the complete inventory
print("\nComplete Inventory:")
print(inventory)