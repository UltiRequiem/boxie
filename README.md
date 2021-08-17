# boxie

[![Mit License Icon](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/UltiRequiem/boxie/blob/main/LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Total Lines](https://img.shields.io/tokei/lines/github.com/UltiRequiem/boxie?color=blue&label=Total%20Lines)](https://github.com/UltiRequiem/boxie)
![CodeQL](https://github.com/UltiRequiem/boxie/workflows/CodeQL/badge.svg)
![Pylint](https://github.com/UltiRequiem/boxie/workflows/Pylint/badge.svg)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/boxie?style=flat-square&label=Repo)
[![PyPi Version](https://img.shields.io/pypi/v/boxie)](https://pypi.org/project/boxie)
[![Total Downloads](https://pepy.tech/badge/boxie)](https://pepy.tech/project/boxie)

A command line utility to put text in a box.

## Installation

```bash
pip install boxie
```

To get the last version:

```bash
pip install git+https:/github.com/UltiRequiem/boxie
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
from boxie import boxier

boxier("Hello World")
```

### Screenshot

![Screenshot](https://raw.githubusercontent.com/UltiRequiem/boxie/main/assets/new_screenshot.png)

### LICENSE

This project is licensed under the [MIT](https://github.com/UltiRequiem/boxie/blob/main/LICENSE) License.
