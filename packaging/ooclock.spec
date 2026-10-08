Name:           ooclock
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign TUI matrix clock, stopwatch, and pomodoro timer
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooclock
Source0:        ooclock-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooclock is a sovereign, capability-bounded TUI matrix clock, stopwatch, and
pomodoro timer written in pure openOODA, featuring circadian lighting, mascot
moods, theme support via oote palettes, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooclock
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooclock-uninstall

%files
/usr/bin/ooclock
/usr/bin/ooclock-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign release v0.2.0: clock_now tool, pomodoro argument parsing, and MCP elevation
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign release: matrix digits, circadian mood, pomodoro, and MCP surface
