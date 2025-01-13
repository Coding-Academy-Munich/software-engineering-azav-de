from grasp_adventure.v4.actions import MoveAction, SkipTurnAction
from fixtures_v4 import *  # noqa


def test_player_location(player, level):
    assert player.location == level["Room 1"]


def test_actions(player, level):
    actions = player.actions

    assert actions == [MoveAction("north", level["Room 2"]), SkipTurnAction()]


def test_select_action(player, level):
    assert player.select_action(player) == MoveAction("north", level["Room 2"])


def test_perform_move_action(player, level):
    action = MoveAction(direction="north", target=level["Room 2"])
    action.execute(player)
    assert player.location == level["Room 2"]


def test_perform_wait_action(player, level):
    action = SkipTurnAction()
    action.execute(player)
    assert player.location == level["Room 1"]


def test_take_turn(player, level):
    player.take_turn()
    assert player.location == level["Room 2"]
