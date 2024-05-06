# Project 2 "Compute Differences of files"

Part of Python Developer Profession on Hexlet: 
https://hexlet.io/programs/python

Project description:
https://ru.hexlet.io/programs/python/projects/50


## About

CLI utility for comparing difference of two files and format diff.
Publishing only locally (not in PyPI).
Usage as package and module as well.

---




### Hexlet tests and linter status:
[![Actions Status](https://github.com/ivekhov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ivekhov/python-project-lvl2/actions)


### GitHub Actions

[![Actions Status](https://github.com/ivekhov/frontend-project-46/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ivekhov/frontend-project-46/actions)

### CodeClimate: Code Coverage

[![Maintainability](https://api.codeclimate.com/v1/badges/f9b0debda75ad31a2506/maintainability)](https://codeclimate.com/github/ivekhov/frontend-project-46/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/f9b0debda75ad31a2506/test_coverage)](https://codeclimate.com/github/ivekhov/frontend-project-46/test_coverage)


---
## How it works 
Asciinema: 

[![asciicast](https://asciinema.org/a/##.svg)](https://asciinema.org/a/##)


## Setup local

```bash
make install-local

gendiff -h
```

## Usage example

```python
from hexlet-code import gendiff 
```

## Run tests

```bash
make test

# example of usage
gendiff  __fixtures__/file01.json __fixtures__/file02.json
```

## Development

Once when developing:

```bash
# add in package.json
"bin": {
  "gendiff": "bin/gendiff.py"
}, 

chmod +x bin/gendiff.py
```

After changing code:

```bash
make test

make lint

make install-local

make publish

make gendiff-help
```

----
