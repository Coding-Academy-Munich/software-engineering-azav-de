import pytest

from grasp_adventure.v1.world import World
from grasp_adventure.data.locations import simple_locations


def test_from_location_descriptions():
    world = World.from_location_descriptions(simple_locations)

    assert world.initial_location_name == "Room 1"

    assert world["Room 1"].name == "Room 1"
    assert world["Room 1"].description == "A small room"
    assert world["Room 2"].name == "Room 2"
    assert world["Room 2"].description == "A large room"


# Superfluous, since the test_from_location_descriptions() test already covers this
def test_getitem():
    world = World.from_location_descriptions(simple_locations)

    assert world["Room 1"].name == "Room 1"
    assert world["Room 1"].description == "A small room"
    assert world["Room 2"].name == "Room 2"
    assert world["Room 2"].description == "A large room"


def test_getitem_raises_key_error():
    world = World.from_location_descriptions(simple_locations)

    with pytest.raises(KeyError):
        world["Room 3"]  # noqa
