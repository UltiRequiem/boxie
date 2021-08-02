from distutils.core import setup
from boxie.version import __version__

setup(
    name="boxie",
    version=__version__,
    description="Like Figlet but puts the text in a box",
    long_description=open("README.md").read(),
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/boxie",
    license="MIT",
    scripts=["./bin/boxie"],
    packages=["boxie"],
)
