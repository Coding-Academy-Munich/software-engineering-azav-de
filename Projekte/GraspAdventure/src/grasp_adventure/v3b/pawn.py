from dataclasses import dataclass
from enum import Enum

from .location import Location


class Action(str, Enum):
    MOVE = "move"
    SKIP_TURN = "skip_turn"


@dataclass
class Pawn:
    name: str
    location: Location

    def perform_action(self, action: Action, **kwargs):
        if action == Action.MOVE:
            new_location = self.location[kwargs["direction"]]
            if new_location:
                self.location = new_location
            else:
                print(
                    f"{self.name!r}: Cannot move in direction {kwargs['direction']!r}."
                )
        elif action == Action.SKIP_TURN:
            print(f"{self.name!r} skips turn.")
        else:
            print(f"Unknown action: {action!r}")
