from typing import Callable
from sys import argv


def box_borders(func: Callable) -> Callable[[str], None]:
    """
    Boxie Decorator
    """

    def wrapper(txt: str) -> None:
        txt_length = len(txt)
        print(" " + "_" * (txt_length + 1))
        print("/" + "_" * txt_length + "/|")
        print("|" + " " * txt_length + "||")
        func("|" + txt + "||")
        print("|" + "_" * txt_length + "|/")

    return wrapper


@box_borders
def boxie(txt: str) -> None:
    """
    Pass the text that you want to be printed with borders
    """
    print(txt)


def run() -> None:
    """
    This is the main function
    """
    try:
        message = argv[1]
    except IndexError:
        message = "You have to pass at least one word!"

    boxie(message)
