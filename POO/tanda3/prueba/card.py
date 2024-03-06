from dataclasses import dataclass
from typeguard import typechecked


@typechecked
@dataclass(frozen=True)
class Card:
    number: str
    suit: str