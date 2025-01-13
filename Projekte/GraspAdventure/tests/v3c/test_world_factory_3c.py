from grasp_adventure.v3c.world_factory import WorldFactory
from grasp_adventure.data.locations import simple_locations


def test_create():
    world = WorldFactory.create(simple_locations)

    assert world.initial_location_name == "Room 1"
    assert world["Room 1"].name == "Room 1"
    assert world["Room 1"].description == "A small room"
    assert world["Room 2"].name == "Room 2"
    assert world["Room 2"].description == "A large room"
