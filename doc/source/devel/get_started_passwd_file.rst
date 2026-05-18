Password File Class
#####################

>>> from pathlib import Path
>>> import getpass
>>> from fitzzftw.devtools.testinfra import TestHomeEnvironment
>>> env = TestHomeEnvironment(Path("doc/source/devel/testhome"))
>>> env.setup()
>>> _ = env.copy2cwd("password.txt")

>>> from ftwpki.password.passwd_file import PasswdFile
>>> from ftwpki.password.cli_parser import PasswordFileParser

>>> pfp = PasswordFileParser()
>>> args = pfp.parse_args(["mypasswordfile"]) # doctest: +NORMALIZE_WHITESPACE


>>> pwd_file = PasswdFile(args)
>>> pwd_file
PasswdFile()

>>> import time

.. _stubpassword-label:

>>> class StubPassword:
...     def __init__(self):
...         self.generate = self._generate()
...     def _generate(self):
...         # first run 
...         yield "secret"
...         yield "secret"
...         # second run 
...         yield "secret"
...         time.sleep(2)
...         yield "secret"
...         # third run 
...         yield "secret"
...         time.sleep(2)
...         yield "sacrat"
...         yield "secret"
...         time.sleep(2)
...         yield "sacrat"
...         # forth run
...         yield ""
...         time.sleep(2)
...         yield ""
...     def __call__(self, prompt):
...         print(prompt, flush=True)
...         return next(self.generate)

Initialize the stub passwordgenerator.

>> stubgetpasswd = StubPassword()

>>> getpass.getpass = StubPassword()

.. note::
   
   In automated environments (like GitHub Actions), there is no interactive terminal (TTY) available. 
   To prevent the CI process from failing with a ``PasswordTerminalError``, we must explicitly 
   set ``require_terminal=False``.


>>> pwd_file_test = PasswdFile(args, require_terminal=False)

>>> pwd_file_test.encrypt()
Password for 'mypasswordfile': 
Retype password: 
Input rejected: Entry was too fast (0.00s). Minimum required: 1.5s.
1

>>> pwd_file_test.encrypt()
Password for 'mypasswordfile': 
Retype password: 
0

>>> pwd_file_test.encrypt()
Password for 'mypasswordfile': 
Retype password: 
Password for 'mypasswordfile': 
Retype password: 
Verification failed: Passwords do not match.
1

>>> pwd_file_test.encrypt()
Password for 'mypasswordfile': 
Retype password: 
2

>>> def stubkeyboardinterrupt(obj):
...     raise KeyboardInterrupt()

>>> getpass.getpass = stubkeyboardinterrupt

>>> pwd_file_test = PasswdFile(args, require_terminal=False)
>>> pwd_file_test.encrypt()
1

>>> def stubexception(obj):
...     raise Exception("Test Exception!")

>>> getpass.getpass = stubexception

>>> pwd_file_test = PasswdFile(args, require_terminal=False)
>>> pwd_file_test.encrypt()
1

>>> env.teardown()
