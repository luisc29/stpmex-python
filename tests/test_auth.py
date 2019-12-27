from stpmex.auth import (
    CUENTA_FIELDNAMES,
    ORDEN_FIELDNAMES,
    compute_signature,
    join_fields,
)


def test_join_fields_for_orden(orden):
    joined = (
        b'||40072|TAMIZI|||CR1564969083|90646|1.20|1|||646180110400000007||40'
        b'|Ricardo Sanchez|072691004495711499|ND||||||Prueba||||||5273144||T|'
        b'|3|1|||'
    )
    assert join_fields(orden, ORDEN_FIELDNAMES) == joined


def test_join_fields_for_cuenta(cuenta):
    joined = b'||TAMIZI|646180157099999993|rfcrfc5||'
    assert join_fields(cuenta, CUENTA_FIELDNAMES) == joined


def test_compute_signature(client, orden):
    firma = (
        'R7aT7P91HAyJi9Q+aKdy2OJXK27qiA23/uKZAQ08pHnZpBpCF+ANbH6MMZUmEj1Swdrd5'
        '8krbgGpEU3R+pSKLDd7Ngo/0MIWdy7Qrl0dIT0rDKjk1FdkgT9AtoHEeOkPcHso+qyyCv'
        'vkZgkCqyhZbpza3IOzKFd3QJs4nvqG+5g='
    )
    sig = compute_signature(client.pkey, join_fields(orden, ORDEN_FIELDNAMES))
    assert sig == firma
