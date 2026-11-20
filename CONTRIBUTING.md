[← Home](README.md)

# Contributing

## Before you change the skip

1. Read `docs/development.md` and `docs/api.md`. The live code is `src/Use_Golden_Key`.
2. Hook only `ClientShowGoldenKeyUseConfirmationDialog`. Quit, delete, and every other yes or no stay as they are.
3. If `ServerUseWithoutConfirmation` fails, leave the question up. Do not block the dialog on a failed spend.

## Dev loop

```text
python scripts/build_sdkmod.py
```

## Commits

Do not commit while a change is still being tried. After you have tested it and said it works, the next step is one commit. The message says why the change exists, and `CHANGELOG.md` is already updated in that commit. Do not stack commits that are titled only with the version number. Do not push, and do not force-push `main` or `master`, unless you ask for that.

## Pull requests

- Keep changes focused. Do not mix an unrelated dialog with the golden-key skip.
- Keep gameplay notes in the current `CHANGELOG.md` section. The working version stays **1.0.0** until that package is actually released. Do not open 1.0.1 for pre-release edits.
- Rebuild `dist/Use_Golden_Key.sdkmod` and refresh the `.sha256` sidecar before asking for review.
- Do not force-push `main` / `master`.

## Docs

The player guide is `docs/play.md`. The API notes are `docs/api.md`. The build and release notes are `docs/development.md`. `README.md` is the only index. Each of those pages links back to it.
