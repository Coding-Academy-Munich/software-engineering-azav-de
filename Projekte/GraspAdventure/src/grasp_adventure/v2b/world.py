from dataclasses import dataclass

from .location import Location, LocationDescriptions


@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

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
        _build_connections_for_all_locations(locations, location_descriptions)
        return cls(locations, initial_location_name)


def _build_connections_for_all_locations(
    locations: dict[str, Location], location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: locations[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        locations[location_description["name"]].connections = connections
