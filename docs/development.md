[← Home](../README.md)

# Development

The live tree is `src/Use_Golden_Key`. Version 1.0.0 until this package is replaced.

```text
src/Use_Golden_Key/
  __init__.py       build_mod, the option, the confirmation hook
  pyproject.toml    sdkmod entry point, games, ClientSide
  README.md         the short note packed into the sdkmod
```

`README.md` at the repository root is the only index. Play, API, and development are the three pages under `docs/`. The file inside the package is the note a player sees if they open the sdkmod. It is not a second index.

Willow2 v3.8 is the helper set. This mod uses `mods_base` and `unrealsdk`. It does not use Networking, Keybinds, or UI Utils. Python on this machine for a local check is 3.10 or newer. Do not import the Willow2 zips from a test run. The game's PythonSDK is newer than that.

## Build

From the repository root:

```text
python scripts/build_sdkmod.py
```

The member list is `MEMBERS` in `scripts/build_sdkmod.py`. A new file under the package has to be added there or it will not ship. The zip is stored, not deflated, with a fixed timestamp so the same sources build the same file.

The build writes `dist/Use_Golden_Key.sdkmod`, the `.sha256` sidecar, and `dist/Use_Golden_Key.manifest.json`.

After a build, copy only the sdkmod into both games:

- `D:\SteamLibrary\steamapps\common\Borderlands 2\sdk_mods`
- `D:\SteamLibrary\steamapps\common\BorderlandsPreSequel\sdk_mods`

Leave the hash file and the manifest in `dist`. Leave every other file in those folders alone.

## Releasing

The changelog section for this work is `1.0.0` in `CHANGELOG.md`. Open 1.1.0 or 1.0.1 only after 1.0.0 has actually shipped. Say what the player does, what they get, and which game it is. Both games get the same skip.

When the behavior changes, update `CHANGELOG.md`, `reports/RELEASE_NOTES.md`, and this set of pages in the same turn. After a rebuild, put the new SHA-256 in the release notes. The hash file is the source for that line.

The usual release is: build, copy the sdkmod into both games, commit locally once it has been played and it works. Do not push unless asked. The publisher then tags a GitHub Release and attaches `dist/Use_Golden_Key.sdkmod` and the `.sha256` file. Paste the hash into the release notes.

Nexus paste text for the two game pages is `docs/nexus-borderlands-2.md` and `docs/nexus-pre-sequel.md`.

## Commits

Do not commit while a change is still being tried. After it has been played and it works, one commit. The message says why. The changelog is already in that commit. Do not stack commits titled only with the version number. Do not force-push `main` or `master` unless that was asked for.

`CONTRIBUTING.md`, `SECURITY.md`, and `CHANGELOG.md` stay at the repository root.
