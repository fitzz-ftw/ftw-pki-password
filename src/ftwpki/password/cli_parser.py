# File: src/ftwpki/password/cli_parser.py
# Author: Fitzz TeXnik Welt
# Email: FitzzTeXnikWelt@t-online.de
# License: LGPLv2 or above
"""
cli_parser
===============================

This module provides the command-line interface for the password
encryption tool, mapping arguments to the PasswordFileProtocol. (rw)
"""

import argparse
from pathlib import Path
from typing import Any

from ftwpki.baselibs._cli_parser import (
    _HELP,
    ArgparseFix311,
    BaseArguments,
    load_help_entries,
    parser_factory_creator,
)

HELP_FILE = Path(__file__).parent.joinpath("cli_parser.help")

# print(_HELP)

load_help_entries(_HELP,HELP_FILE)


LANG = "en"


# CLASS - PasswordFileArguments
class PasswordFileArguments(BaseArguments):
    __slots__=["target_file", 
               "passphrase_file", 
               "outdir"]
    helpid: list[str] = ["passwordfile"]
    arg_data = {
        "target_file": {"flags": [], "kws": {}, "pre": {"nargs": "?"}},
        "passphrase_file": {
            "flags": ["-p", "--passphrase-file"],
            "kws": {
                "default": "password.txt",
            },
            "pre": {},
        },
        "outdir": {"flags": ["-o", "--outdir"], 
                    "kws": {"default":".private"}, 
                    "pre": {}},
    }

    def __init__(self) -> None:
        super().__init__()
        self.target_file: str = ""
        self.passphrase_file: str = ""
        self.outdir: str = ""


# !CLASS - PasswordFileArguments


password_parser = parser_factory_creator(PasswordFileArguments)



if __name__ == "__main__":  # pragma: no cover
    from doctest import FAIL_FAST, testfile

    be_verbose = False
    be_verbose = True
    option_flags = 0
    option_flags = FAIL_FAST
    test_sum = 0
    test_failed = 0
    passed_files = 0

    # Pfad zu den dokumentierenden Tests
    testfiles_dir = Path(__file__).parents[3] / "doc/source/devel"

    test_files = [
        # "test_new_parser.rst",
        "get_started_cli_parser.rst",
    ]
    for file in test_files:
        test_file = testfiles_dir / file
        if test_file.exists():
            print(f"--- Running Doctest for {test_file.name} ---")
            doctestresult = testfile(
                str(test_file),
                module_relative=False,
                verbose=be_verbose,
                optionflags=option_flags,
            )
            test_failed += doctestresult.failed
            test_sum += doctestresult.attempted
            if doctestresult.failed > 0 and option_flags & FAIL_FAST:
                print(f"Doctest result for {test_file.name}: {doctestresult}")
                print(
                    f"\nKeep going! You already passed {passed_files} files "
                    f"with {test_sum} tests before this hit."
                )
                break  # Stop on first failure if FAIL_FAST is set
            passed_files += 1
        else:
            print(f"⚠️ Warning: Test file {test_file.name} not found.")
    if test_failed == 0:
        print(f"\nDocTests passed without errors, {test_sum} tests.")
    else:
        if not option_flags & FAIL_FAST:
            print(f"\nDocTests failed: {test_failed} tests out of {test_sum}.")
