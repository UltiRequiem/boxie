from sys import argv


def box_borders(func):
    def wrapper(txt: str) -> None:
        txt_length = len(txt)
        print(" " + "_" * (txt_length + 1))
        print("/" + "_" * txt_length + "/|")
        print("|" + " " * txt_length + "||")
        func("|" + txt + "||")
        print("|" + "_" * txt_length + "|/")

    return wrapper


@box_borders
def print_console(txt: str) -> None:
    print(txt)


def run() -> None:
    try:
        message = argv[1]
    except IndexError:
        message = "You have to pass at least one word!"

    print_console(message)
