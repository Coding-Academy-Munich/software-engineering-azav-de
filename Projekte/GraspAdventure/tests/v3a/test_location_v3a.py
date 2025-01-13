from grasp_adventure.v3a.location import Location
from grasp_adventure.v3a.world_factory import WorldFactory
from grasp_adventure.data.locations import simple_locations


def test_from_description():
    location = Location.from_description(
        {"name": "Room 1", "description": "A small room"}
    )
    assert location.name == "Room 1"
    assert location.description == "A small room"


def test_connections():
    world = WorldFactory.create(simple_locations)
    room1 = world["Room 1"]
    room2 = world["Room 2"]

    assert room1["north"] == room2
    assert room2["south"] == room1
