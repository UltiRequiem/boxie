# boxie

[![Mit License Icon](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/UltiRequiem/boxie/blob/main/LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Total Lines](https://img.shields.io/tokei/lines/github.com/UltiRequiem/boxie?color=blue&label=Total%20Lines)](https://github.com/UltiRequiem/boxie)
[![PyPi Version](https://img.shields.io/pypi/v/boxie)](https://pypi.org/project/boxie)
[![Total Downloads](https://pepy.tech/badge/boxie)](https://pepy.tech/project/boxie)

A command line utility to put text in a box.

## Installation

```bash
pip install boxie
```

If you are on Linux you may need to use sudo to access this globally.

## Usage

```bash
boxie "Hello World"
```

Or...

```bash
python -m boxie "Hello World"
```

Or in your code:

```python
from boxie import box_borders

@box_borders
def print_console(txt):
    print(txt)

print_console("Hello World")
```

Check [test.py](./test.py)

### Screenshot

![Screenshot](https://raw.githubusercontent.com/UltiRequiem/boxie/main/assets/screenshot.png)

### LICENSE

[MIT](https://github.com/UltiRequiem/boxie/blob/main/LICENSE)
