from setuptools import setup
from boxie import __version__, __author__, __author_email__, __url__, __package_name__

setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    license="MIT",
    scripts=["./bin/boxie"],
    packages=["boxie"],
)
