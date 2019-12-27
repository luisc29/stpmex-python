import time

import pytest


@pytest.mark.vcr
def test_registra_orden(client, orden_dict):
    orden_dict['claveRastreo'] = f'CR{int(time.time())}'
    orden = client.ordenes.registra(**orden_dict)
    assert isinstance(orden.id, int)
