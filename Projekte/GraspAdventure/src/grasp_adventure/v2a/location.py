from dataclasses import dataclass
from typing import Any, Mapping, Sequence

LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
    description: str = ""

    @classmethod
    def from_description(cls, data: LocationDescription) -> "Location":
        return cls(data["name"], data.get("description", ""))
