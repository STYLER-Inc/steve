# profiles-for-skaffold (steve)

## Installation
### Quick setup
Copy and paste:
```bash
(cd /tmp && ([[ -d steve ]] || git clone --depth 1 --config core.autocrlf=false https://github.com/STYLER-Inc/profiles-for-skaffold.git steve) && cd steve && make install) && source ~/.profile
```
### Manual setup
```bash
make install && source ~/.profile
```

## Uninstallation
```bash
make uninstall
```
