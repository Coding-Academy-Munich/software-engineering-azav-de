simple_locations = [
    {
        "name": "Room 1",
        "description": "A small room",
        "connections": {"north": "Room 2"},
    },
    {
        "name": "Room 2",
        "description": "A large room",
        "connections": {"south": "Room 1"},
    },
]

dungeon_locations = [
    {
        "name": "Vestibule",
        "description": "You are in a dimly lit room with a high ceiling",
        "connections": {"north": "Entrance Hall"},
    },
    {
        "name": "Entrance Hall",
        "description": (
            "You find yourself in the entrance to the dungeon. "
            "It is a large room with a polished marble floor"
        ),
        "connections": {
            "west": "Dark Corridor",
            "east": "Brightly Lit Corridor",
            "south": "Vestibule",
        },
    },
    {
        "name": "Dark Corridor",
        "description": "You enter a dark and gloomy corridor",
        "connections": {"west": "Treasure Chamber", "east": "Entrance Hall"},
    },
    {
        "name": "Brightly Lit Corridor",
        "description": "You find yourself in a brightly lit corridor",
        "connections": {"west": "Entrance Hall"},
        "objects": ["Torch"],
    },
    {
        "name": "Treasure Chamber",
        "description": (
            "Invaluable treasures from a long-forgotten era are scattered "
            "around the large, richly decorated chamber."
        ),
        "connections": {"east": "Dark Corridor"},
        "objects": ["Treasure Chest"],
    },
]
