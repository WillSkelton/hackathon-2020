#!/usr/bin/env python3

from face_compare import compare
from face_compare import compareDir
import subprocess
import sys
import os


def main():
    args = sys.argv

    matches = []
    if os.path.isdir(args[1]) == True and os.path.isfile(args[2]):

        matches = compareDir(args[1], args[2])

        path = os.path.dirname(args[1])
        file_name = os.path.basename(args[2])

        file_path = os.path.dirname(args[2])

        subprocess.run(["mkdir", str(path) + "/../matches", "-p"])

        for match in matches:
            subprocess.run(
                ["cp", file_path + "/" + match, str(path) + "/../matches"])

    elif os.path.isdir(args[2]) == True and os.path.isfile(args[1]):

        matches = compareDir(args[2], args[1])

        path = os.path.dirname(args[2])
        file_name = os.path.basename(args[1])

        file_path = os.path.dirname(args[1])

        subprocess.run(["mkdir", str(path) + "/../matches", "-p"])

        for match in matches:
            subprocess.run(
                ["cp", file_path + "/" + match, str(path) + "/../matches"])

    else:
        ValueError("No dir and file pair received!")


if __name__ == '__main__':
    main()
