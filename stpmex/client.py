import dataclasses
from typing import ClassVar

from OpenSSL import crypto
from requests import Session

from .exc import InvalidPassphrase
from .resources import Orden, Resource

DEMO_BASE_URL = 'https://demo.stpmex.com:7024/speidemows/rest/'


class Client:

    base_url: str
    demo: bool
    session: Session

    # resources
    ordenes: ClassVar = Orden

    def __init__(
        self,
        priv_key: str,
        priv_key_passphrase: str,
        demo: bool = True,
    ):
        self.session = Session()
        if demo:
            self.base_url = DEMO_BASE_URL
        try:
            self._pkey = crypto.load_privatekey(
                crypto.FILETYPE_PEM,
                priv_key,
                priv_key_passphrase.encode('ascii'),
            )
        except crypto.Error:
            raise InvalidPassphrase
        Resource._client = self
