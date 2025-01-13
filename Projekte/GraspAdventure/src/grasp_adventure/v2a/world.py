from dataclasses import dataclass, field

from .location import Location, LocationDescriptions


@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str
    connections: dict[str, dict[str, Location]] = field(default_factory=dict)

    def __getitem__(self, location_name: str):
        """Get a location by name."""
        return self.locations[location_name]

    @classmethod
    def from_location_descriptions(
        cls, location_descriptions: LocationDescriptions
    ) -> "World":
        """Create a World from a description of its locations."""
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        initial_location_name = location_descriptions[0]["name"]
        result = cls(locations, initial_location_name)
        _build_connections_for_all_locations(result, location_descriptions)
        return result

    def connection(self, location: Location, direction: str) -> Location | None:
        """Return the connected location in a given direction, or `None`."""
        return self.connections[location.name].get(direction)


def _build_connections_for_all_locations(world, location_descriptions):
    for ld in location_descriptions:
        world.connections[ld["name"]] = {
            direction: world[loc_name]
            for direction, loc_name in ld.get("connections", {}).items()
        }
