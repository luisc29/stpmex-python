import time

import pytest


@pytest.mark.vcr
def test_registrar_orden(orden):
    orden.claveRastreo = f'CR{int(time.time())}'
    resp = orden._registra()
    assert resp['resultado']['descripcionError'] is None
    assert isinstance(resp['id'], int)
