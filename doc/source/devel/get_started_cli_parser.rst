Password
=========

>>> import sys

>>> from ftwpki.password.cli_parser import password_parser, PasswordFileArguments

>>> pwargs = PasswordFileArguments()

>>> pwargs
PasswordFileArguments(outdir=''
passphrase_file=''
target_file='')

>>> pwargs.setup_args()

>>> pfp = password_parser()

>>> pfp # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
PKIBaseParser(prog='...', 
    usage=None, 
    description=None, 
    formatter_class=<class 'argparse.HelpFormatter'>, 
    conflict_handler='error', 
    add_help=True)

>>> pfp.print_help(file=sys.stderr)

>>> pfp.parse_args(["mypasswordfile"]) # doctest: +NORMALIZE_WHITESPACE
PasswordFileArguments(outdir='.private'
    passphrase_file='password.txt'
    target_file='mypasswordfile')

>>> pfp.parse_args(["mypasswordfile"], namespace=PasswordFileArguments()) # doctest: +NORMALIZE_WHITESPACE
PasswordFileArguments(outdir='.private'
    passphrase_file='password.txt'
    target_file='mypasswordfile')

>>> pfp = password_parser(pre_parser=True)



