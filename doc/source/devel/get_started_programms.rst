The Password Programm
=======================

>>> from pathlib import Path
>>> from fitzzftw.devtools.testinfra import TestHomeEnvironment
>>> env = TestHomeEnvironment(Path("doc/source/devel/testhome"))
>>> env.setup()
>>> _ = env.copy2cwd("password.txt")

>>> import time

>>> import getpass

>>> class StubPassword:
...     def __init__(self):
...         self.generate = self._generate()
...     def _generate(self):
...         # first run 
...         yield "secret"
...         time.sleep(2)
...         yield "secret"
...     def __call__(self, prompt):
...         print(prompt, flush=True)
...         return next(self.generate)


>>> getpass.getpass= StubPassword()

>>> sys_argv = ["mypasswordfile",]

>>> from ftwpki.password.cli_parser import  password_parser

>>> pfp =  password_parser()
>>> args = pfp.parse_args(sys_argv) # doctest: +NORMALIZE_WHITESPACE

>>> from ftwpki.password.passwd_file import PasswdFile
>>> pwd_file = PasswdFile(args, require_terminal=False)

>>> pwd_file.encrypt()
Password for 'mypasswordfile': 
Retype password: 
0

>>> getpass.getpass = StubPassword()

>>> from ftwpki.password.programms import prog_password_enc

>>> prog_password_enc(sys_argv, require_terminal=False)
Password for 'mypasswordfile': 
Retype password: 
0



>>> env.clean_home()
>>> env.teardown()

