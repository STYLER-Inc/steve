# Styler Template Environment Variable Extractor (Steve)

## Installation
### Quick setup (copy + paste)
```bash
(cd /tmp && ([[ -d steve ]] || git clone --depth 1 --config core.autocrlf=false https://github.com/STYLER-Inc/profiles-for-skaffold.git steve) && cd steve && make install) && source ~/.profile
```
### Manual setup
```bash
make install && source ~/.profile
```

## Running tests
### After cloning repository
```bash
(virtualenv -p `which python3` venv && cd src/ && ../venv/bin/pytest tests/*)
```

### After install
```bash
(cd ~/.steve/src ; ../venv/bin/pytest tests/*)
```

## Usage
Run `steve` to see the usage. You can try it out with the test data like this:

Usage:
```bash
steve --help
```

Example:
```bash
steve ~/.steve/src/tests/data/template.yaml ~/.steve/src/tests/data/values.yaml
```

## Uninstallation
```bash
make uninstall
```
