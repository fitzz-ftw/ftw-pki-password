
from typing import Protocol


class PasswordFileProtocol(Protocol):
    target_file:str
    passphrase_file:str
    outdir:str
    
