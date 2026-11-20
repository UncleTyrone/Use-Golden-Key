# Use Golden Key 1.0.0

Using a golden chest spends one golden key and opens the chest. The game does not ask if you are sure. It runs in Borderlands 2 and in Borderlands: The Pre-Sequel. Other yes or no questions stay as they are.

PythonSDK is required. Install [Willow2 Mod Manager v3.8, Slammer](https://github.com/bl-sdk/willow2-mod-manager/releases/tag/v3.8) first.

Copy `dist/Use_Golden_Key.sdkmod` into each game's `sdk_mods` folder and restart. Leave the `.sha256` file and the manifest in `dist`. Enable **Use Golden Key**. **Skip the key question** starts on. Turn it off if you want the question back.

The same file goes in both games. A player who does not have it still gets the question. A player who has it spends their own key without the question, including when they joined someone else.

The package that builds is `src/Use_Golden_Key`.

```text
python scripts/build_sdkmod.py
```

## Pages

- [Play](docs/play.md) covers install, the option, and co-op.
- [API](docs/api.md) covers the hook, the games, and what the package sends.
- [Development](docs/development.md) covers the tree, the build, and how a release goes out.

Nexus paste text: [Borderlands 2](docs/nexus-borderlands-2.md) and [The Pre-Sequel](docs/nexus-pre-sequel.md).

[Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [License](LICENSE)
