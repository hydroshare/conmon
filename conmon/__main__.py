"""
A __main__ namespace for the conmon package.
"""

import sys
import argparse
from time import time
from conmon.monitor import server_up


def main(argv):
    """
    main(argv) -> None

    where argv -> command line arguments

    Call the package if run as a script.
    """

    print(server_up())

    return

if __name__ == '__main__':
    main(sys.argv[1:])
