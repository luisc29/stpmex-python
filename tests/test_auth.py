from stpmex.auth import (
    CUENTA_FIELDNAMES,
    ORDEN_FIELDNAMES,
    compute_signature,
    join_fields,
)


def test_join_fields_for_orden(orden):
    joined = (
        b'||40072|TAMIZI|||CR1564969083|90646|1.20|1|||||40|Ricardo Sanchez|07'
        b'2691004495711499|ND||||||Prueba||||||5273144||T||3|1|||'
    )
    assert join_fields(orden, ORDEN_FIELDNAMES) == joined


def test_join_fields_for_cuenta(cuenta):
    joined = b'||TAMIZI|646180110400000007|rfcrfc||'
    assert join_fields(cuenta, CUENTA_FIELDNAMES) == joined


def test_compute_signature(client, orden):
    firma = (
        'wheaue7DpL7ro+9GAR4pJAscGTT+UPD/aXiAchkQI/61QIJBcAzhecW7BG9bAVTG5fI8g'
        'Ah6CdTEQn9q1O7VClOLdRqjNVluOLtDhm4iq5R7ew9+tjjHMJAv7JtSX7W9v55NtR9/jZ'
        '7RhSUbvEvS06Tfxq5CX+Ct7ySDOOiaOpM='
    )
    sig = compute_signature(client.pkey, join_fields(orden, ORDEN_FIELDNAMES))
    assert sig == firma
