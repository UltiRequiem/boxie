from boxie import box_borders


@box_borders
def print_console(txt):
    print(txt)


if __name__ == "__main__":
    print_console("Hello World")
