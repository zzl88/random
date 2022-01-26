import abc
import datetime

from typing import Callable, NamedTuple, Optional, Dict


class L2(NamedTuple):
    symbol: str
    price: float
    qty: float
    ts: datetime.datetime
    traded_qty: Optional[float] = 0.


class MDMgr(abc.ABCMeta):
    @abc.abstractmethod
    def subscribe(cls, symbol: str, callback: Callable[[L2], None]):
        ...


class OrderUpdate(NamedTuple):
    id_: str
    symbol: str
    price: float
    qty: float
    fill_qty: float = 0.


class NewOrder(NamedTuple):
    id_: str
    symbol: str
    price: float
    qty: float


class CancelOrder(NamedTuple):
    id_: str


class OEMgr(abc.ABCMeta):
    @abc.abstractmethod
    def subscribe(cls, callback: Callable[[OrderUpdate], None]):
        ...

    @abc.abstractmethod
    def send_new(cls, req: NewOrder):
        ...

    @abc.abstractmethod
    def send_cancel(cls, req: CancelOrder):
        ...


class TimerFactory(abc.ABCMeta):
    @abc.abstractmethod
    def call_at(cls, ts: datetime.datetime, callback: Callable[[], None]):
        ...


class Strategy(abc.ABCMeta):
    @abc.abstractmethod
    def configure(cls, md_mgr: MDMgr, oe_mgr: OEMgr,
                  timer_factory: TimerFactory, params: Dict):
        ...

    @abc.abstractmethod
    def start(cls):
        ...

    @abc.abstractmethod
    def stop(cls):
        ...


class Event(NamedTuple):
    ts: datetime.datetime
    in_new: Optional[NewOrder]
    in_cxl: Optional[CancelOrder]
    out_md: Optional[L2]
    out_ou: Optional[OrderUpdate]


class Backtester(object):
    def __init__(self):
        self._events: Dict[datetime.datetime, Event] = {}

    def configure(self):
        """
        * where to load historical data
        * exchange latencies
        """
        ...

    def run(self, strategy: Strategy, params: Dict):
        """
        1. load historical data, inserts deduced orders into self._events
        2. create MDMgr, OEMgr, TimerFactory
        3. configure strategy
        4. start strategy
        5. Loop until self._events is empty
        """
        ...

