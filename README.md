# profiles-for-skaffold (profs)

## Installation
### Quick setup
Copy and paste:
```bash
(cd /tmp && ([[ -d profs ]] || git clone --depth 1 --config core.autocrlf=false https://github.com/STYLER-Inc/profiles-for-skaffold.git profs) && cd profs && make install) && source ~/.profile
```
### Manual setup
```bash
make install && source ~/.profile
```

## Uninstallation
```bash
make uninstall
```
