import curses
import sys

lightValues = [
    (" ", 0.0, 0.0),
    (".", 0.0, 0.2),
    (":", 0.2, 0.4),
    ("!", 0.4, 0.6),
    ("#", 0.6, 0.8),
    ("@", 0.8, 1.0)
]

def main(screen):
    curses.curs_set(False)
    curses.halfdelay(1)

    screen.clear()

    while True:
            screen.clear()
            LINES, COLS = screen.getmaxyx()

            # Rendering code goes below.

            screen.addstr(LINES // 2, COLS // 2, lightValues[1][0])

            # Rendering code goes above.
            screen.refresh()
            
            try:
                terminalInput = screen.getkey()

                if terminalInput == 'q':
                    break
                elif terminalInput == curses.KEY_RESIZE:
                    y, x = screen.getmaxyx()
                    screen.clear()
                    curses.resizeterm(y, x)
                    screen.refresh()

            except curses.error:
                pass


if __name__ == "__main__":
    curses.wrapper(main)