# TabRelay — an Alfred workflow

<p align="center"><img src="assets/icon.png" width="120" alt="TabRelay icon"></p>

**Hand the page you're reading to your Muse agent.**

Pass the page you are reading in **Brave** to **Muse** (the Mac app) in two keystrokes.

Type `mc` in Alfred, and the current Brave tab appears as a result. Press Enter, and a ready-to-send prompt — the page title and URL — is copied to your clipboard and Muse's Quick Chat opens. Paste (⌘V), send, done.

A Japanese version is included as `TabRelay-JA.alfredworkflow`; the English one is `TabRelay-EN.alfredworkflow`. Install only one of them (both use the keyword `mc`).

日本語の説明は [README.ja.md](README.ja.md) をご覧ください。

## Requirements

- macOS
- Alfred 4 or 5 with the Powerpack (required for workflows)
- Brave Browser
- Muse for Mac, with Quick Chat on its default shortcut (Option+Space)

## Preview

![TabRelay in Alfred](assets/preview-alfred.png)

Type `mc` in Alfred and the current Brave tab (title + URL) is ready to pass to Muse.

## Install

1. Download `TabRelay-EN.alfredworkflow` (or the JA file) from this repository's `dist/` folder or from Releases.
2. Double-click the file. Alfred imports the workflow.
3. Open a page in Brave, launch Alfred, type `mc`, press Enter.

## Permissions

- **Automation**: the first run asks whether Alfred may control Brave Browser. Allow it — the workflow reads the active tab's title and URL via AppleScript.
- **Accessibility** (optional): used to open Quick Chat automatically with an Option+Space keystroke. Without it, everything still works; just press Option+Space yourself before pasting.

## What it does / does not do

- Reads **only the active tab's title and URL**. No browsing history, no other tabs.
- Puts plain text on **your clipboard**. Nothing is uploaded anywhere, and nothing is sent to Muse automatically — you paste and send it yourself.
- It does **not** extract the article body. If you need full-text clipping, a tool such as Obsidian Web Clipper is the better fit; this workflow is the lightweight "take a look at this page" path.

## How it works

A small zsh script (`src/tabrelay`) talks to Brave via AppleScript. In the distributed workflows the script is embedded directly into the workflow, so there are no other files to install. Run `./build.py` to regenerate the packages in `dist/` from `src/`.

## License

MIT — see [LICENSE](LICENSE).
