# profiles-for-skaffold (profs)

## Installation
Quick setup:
```bash
(cd /tmp && ([[ -d sprofs ]] || git clone --depth 1 --config core.autocrlf=false https://github.com/STYLER-Inc/profiles-for-skaffold.git) && cd sprofs && make install) && source ~/.profile
```
If you already have the source:
```bash
make install
```

## Uninstallation
```bash
make uninstall
```
