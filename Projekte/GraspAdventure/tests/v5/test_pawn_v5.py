from grasp_adventure.v5.actions import MoveAction, SkipTurnAction
from fixtures_v5 import *  # noqa


def test_actions(pawn, level):
    actions = pawn.actions

    assert actions == [MoveAction("north", level["Room 2"])]
