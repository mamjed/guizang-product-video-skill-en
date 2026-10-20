# Dependency Installation (read only when items are missing)

First confirm the style and initialize the video directory, then run `check_environment.py --project <video-dir>`. Install Python first if it is not present. The check script uses only the standard library and can run even with missing dependencies, listing what needs to be installed.

## Installation Scope & Verification

| Path | Required environment |
| --- | --- |
| Starter project | Python ≥3.9, Node ≥22, npm, FFmpeg/FFprobe; project-local React, ReactDOM, esbuild, GSAP, Three.js, Playwright and its launchable Chromium |
| Code-original score (optional) | When using scripts like `score-example-cinematic.py` that depend on numpy/scipy/soundfile, install in a venv inside the video project — not into system Python |
| HyperFrames | Corresponding version's official runtime requirements, FFmpeg/FFprobe, launchable Chrome; this skill's audio scripts need Python |
| Other existing frameworks | Keep the framework and lockfile, fill in only what it actually lacks |

Reuse available environments first. The commands below run only for missing items; before installing, check the **current official documentation** at the linked URLs to verify system support, package names, and required versions. Stable lower bounds are for compatibility judgment; new installs should prefer supported versions. Record actual installed versions, lock files, and run results in the project; historical verification dates do not represent future compatibility commitments.

Re-run the check after installation. When the same error persists after installation, first read the error to distinguish permission, system library, network, or version issues, then address the specific cause — avoid repeated downloads. Handle system permissions according to the current execution environment's permission mechanism.

## System Tools

### macOS

When Homebrew is already installed, choose commands for missing items. Use `brew info <formula>` to verify package info before installing:

```sh
brew install ffmpeg
brew install node
brew install python
```

Sources: [FFmpeg](https://formulae.brew.sh/formula/ffmpeg), [Node](https://formulae.brew.sh/formula/node), [Python](https://docs.brew.sh/Homebrew-and-Python). If Node LTS is needed, choose a supported LTS per the [Node download page](https://nodejs.org/en/download) and Homebrew's current formula; keep the existing version if a usable Node is already present. Determine PATH for versioned formulas from the actual `brew --prefix <formula>` and install output.

Without Homebrew, use existing tools or the [official installer](https://docs.brew.sh/Installation). When Homebrew installation is needed, get the current command from official documentation, review the script before executing; do not freeze installer script versions here.

### Debian / Ubuntu

```sh
sudo apt-get update
sudo apt-get install -y ffmpeg python3
```

Reduce the package list when only one item is missing. Node can reuse existing nvm:

```sh
nvm install --lts
nvm use --lts
```

When nvm is not installed, get the current versioned script URL from the [nvm official install instructions](https://github.com/nvm-sh/nvm#installing-and-updating), download, review, then execute; use `PROFILE=/dev/null` to avoid modifying shell config, then source the actual `nvm.sh` from the install output. Handle other distributions per their package manager and the [FFmpeg download page](https://ffmpeg.org/download.html).

### Windows / PowerShell

First search and verify the package identity, then install the exact ID actually returned. For example:

```powershell
winget search --name Node.js
winget search --name FFmpeg
winget search --name Python
# Replace package-id with the exact ID verified against search results and official documentation:
winget show --id <package-id> --exact
winget install --id <package-id> --exact
```

Sources: [WinGet search](https://learn.microsoft.com/en-us/windows/package-manager/winget/search), [WinGet install](https://learn.microsoft.com/en-us/windows/package-manager/winget/install), [Python Windows install guide](https://docs.python.org/3/using/windows.html), [FFmpeg official Windows builds](https://ffmpeg.org/download.html). Python package identity/installer follows current official documentation — do not freeze Store IDs. Refresh the session PATH after installation; verify using the actual `python` / `py -3` command.

## Project Dependencies & Browser

In the video project directory: use `npm ci` when package-lock.json exists; use `npm install` for first-time without a lock file. Other managers keep their existing lock files. The starter project's package.json pinned versions are the reproducible baseline; upgrade after testing, do not auto-upgrade for every film.

Browser version follows the project's Playwright; only when the corresponding browser is missing:

```sh
npx playwright install chromium --only-shell
```

This command suits the starter project's default `headless:true`, no-channel-specified export. Remove `--only-shell` when the project needs headed Chromium. On Linux with missing system libraries, use `npx playwright install --with-deps chromium`. Per [Playwright browser docs](https://playwright.dev/docs/browsers), headless shell and full Chromium are separate files — **acceptance is based on actual launch success or failure**. When sandbox/permissions cause launch failure, fix execution permissions; re-downloading the browser will not fix it.

The starter project's export script includes `--use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist` so Three.js/WebGL uses software rendering in headless mode; the environment check launches the browser with the same flags.

## HyperFrames

Reuse existing version. When a new project needs the CLI, first check the [official CLI docs](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/references/doctor-browser.md) and current `--help`, then execute:

```sh
npm install --save-dev --save-exact hyperframes
npx hyperframes doctor --json
# Only when Chrome is missing:
npx hyperframes browser ensure
```

Lock the actually installed version. Doctor explains per actual missing items: local rendering needs Node, FFmpeg, FFprobe, Chrome; unselected TTS, Whisper, MusicGen, Docker do not constitute mandatory dependencies. When the doctor schema changes, update the check adapter instead of repeatedly installing software that already exists. Only handle Docker dependencies when actually using Docker rendering. Install framework CLI and other skills separately, choosing based on actual task needs.

## Re-check

```sh
python3 <skill-dir>/scripts/check_environment.py --project <video-dir> --engine browser --force
```

For HyperFrames, use `--engine hyperframes`. On success, continue with the original shot list work; only re-read the corresponding section when items are missing. Platform installation syntax comes from the official sources above; actual machine coverage is based on verification records.
