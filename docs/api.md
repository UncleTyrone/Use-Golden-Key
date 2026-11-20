[← Home](../README.md)

# API

Package `Use_Golden_Key` version 1.0.0, loaded from `src/Use_Golden_Key`. `__version__` is `1.0.0`. Author is UncleTyrone.

`build_mod` is what the mod manager calls. The only option is **Skip the key question**. It starts on. Off leaves the game's question in place.

## The hook

`WillowGame.WillowPlayerController:ClientShowGoldenKeyUseConfirmationDialog` is hooked on `Type.PRE`. Borderlands 2 and The Pre-Sequel both ask with that function. Yes on that box calls `ServerUseWithoutConfirmation`, which is what spends the key and opens the chest.

When the option is on, the hook calls `ServerUseWithoutConfirmation` on the player controller and returns `Block`, so the box is not shown. If that call raises, the hook returns nothing and the box still shows. When the option is off, the hook returns nothing and the game asks as usual.

Quit, delete, and every other confirmation dialog are not hooked.

## Games and co-op

`supported_games` is Borderlands 2 and The Pre-Sequel when those `Game` values import. `coop_support` is `ClientSide` when that value imports. The skip runs on the player who used the chest. It does not answer the question for anyone else. If those enums are missing, the mod still builds without them.

The short note inside the sdkmod is `src/Use_Golden_Key/README.md`. The home page for this repository is the root `README.md`.
