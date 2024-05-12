# Project 2 "Compute Differences of files"

**Part of Python Developer Profession on Hexlet**
https://hexlet.io/programs/python

**Official project description**
https://ru.hexlet.io/programs/python/projects/50


## About tool

CLI utility for comparing difference of two files and format diff.
Publishing only locally (not in PyPI).
Usage as package and module as well.

---

### Hexlet tests and linter status:
[![Hexlet-check](https://github.com/ivekhov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/ivekhov/python-project-lvl2/actions)

<!-- ![Python CI](https://github.com/ivekhov/python-project-lvl2/workflows/Python%20CI/badge.svg) -->


### GitHub Actions

[![Actions Status](https://github.com/ivekhov/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ivekhov/python-project-lvl2/actions)

### CodeClimate: Code Coverage

[![Maintainability](https://api.codeclimate.com/v1/badges/f9b0debda75ad31a2506/maintainability)](https://codeclimate.com/github/ivekhov/frontend-project-46/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/f9b0debda75ad31a2506/test_coverage)](https://codeclimate.com/github/ivekhov/frontend-project-46/test_coverage)


---
## How it works 
Asciinema: 

[![asciicast](https://asciinema.org/a/5J9otro3SrQMvT04IRO0pcQAE.svg)](https://asciinema.org/a/5J9otro3SrQMvT04IRO0pcQAE)


Reminder on asciinema usage:
```bash
# install asciinema
$ brew install asciinema

# record asciinedma in terminal
$ asciinema rec
```

## Setup local

```bash
$ git clone git@github.com:ivekhov/python-project-lvl2.git

$ make install
```

## Help
```bash
$ gendiff -h
```


## Usage  as CLI utility

```bash

$ gendiff -h

$ gendiff file_before.json file_after.json

$ gendiff -f plain file_before.json file_after.json

$ gendiff -f stylish file_before.yml file_after.yml

$ gendiff -f stylish file_extended_before.json file_extended_after.json
```

## Usage inside python as package
```python
from gendiff import generate_diff

generate_diff('file_before.json', 'file_before.json', formatter='stylish')
```

## Run tests

```bash
make test
```

## Development

Once when developing:

```bash
# add in pyproject.toml
packages = [
    {include = "gendiff"},
]
...
[tool.poetry.scripts]
gendiff = 'gendiff.scripts.gendiff:main'

# in __init__.py inside gendiff directory add: 
__all__ = ['generate_diff']
from .generate_diff import generate_diff

```

After changing code:

```bash
# in one command 3 checks: test lint selfcheck
$ make check

# tests: basic and extended
$ make test

# linter validation
$ make lint

# building a package
$ make build
```

----
