from distutils.core import setup
from boxie.version import __version__
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="boxie",
    version=__version__,
    description="Like Figlet but puts the text in a box",
    long_description=README,
    long_description_content_type="text/markdown",
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/boxie",
    license="MIT",
    scripts=["./bin/boxie"],
    packages=["boxie"],
)
