import sys

import colorama

cyan, red = (
    colorama.Fore.CYAN,
    colorama.Fore.RED,
)


def setup_colorama() -> None:
    """
    Execute init function of Colorama. This is not necessary in Linux or Darwin.
    """
    if "win" in sys.platform:
        colorama.init()


def cprint(
    text: str,
    color: str = cyan,
    brightness: str = colorama.Style.NORMAL,
    **kwargs,
) -> None:
    """
    Print the text with colors.
    """
    print(f" {brightness}{color}{text}{colorama.Style.RESET_ALL}", **kwargs)
