from typing import Any, ClassVar, Dict

from OpenSSL import crypto
from requests import Response, Session

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
        self, priv_key: str, priv_key_passphrase: str, demo: bool = False
    ):
        self.session = Session()
        if demo:
            self.base_url = DEMO_BASE_URL
        else:
            raise NotImplementedError('Sólo funciona en demo por ahora.')
        try:
            self._pkey = crypto.load_privatekey(
                crypto.FILETYPE_PEM,
                priv_key,
                priv_key_passphrase.encode('ascii'),
            )
        except crypto.Error:
            raise InvalidPassphrase
        Resource._client = self

    def put(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        return self.request('put', endpoint, **kwargs)

    def request(
        self,
        method: str,
        endpoint: str,
        data: Dict[str, Any],
        firma: str,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        url = self.base_url + endpoint
        data = {**data, **dict(firma=firma)}
        response = self.session.request(method, url, json=data, **kwargs)
        self._check_response(response)
        return response.json()

    @staticmethod
    def _check_response(response: Response) -> None:
        if response.ok:
            return
        response.raise_for_status()
