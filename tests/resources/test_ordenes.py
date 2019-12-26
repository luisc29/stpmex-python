import time

import pytest


@pytest.mark.vcr
def test_registrar_orden(orden):
    orden.claveRastreo = f'CR{int(time.time())}'
    resp = orden._registra()
    assert resp.get('descripcionError') is None
    assert isinstance(resp['id'], int)


@pytest.mark.vcr
def test_create_orden(client, orden_dict):
    orden_dict['claveRastreo'] = f'CR{int(time.time())}'
    orden = client.ordenes.create(**orden_dict)
    assert isinstance(orden.id, int)
