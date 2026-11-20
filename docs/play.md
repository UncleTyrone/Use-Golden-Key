[← Home](../README.md)

# Playing Use Golden Key

Version 1.0.0. One file, `Use_Golden_Key.sdkmod`, runs in Borderlands 2 and in Borderlands: The Pre-Sequel. Using a golden chest spends one golden key and opens the chest. The game does not ask if you are sure.

You need [Willow2 Mod Manager v3.8, Slammer](https://github.com/bl-sdk/willow2-mod-manager/releases/tag/v3.8) in each game. That is the PythonSDK package.

## Install

1. Install Willow2 v3.8 in the game you are playing.
2. Copy `Use_Golden_Key.sdkmod` into that game's `sdk_mods` folder. Leave the `.sha256` file and the manifest wherever you built them. Do not copy those two into the game folder.
3. Enable **Use Golden Key**.
4. Restart the game.

**Skip the key question** starts on. Turn it off in the mod options if you want the question back.

To remove it, disable it in the menu and delete `Use_Golden_Key.sdkmod` from `sdk_mods`.

## What you get

Walk up to a golden chest and use it. One key is spent and the chest opens. The "are you sure you want to spend a golden key?" question is not shown.

Quit, delete, and every other yes or no stay as they are. This only skips the golden-key question.

If the spend cannot go through, the question still shows, so you are not left with a chest that did nothing.

## Playing with other people

The same file goes in both games. Each player who wants the skip installs it. The question is skipped on that player's own chest use, including when they joined someone else. A player who does not have the mod still gets the question. Their keys are not spent by someone else's copy of this mod.
