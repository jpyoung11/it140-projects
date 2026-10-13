"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

# TODO: Run and debug all milestone cases in prototype/README.md.
rooms = {
    'Parlor': {
        'north': 'Masters Room',
        'north': 'Library'
    },
    'Masters Room': {
        'south': 'Parlor',
        'west': 'Servants Quarters',
        'southwest': 'Study'
    },
    'Servants Quarters': {
        'east': 'Masters Room',
        'north': 'Grounds Keepers Room'
    },
    'Grounds Keepers Room': {
        'north': 'Servants Quarters'
    },
    'Library': {
        'south': 'Parlor',
        'north': 'Dining Room'
    },
    'Dining Room': {
        'south': 'Library',
        'west': 'Study'
    },
    'Study': {
        'east': 'Dining Room',
        'northeast': 'Masters Room'
    }
}

# Set the player's starting room.
current_room = 'Parlor'

# Continue the game until the player exits.
while current_room != 'exit':
    # Display the player's current room.
    print(f'\nYou are in the {current_room}.')

    # Ask the player for a command.
    command = input(
        "Enter a direction (north, south, east, west, northeast, southwest) "
        "or 'exit' to quit: "
    ).lower().strip()

    # Exit the game.
    if command == 'exit':
        current_room = 'exit'
        print('Thanks for playing! Goodbye!')

    # Move the player if the direction is valid.
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
        print(f'You moved to the {current_room}.')

    # Handle invalid commands.
    else:
        print('Invalid move. You cannot go that way.')

