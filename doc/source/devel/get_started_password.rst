>>> from ftwpki.baselibs.passwd import PasswordCli

>>> pc = PasswordCli()
>>> pc
PasswordCli()

>>> pm.encrypt_password_file("not_exist_pw.txt", "root.enc", "my_password")
Traceback (most recent call last):
    ...
FileNotFoundError: Input file not_exist_pw.txt is missing or empty.

>>> pm.decrypt_password_file("not_exist_root.enc", "my_password")
Traceback (most recent call last):
    ...
FileNotFoundError: Encrypted file not_exist_root.enc not found.

>>> from ftwpki.baselibs.passwd import get_parser
>>> get_parser() # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
ArgumentParser(prog=..., 
    usage=None, 
    description='Encrypt a passphrase file into the private directory.', 
    formatter_class=<class 'argparse.HelpFormatter'>, 
    conflict_handler='error', 
    add_help=True)
