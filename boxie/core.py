from sys import argv


def box_borders(func):
    def wrapper(txt: str) -> None:
        print(" " + "_" * (len(txt) + 1))
        print("/" + "_" * len(txt) + "/|")
        print("|" + " " * len(txt) + "||")
        func("|" + txt + "||")
        print("|" + "_" * len(txt) + "|/")

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
