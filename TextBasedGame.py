
# Haley Candia Perez

# Create instructions
def show_instructions():
    print("Cat-tastrophe - A Text-Based Adventure Game!")
    print("*****************************************")
    print("Try to collect all of the items before encountering the evil dog!")
    print("Commands to move: go North, go South, go East, go West")
    print("Command to add items to your Inventory: get [item name]")


# Function to show player's status
def show_status(current_room, inventory, item_in_room):
    print(f"You are currently in the {current_room}")
    print(f"Your current Inventory: {inventory}")
    if item_in_room:
        print(f"You find a {item_in_room}")
    print("**********************")


def main():

    # Dictionary of all the rooms and their directions, items, or the villain
    rooms = {
        'Cat Headquarters': {'South': 'Toy Room', 'North': 'Kitchen', 'West': 'Litterbox', 'East': 'Catnip Room'},
        'Kitchen': {'South': 'Cat Headquarters', 'East': 'Bedroom', 'item': 'Treat'},
        'Bedroom': {'West': 'Kitchen', "villain": True},
        'Litterbox': {'East': 'Cat Headquarters', 'South': 'Dungeon', 'item': 'Sword'},
        'Dungeon': {'North': 'Litterbox', 'item': 'Handcuffs'},
        'Catnip Room': {'South': 'Party Room', 'West': 'Cat Headquarters', 'item': 'Catnip'},
        'Party Room': {'North': 'Catnip Room', 'item': 'Mask'},
        'Toy Room': {'North': 'Cat Headquarters', 'item': 'Squeaky Toy'}
    }
    # Current room
    current_room = 'Cat Headquarters'
    # Create empty inventory
    inventory = []
    # Items needed to win
    win_condition = 6  # Number of items to win

    # Display instructions
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms[current_room].get('item'))

        # Have user input command
        command = input('What would you like to do? (go <direction> or get <item>): ').lower().split()
        # If command is less than 2 print invalid command
        if len(command) < 2:
            print('Invalid command. Please try again')
            continue
        # If user wants to move to a different room by typing go <North, South, East, West>
        if command[0] == 'go':
            direction = ' '.join(command[1:]).title()
            # Check if direction is valid
            if direction in rooms[current_room]:
                # Move the player to the new room, unless direction is invalid then print they can't go there
                current_room = rooms[current_room][direction]
            else:
                print("You can't go in that direction")

        # If user wants to get an item, get item and add to inventory list
        elif command[0] == 'get':
            item_name = ' '.join(command[1:])
            item_in_room = rooms[current_room].get('item')
            if item_in_room:
                if item_name.lower() == item_in_room.lower():
                    print(f'You picked up the {item_name}.')
                    inventory.append(item_name)
                    rooms[current_room].pop('item')
                    win_condition -= 1
                else:
                    # If item invalid print there's no item
                    print("There's no item like this in this room.")
            else:
                # If no item in room, print no item to pick up
                print('There are no items to pick up in this room.')
        # If command is anything else, print invalid command and try again
        else:
            print("Invalid command. Please try again.")

        # If player collects all items, player wins and loop breaks, end game
        if win_condition == 0:
            print('Congratulations! You have collected all of the items and won the game!')
            break
        # If player encounters villain, player loses and loop breaks, end game
        if 'villain' in rooms[current_room]:
            print("Oh no, you have found the dog without collecting all the items! You lose!")
            break


main()
