def create_shopping_list():
    shopping_list = []  # Create an empty list to store shopping items
    print("Enter items for your shopping list. Type 'done' when finished.")

    while True:  # Infinite loop to keep asking for items
        item = input("Add item: ")  # Get user input for an item
        if item.lower() == 'done':
            break  # Exit the loop if the user types 'done'
        elif item.lower() == 'remove':
            if shopping_list:  # Check if the list is not empty
                print_shopping_list(shopping_list)  # Print current list before removal
                removed_item = input("Enter the item to remove: ")
                if removed_item in shopping_list:
                    shopping_list.remove(removed_item)
                    print(f"{removed_item} removed from the list.")
                else:
                    print(f"{removed_item} not found in the list.")
            else:
                print("The shopping list is empty.")
        else:
            shopping_list.append(item)  # Add the item to the list

    return shopping_list  # Return the complete list

def print_shopping_list(shopping_list):
    """Print the shopping list in a formatted way."""
    if shopping_list:
        print("Your Shopping List:")
        for i in range(len(shopping_list)):
            print(f"{i+1}. {shopping_list[i]}")
    else:
        print("The shopping list is empty.")

# Example usage:
my_shopping_list = create_shopping_list()
print_shopping_list(my_shopping_list)
