import time
from typing import Any, Dict

import pytest

from stpmex import Client
from stpmex.resources import Orden
from stpmex.types import TipoCuenta


@pytest.mark.vcr
def test_registra_orden(client: Client, orden_dict: Dict[str, Any]):
    orden_dict['claveRastreo'] = f'CR{int(time.time())}'
    orden = client.ordenes.registra(**orden_dict)
    assert isinstance(orden.id, int)


@pytest.mark.parametrize(
    'cuenta, tipo',
    [
        ('072691004495711499', TipoCuenta.clabe),
        ('4000000000000002', TipoCuenta.card),
        ('5512345678', TipoCuenta.phone_number),
    ],
)
def test_tipoCuentaBeneficiario(orden: Orden, cuenta: str, tipo: TipoCuenta):
    orden.cuentaBeneficiario = cuenta
    assert orden.tipoCuentaBeneficiario == tipo.value


def test_invalid_cuentaBeneficiario(orden: Orden):
    orden.cuentaBeneficiario = '123'
    with pytest.raises(ValueError):
        orden.tipoCuentaBeneficiario
