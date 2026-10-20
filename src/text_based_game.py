"""Project Two starter for the student's text-based adventure game."""

# TODO: Add the full-name comment required by Project Two directions.


def show_instructions():
    """Display the game objective and available commands."""
    # TODO: Print instructions that match your game and commands.
    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    pass


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
def show_instructions():
    """Display the game title, objective, and available commands."""
    print("THE ESCAPE: A Historical Horror Adventure")
    print("Collect all 6 items before entering the Grounds Keeper's Room.")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items: get item name")
    print()


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and any room item."""
    print("------------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")

    room_item = rooms[current_room].get("item")
    if room_item:
        print(f"You see: {room_item}")

    print("------------------------------")


def main():
    """Run the game until the player wins or loses."""

    # Room connections and collectible items.

    # The Grounds Keeper's Room is the villain room and has no item.
    rooms = {
        "Parlor": {
            "north": "Library",
            "east": "Master's Room"
        },
        "Library": {
            "south": "Parlor",
            "east": "Study",
            "item": "map"
        },
        "Study": {
            "west": "Library",
            "south": "Dining Room",
            "item": "master's letterhead paper"
        },
        "Dining Room": {
            "north": "Study",
            "west": "Kitchen",
            "east": "Servants' Quarters",
            "item": "money"
        },
        "Kitchen": {
            "east": "Dining Room",
            "item": "gun"
        },
        "Master's Room": {
            "west": "Parlor",
            "south": "Servants' Quarters",
            "item": "master's stamp"
        },
        "Servants' Quarters": {
            "west": "Dining Room",
            "north": "Master's Room",
            "south": "Grounds Keeper's Room",
            "item": "keys"
        },
        "Grounds Keeper's Room": {
            "north": "Servants' Quarters"
        }
    }

    # The player must collect all six items before confronting the villain.

    all_items = {
        "map",
        "master's letterhead paper",
        "money",
        "gun",
        "master's stamp",
        "keys"
    }

    inventory = []
    current_room = "Parlor"

    show_instructions()

    # Keep playing until the player enters the villain room.
    while True:

        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()
        command_parts = command.split()

        if len(command_parts) == 2 and command_parts[0] == "go":
            direction = command_parts[1]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                if current_room == "Grounds Keeper's Room":
                    if set(inventory) == all_items:
                        print("\nYou collected every item and are ready to escape!")
                        print("Congratulations! You outsmarted the Grounds Keeper and escaped!")
                    else:
                        print("\nThe Grounds Keeper catches you before you can escape.")
                        print("GAME OVER!")
                    print("Thanks for playing. Hope you enjoyed the game.")
                    break
            else:
                print("You cannot go that way. Try another direction.")

        elif len(command_parts) >= 2 and command_parts[0] == "get":
            requested_item = " ".join(command_parts[1:])
            room_item = rooms[current_room].get("item")

            if room_item and requested_item == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(f"You collected: {room_item}")

                if set(inventory) == all_items:
                    print("\nYou have collected all six items. Now reach the Grounds Keeper's Room to escape!")
            elif room_item is None:
                print("There is no item to collect in this room.")
            else:
                print(f"You cannot find '{requested_item}' here. Enter the item name shown in the room.")

        else:
            print("Invalid command. Enter 'go north', 'go south', 'go east', 'go west', or 'get item name'.")


if __name__ == "__main__":
    main()

