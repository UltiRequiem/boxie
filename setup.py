from distutils.core import setup
from boxie.version import __version__

from os import path

with open(
    path.join(path.abspath(path.dirname(__file__)), "README.rst"), encoding="utf-8"
) as readme_file:
    long_description = readme_file.read()

setup(
    name="boxie",
    version=__version__,
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/boxie",
    long_description=long_description,
    include_package_data=True,
    license="MIT",
    scripts=["./bin/boxie"],
    packages=["boxie"],
)
