import sys
from pathlib import Path
from colorama import init, Fore, Style


def display_structure(directory, indent_level=0):
    try:
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name))
        indent = ' ' * 4 * indent_level
        for item in items:
            if item.is_dir():
                print(indent + Fore.BLUE + item.name + '/' + Style.RESET_ALL)
                display_structure(item, indent_level + 1)
            elif item.is_file():
                print(indent + Fore.YELLOW + item.name + Style.RESET_ALL)
    except Exception as e:
        print('Exception occured: ' + str(e))


root_directory = Path(sys.argv[len(sys.argv) - 1])

display_structure(root_directory)
