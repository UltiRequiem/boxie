"""
Core of The Project
"""
from typing import Callable
import sys

from .ui import cprint, setup_colorama, red

setup_colorama()


def box_borders(func: Callable) -> Callable[[str], None]:
    """
    Boxie Decorator
    """

    def wrapper(txt: str) -> None:
        txt_length = len(txt)
        cprint(" " + "_" * (txt_length + 1))
        cprint("/" + "_" * txt_length + "/|")
        cprint("|" + " " * txt_length + "||")
        func("|" + txt + "||")
        cprint("|" + "_" * txt_length + "|/")

    return wrapper


@box_borders
def boxier(txt: str) -> None:
    """
    Pass the text that you want to be cprinted with borders
    """
    cprint(txt)


def main() -> None:
    """
    This is the main function
    """
    try:
        message = sys.argv[1]
    except IndexError:
        cprint("You have to pass at least one word!", red)
        sys.exit(0)

    boxier(message)
