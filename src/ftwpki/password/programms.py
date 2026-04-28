# File: src/ftwpki/password/programms.py
# Author: Fitzz TeXnik Welt
# Email: FitzzTeXnikWelt@t-online.de
# License: LGPLv2 or above
"""
programms
===============================


Modul programms documentation
"""

from pathlib import Path

from ftwpki.password.cli_parser import PasswordFileParser
from ftwpki.password.passwd_file import PasswdFile


def prog_password_enc(argv:list[str]| None=None, **kwargs) -> int:
    """
    Main entry point for the password encryption command line interface.

    This function initializes the PasswordCli, parses arguments,
    and executes the encryption/decryption logic.

    :return: Exit code (0 for success, non-zero for errors).
    """
    pfp = PasswordFileParser()
    args = pfp.parse_args(argv) # doctest: +NORMALIZE_WHITESPACE

    pwd_file = PasswdFile(args, **kwargs)
    return pwd_file.encrypt()


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
    test_file = testfiles_dir / "get_started_programms.rst"
    
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
