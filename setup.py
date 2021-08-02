from distutils.core import setup
from boxie.version import __version__

setup(
    name="boxie",
    version=__version__,
    author="UltiRequiem",
    author_email="eliaz.bobadilladev@gmail.com",
    url="https://github.com/UltiRequiem/boxie",
    include_package_data=True,
    license="MIT",
    scripts=["./bin/boxie"],
    packages=["boxie"],
)
