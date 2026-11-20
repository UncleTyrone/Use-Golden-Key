"""Use Golden Key: the golden chest spends the key without asking.

Borderlands 2 and The Pre-Sequel both ask with the same controller function,
ClientShowGoldenKeyUseConfirmationDialog. Yes on that box calls
ServerUseWithoutConfirmation, which is what actually opens the chest. This mod
calls that itself and does not show the box. Quit, delete, and every other
yes or no stay as they are.
"""

from __future__ import annotations

from typing import Any

from mods_base import BoolOption, build_mod, hook
from unrealsdk.hooks import Block, Type
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct

__version__ = "1.0.0"
__author__ = "UncleTyrone"

skip_option = BoolOption(
    "Skip the key question",
    True,
    "On",
    "Off",
    description="On: using the golden chest spends a key and opens it. Off: the game still asks.",
)


@hook(
    "WillowGame.WillowPlayerController:ClientShowGoldenKeyUseConfirmationDialog",
    Type.PRE,
)
def _use_the_key(
    obj: UObject,
    _args: WrappedStruct,
    _ret: Any,
    _func: BoundFunction,
) -> type[Block] | None:
    if not skip_option.value:
        return None
    try:
        obj.ServerUseWithoutConfirmation()
    except Exception:  # noqa: BLE001
        return None
    return Block


_build_kwargs: dict[str, Any] = dict(
    name="Use Golden Key",
    author=__author__,
    version=__version__,
    description=(
        "Using the golden chest spends a key and opens it. "
        "The yes or no question is not shown. "
        "Borderlands 2 and The Pre-Sequel."
    ),
    options=[skip_option],
    hooks=[_use_the_key],
)

try:
    from mods_base import Game

    _selected = []
    for _name in ("BL2", "TPS"):
        _game = getattr(Game, _name, None)
        if _game is not None:
            _selected.append(_game)
    if _selected:
        _build_kwargs["supported_games"] = _selected
except Exception:  # noqa: BLE001
    pass

try:
    from mods_base import CoopSupport

    _coop = getattr(CoopSupport, "ClientSide", None)
    if _coop is not None:
        _build_kwargs["coop_support"] = _coop
except Exception:  # noqa: BLE001
    pass

mod = build_mod(**_build_kwargs)
