# File: src/ftwpki/password/protocols.py
# Author: Fitzz TeXnik Welt
# Email: FitzzTeXnikWelt@t-online.de
# License: LGPLv2 or above
"""
protocols
===============================

This module defines structural interfaces for the password management
package. (ro)
"""

from pathlib import Path
from typing import Protocol


# CLASS - PasswordFileProtocol
class PasswordFileProtocol(Protocol):
    """
    Structural interface for password file operations. (ro)

    Defines the required attributes for handling the encryption and
    storage of passphrase files.
    """

    target_file: str
    """The name of the encrypted file to be created or read."""
    passphrase_file: str
    """The path to the source file containing the raw passphrase."""
    outdir: str
    """The directory where the encrypted secret will be stored."""


# !CLASS - PasswordFileProtocol
# Hier den Code einfügen

if __name__ == "__main__":  # pragma: no cover
    from doctest import FAIL_FAST, testfile

    be_verbose = False
    be_verbose = True
    option_flags = 0
    option_flags = FAIL_FAST
    test_sum = 0
    test_failed = 0

    # Pfad zu den dokumentierenden Tests
    testfiles_dir = Path(__file__).parents[3] / "doc/source/devel"
    test_file = testfiles_dir / "get_started_protocols.rst"

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
