# File: src/ftwpki/password/cli_parser.py
# Author: Fitzz TeXnik Welt
# Email: FitzzTeXnikWelt@t-online.de
# License: LGPLv2 or above
"""
cli_parser
===============================


Modul cli_parser documentation
"""

import argparse
from pathlib import Path
from typing import cast

from ftwpki.baselibs.cli_parser import ArgparseFix311
from ftwpki.password.protocols import PasswordFileProtocol


class PasswordFileParser(ArgparseFix311):
    """
    CLI for encrypting password files using the PasswordManager.
    """
    def __init__(self, prog: str | None = None, 
                 usage: str | None = None, 
                 description: str | None = None,
                 exit_on_error: bool = False,
                 **kwargs
                 ) -> None:
        description = description if description else "Encrypt a passphrase file into the private directory."
        super().__init__(
            prog,
            usage,
            description,
            exit_on_error=exit_on_error,
            **kwargs
        )
        self._setup_parser()

    def _setup_parser(self) -> None:
        """
        Configure the argument parser for target, source, and output directory.

        :returns: The configured ArgumentParser instance.
        """

        self.add_argument("target_file", 
                            help="Name of the encrypted output file"
                            )

        self.add_argument(
            "-p",
            "--passphrase-file",
            dest="passphrase_file",
            default="password.txt",
            help="Source file containing the passphrase (default: password.txt)",
        )

        self.add_argument(
            "-o",
            "--outdir",
            dest="outdir",
            default=".private",
            help="Target directory for encrypted files (default: .private)",
        )

    def parse_args(
        self, args: list[str] | None = None, namespace: argparse.Namespace | None = None
    ) -> PasswordFileProtocol:
        return cast(PasswordFileProtocol, super().parse_args(args, namespace))

    # def __repr__(self) -> str:
    #     """
    #     Return the canonical string representation.

    #     :returns: String containing the class name.
    #     """
    #     return f"{self.__class__.__name__}()"


def get_parser() -> argparse.ArgumentParser:
    """
    Get the argument parser for the password encryption tool.

    This function is used by Sphinx-argparse to automatically generate
    the CLI documentation.

    :return: An initialized ArgumentParser object.
    """
    parser = PasswordFileParser()
    return parser

# Hier den Code einfügen

if __name__ == "__main__": # pragma: no cover
    from doctest import FAIL_FAST, testfile
    
    be_verbose = False
    be_verbose = True
    option_flags = 0
    option_flags = FAIL_FAST
    test_sum = 0
    test_failed = 0
    
    # Pfad zu den dokumentierenden Tests
    testfiles_dir = Path(__file__).parents[3] / "doc/source/devel"
    test_file = testfiles_dir / "get_started_cli_parser.rst"
    
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
        if test_failed == 0:
            print(f"\nDocTests passed without errors, {test_sum} tests.")
        else:
            print(f"\nDocTests failed: {test_failed} tests.")
    else:
        print(f"⚠️ Warning: Test file {test_file.name} not found.")
