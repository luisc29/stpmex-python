import random
import string

import pytest
from clabe import generate_new_clabes

from stpmex.resources import Cuenta


@pytest.mark.vcr
def test_alta_cuenta(client, cuenta_dict):
    cuenta = client.cuentas.alta(**cuenta_dict)
    assert isinstance(cuenta.id, int)


@pytest.mark.vcr
def test_baja_cuenta(client, cuenta):
    assert cuenta.baja()


@pytest.mark.vcr
def test_alta_lote(client, cuenta_dict):
    del cuenta_dict['rfcCurp']
    del cuenta_dict['cuenta']
    num_cuentas = 100
    rfcs = ''.join(
        [
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(num_cuentas)
        ]
    )
    clabes = generate_new_clabes(num_cuentas, '6461801570')

    lote = []
    for rfc, clabe in zip(rfcs, clabes):
        cuenta = Cuenta(**cuenta_dict, cuenta=clabe, rfcCurp=rfc)
        lote.append(cuenta)
    resp = client.cuentas.alta_lote(lote)
    assert list(resp.keys()) == clabes
    assert all(r['id'] == 0 for r in resp.values())
    assert all(r['descripcion'] == '' for r in resp.values())
    for cuenta in lote:
        cuenta.baja()
