from grasp_adventure.v1.location import Location


def test_from_description():
    location = Location.from_description(
        {"name": "Room 1", "description": "A small room"}
    )
    assert location.name == "Room 1"
    assert location.description == "A small room"
