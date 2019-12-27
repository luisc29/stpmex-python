import pytest


@pytest.mark.vcr
def test_create_cuenta(client, cuenta_dict):
    cuenta = client.cuentas.create(**cuenta_dict)
    assert isinstance(cuenta.id, int)


@pytest.mark.vcr
def test_delete_cuenta(client, cuenta):
    assert cuenta.delete()
