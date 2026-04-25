import argparse
from typing import Any, Sequence, cast

from ftwpki.password.protocols import PasswordFileProtocol


class PasswordFileParser(argparse.ArgumentParser):
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

    def __repr__(self) -> str:
        """
        Return the canonical string representation.

        :returns: String containing the class name.
        """
        return f"{self.__class__.__name__}()"


def get_parser() -> argparse.ArgumentParser:
    """
    Get the argument parser for the password encryption tool.

    This function is used by Sphinx-argparse to automatically generate
    the CLI documentation.

    :return: An initialized ArgumentParser object.
    """
    return PasswordFileParser()
