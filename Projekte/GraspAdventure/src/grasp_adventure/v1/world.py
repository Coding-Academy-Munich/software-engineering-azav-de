from dataclasses import dataclass

from .location import Location, LocationDescriptions


@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

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
        return cls(locations, initial_location_name)

    def __getitem__(self, location_name: str):
        """Get a location by name."""
        return self.locations[location_name]
