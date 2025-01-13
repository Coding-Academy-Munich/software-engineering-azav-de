from collections.abc import Mapping
from typing import Any, Optional

from .game import Game
from .location import Location, LocationDescriptions
from .pawn import Pawn
from .player import Player
from .world import World


class GameFactory:
    def __init__(
        self, object_descriptions: dict[str, Any] | None = None, object_classes=None
    ):
        self.object_descriptions: dict[str, Any] = (
            {} if object_descriptions is None else object_descriptions
        )
        self.object_classes: dict[str, type] = (
            {} if object_classes is None else object_classes
        )
        self.objects = {}
        self.world: World | None = None
        self.players = {}

    def create_game(
        self, location_descriptions: LocationDescriptions, player_descriptions
    ) -> Game:
        world = self.create_world(location_descriptions)
        players = self.create_players(player_descriptions)
        return Game(players=players, world=world)

    def create_players(self, player_descriptions) -> list[Player]:
        return [self.create_player(desc) for desc in player_descriptions]

    def create_player(self, player_description) -> Player:
        assert self.world is not None
        if not isinstance(player_description, Mapping):
            player_description = {"name": player_description}
        player_name = player_description["name"]
        if self.players.get(player_name) is None:
            location_name = player_description.get("location")
            if location_name is None:
                location_name = self.world.initial_location_name
            self.players[player_name] = Player(
                name=player_description["name"],
                pawn=Pawn(location=self.world[location_name]),
            )
        return self.players[player_name]

    def create_world(
        self,
        location_descriptions: LocationDescriptions,
    ) -> World:
        """Create a World from a description of its locations."""
        if self.world is None:
            locations = GameFactory._create_locations(location_descriptions)
            self.world = World(
                locations=locations,
                initial_location_name=location_descriptions[0]["name"],
            )
            return self.world
        else:
            raise ValueError("The world has already been created.")

    @staticmethod
    def _create_locations(
        location_descriptions: LocationDescriptions,
    ) -> dict[str, Location]:
        """Create a World from a description of its locations."""
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        GameFactory._build_connections_for_all_locations(
            locations, location_descriptions
        )
        return locations

    @staticmethod
    def _build_connections_for_all_locations(
        locations: dict[str, Location], location_descriptions: LocationDescriptions
    ):
        for location_description in location_descriptions:
            connections = {
                direction: locations[name]
                for direction, name in location_description.get(
                    "connections", {}
                ).items()
            }
            locations[location_description["name"]].connections = connections
