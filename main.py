from src.core.display_interface import DisplayInterface
from src.display.terminal_display import TerminalDisplay


def main():
    display = TerminalDisplay()
    display.proccess()


if __name__ == "__main__":
    main()