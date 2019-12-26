from typing import ClassVar


class Resource:
    _client: ClassVar['stpmex.Client']  # type: ignore
    _endpoint: ClassVar[str]
    empresa: ClassVar[str]
