import pytest


@pytest.mark.vcr
def test_alta_cuenta(client, cuenta_dict):
    cuenta = client.cuentas.alta(**cuenta_dict)
    assert isinstance(cuenta.id, int)


@pytest.mark.vcr
def test_baja_cuenta(client, cuenta):
    assert cuenta.baja()
