from distutils.core import setup
from boxie import __version__, __author__, __author_email__, __url__

from os import path

with open(
    path.join(path.abspath(path.dirname(__file__)), "README.rst"), encoding="utf-8"
) as readme_file:
    long_description = readme_file.read()

setup(
    name="boxie",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    long_description=long_description,
    include_package_data=True,
    license="MIT",
    scripts=["./bin/boxie"],
    packages=["boxie"],
)
