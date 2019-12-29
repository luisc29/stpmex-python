import time
from typing import Any, Dict

import pytest

from stpmex import Client


@pytest.mark.vcr
def test_registra_orden(client: Client, orden_dict: Dict[str, Any]):
    orden_dict['claveRastreo'] = f'CR{int(time.time())}'
    orden = client.ordenes.registra(**orden_dict)
    assert isinstance(orden.id, int)
