Password
=========



>>> from ftwpki.password.cli_parser import PasswordFileParser

>>> pfp = PasswordFileParser()
>>> pfp # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
PasswordFileParser(prog='...', 
    usage=None, 
    description='Encrypt a passphrase file into the out directory.', 
    formatter_class=<class 'argparse.HelpFormatter'>, 
    conflict_handler='error', 
    add_help=True)

>>> pfp.parse_args(["mypasswordfile"]) # doctest: +NORMALIZE_WHITESPACE
Namespace(target_file='mypasswordfile', 
    passphrase_file='password.txt', 
    outdir='.private')

>>> from ftwpki.password.cli_parser import get_parser
>>> get_parser() # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
PasswordFileParser(prog=..., 
    usage=None, 
    description='Encrypt a passphrase file into the out directory.', 
    formatter_class=<class 'argparse.HelpFormatter'>, 
    conflict_handler='error', 
    add_help=True)

>>> pfp = PasswordFileParser(run_setup=False)
>>> pfp # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
PasswordFileParser(prog='pytest', 
    usage=None, 
    description='Encrypt a passphrase file into the out directory.', 
    formatter_class=<class 'argparse.HelpFormatter'>, 
    conflict_handler='error', 
    add_help=True)
