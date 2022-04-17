import typing
from dataclasses import dataclass, field, asdict


@dataclass(frozen=True, eq=True)
class CoordinateModel:
    """ simple coordinate model """
    lng: float
    lat: float


@dataclass
class SiteModel:
    """ solar plant instance """
    id: int = field(default=1)
    capacity: float = field(default=200)
    panels: int = field(default=1)
    address: str = field(default='Artillery ave. 23')
    city: str = field(default='KS')
    state: str = field(default='UA')
    postal_code: str = field(default='73000')
    is_active: bool = field(default=False)
    coordinate: typing.Union[CoordinateModel, None] = field(default=None)

    @property
    def total_capacity(self):
        return self.capacity * self.panels

    def dump(self):
        return asdict(self)

    @classmethod
    def load(cls, kwargs):
        return cls(**kwargs)

