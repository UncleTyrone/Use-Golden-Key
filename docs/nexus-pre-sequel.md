[b][size=6]Use Golden Key[/size][/b]

[b][size=5]Summary[/size][/b]
Using a golden chest spends one golden key and opens the chest. The game does not ask if you are sure. Other yes or no questions stay as they are.

This is the 1.0.0 package. It is the same file used for Borderlands 2. The skip works the same way in both games.

[url=https://github.com/UncleTyrone/Use-Golden-Key]Source, changelog, and the file hash are on GitHub[/url]

[b][size=5]Requirements[/size][/b]
[list]
[*][url=https://github.com/bl-sdk/willow2-mod-manager/releases/tag/v3.8]Willow2 Mod Manager v3.8 (Slammer)[/url]. PythonSDK is required.[/*]
[/list]

[b][size=5]What's new in 1.0.0[/size][/b]
[list]
[*]The golden chest spends a key and opens. The confirmation is not shown.[/*]
[*]Skip the key question starts on. Turn it off if you want the question back.[/*]
[*]A player without the mod still gets the question.[/*]
[/list]

[b][size=5]Installation[/size][/b]
[list=1]
[*]Install Willow2 v3.8 first.[/*]
[*]Copy [b]Use_Golden_Key.sdkmod[/b] into [b]Borderlands The Pre-Sequel/sdk_mods[/b].[/*]
[*]Do not copy the .sha256 file or the manifest into that folder.[/*]
[*]Enable Use Golden Key.[/*]
[*]Restart the game.[/*]
[/list]

[b][size=5]How it plays[/size][/b]
Use the golden chest. One key is spent and the chest opens. Quit, delete, and every other yes or no are unchanged. If the spend cannot go through, the question still shows.

In co-op, each player who wants the skip installs this file. It spends that player's own key, including when they joined someone else.
