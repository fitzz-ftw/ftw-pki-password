# File: src/ftwpki/password/passwd_file.py
# Author: Fitzz TeXnik Welt
# Email: FitzzTeXnikWelt@t-online.de
# License: LGPLv2 or above
"""
passwd_file
===============================


Modul passwd_file documentation
"""

import sys
from pathlib import Path

from securify.input.exceptions import (
    PasswordMismatchError,
    PasswordSpeedError,
    PasswordTerminalError,
)
from securify.input.password import Callable, PasswordDoubleCheck

from ftwpki.baselibs.passwd import PasswordManager
from ftwpki.password.protocols import PasswordFileProtocol


class PasswdFile:
    def __init__(
        self,
        args: PasswordFileProtocol,
        tries_by_mismatch: int = 0,
        *,
        min_delay: float = 1.5,
        require_terminal: bool = True,
        prompt1: str = "",
        prompt2: str = "",
        **kwargs,
    ) -> None:
        pwcall: Callable[[str], str] = kwargs.pop("pwcall", None)
        self._args = args
        self._pm = PasswordManager(private_dir=args.outdir)
        self._password = PasswordDoubleCheck(
            min_delay=min_delay,
            require_terminal=require_terminal,
            prompt1=prompt1,
            prompt2=prompt2,
            pwcall=pwcall,
        )
        self._tries_by_mismatch = tries_by_mismatch

    def __repr__(self) -> str:
        """
        Return the canonical string representation.

        :returns: String containing the class name.
        """
        return f"{self.__class__.__name__}()"

    def _getpassword(self, prompt1: str = "", prompt2: str = "") -> str:
        current_try: int = 0
        while not self._password.is_valid or current_try <= self._tries_by_mismatch:
            current_try += 1
            try:
                retpasswd = self._password(prompt1, prompt2)
            except PasswordMismatchError as err:
                if current_try - 1 <= self._tries_by_mismatch:
                    pass
                else:
                    raise err
        return retpasswd

    def encrypt(self) -> int:
        """
        Execute the encryption process.

        :param args_list: Command line arguments.
        :returns: Exit code (0 for success, 1 for error).
        """

        try:
            password = self._getpassword(
                f"Password for '{self._args.target_file}': ", "Retype password: "
            )

            if not password:
                print("Error: Password is required.", file=sys.stderr)
                return 2

            self._pm.encrypt_password_file(
                input_file=self._args.passphrase_file,
                output_filename=self._args.target_file,
                password=password,
            )

            return 0
        except (PasswordMismatchError, PasswordSpeedError, PasswordTerminalError) as err:
            print(err)
            return 1

        except KeyboardInterrupt:
            return 1
        except Exception as err:
            print(f"Error: {err}", file=sys.stderr)
            return 1


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
    test_file = testfiles_dir / "get_started_passwd_file.rst"

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
