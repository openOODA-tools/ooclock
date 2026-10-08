# ooclock

> **Sovereign TUI matrix clock, stopwatch, and pomodoro timer for the openOODA era.**  
> *A drop-in digital terminal clock written in pure openOODA, featuring negative-trust capability security, big block matrix digits, dynamic circadian mascot moods, Pomodoro timers, and a first-class Model Context Protocol (MCP) surface.*

Part of [openOODA-tools](https://github.com/openOODA-tools).

---

## 1. Installation

`ooclock` has zero runtime dependencies. It compiles to a standalone native binary linked directly with libc.

### Universal Web Installer
Installs the standalone native binary to `/usr/local/bin` (or `~/.local/bin`):

```bash
curl -fsSL https://openooda-tools.github.io/ooclock/install.sh | bash
```

### Debian / Ubuntu (APT)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/ooclock/install.sh | bash -s -- --apt

# Or manual package install
sudo dpkg -i ooclock_0.2.0-1_amd64.deb
```

### Fedora / RHEL / CentOS (DNF)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/ooclock/install.sh | bash -s -- --dnf

# Or manual RPM install
sudo dnf install ./ooclock-0.2.0-1.fc44.x86_64.rpm
```

### Arch Linux (PKGBUILD)
```bash
# Automated via installer
curl -fsSL https://openooda-tools.github.io/ooclock/install.sh | bash -s -- --arch

# Or manual build via packaging/PKGBUILD
cd packaging && makepkg -si
```

### Clean Uninstaller
To cleanly remove `ooclock` and any installed package manager entries:

```bash
# Automated via standalone uninstaller
curl -fsSL https://openooda-tools.github.io/ooclock/uninstall.sh | bash

# Or via installer flag
curl -fsSL https://openooda-tools.github.io/ooclock/install.sh | bash -s -- --uninstall

# Or preview removal without making changes (dry-run)
curl -fsSL https://openooda-tools.github.io/ooclock/uninstall.sh | bash -s -- --dry-run
```

---

## 2. Usage & Features

### Big Block Matrix Clock
Display digital clock with dynamic circadian mascot moods:

```bash
# Run clock snapshot
ooclock -1

# Start Pomodoro focus session (25 minutes)
ooclock -p 25

# Launch Stopwatch timer
ooclock -s

# Adjust timezone offset from UTC (e.g. -10 for Hawaii-Aleutian)
ooclock --tz=-10
```

### Circadian Mascot Moods & Lighting
The mascot emote and inspirational quote dynamically cycle throughout the 24-hour cycle:
- **Dawn / Morning** (`5:00` - `11:59`): `( ＾◡＾)っ♨` Sunrise Amber
- **Daylight / Afternoon** (`12:00` - `17:59`): `(⌐■_■)⚡` Deep Work Cyan
- **Twilight / Evening** (`18:00` - `21:59`): `(✿◠‿◠)✨` Twilight Violet
- **Starlight / Night** (`22:00` - `4:59`): `( ᴗ_ ᴗ。) zZ` Late Night Indigo

### Model Context Protocol (MCP) Mode
`ooclock` speaks JSON-RPC 2.0 MCP over stdio for LLM coding agents:

```bash
ooclock --mcp
```

#### MCP Tools Provided:
- `get_time`: Get current ISO time, circadian phase, and mascot mood.
  - Parameters: None
- `pomodoro_status`: Calculate pomodoro cycle metrics and graphical progress bars.
  - Parameters: `work_mins` (integer), `elapsed_secs` (integer)

---

## 3. Capability Security & Verification

`ooclock` enforces strict Object Capability Discipline (OCap):
- **FsReadCap**: Strictly bounded read-only access to system themes and locale configs.
- **TimeCap**: Monotonic and epoch clock measurement via `chrono_now_ms`.
- **Zero Ambient Authority**: Zero child processes, zero network sockets, zero unprompted disk writes.