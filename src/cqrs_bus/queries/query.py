from abc import ABC, abstractmethod
from typing import TypeVar

TResult = TypeVar("TResult")


class Query[TResult](ABC):
    """Marker base class for queries (read-only requests).

    Carries no fields of its own — subclass it and add data with ``@dataclass``,
    Pydantic, ``attrs``, or whatever you prefer.

    Optionally parameterize it with the result type its handler returns, e.g.
    ``class GetOrder(Query[Order])``. ``QueryBus.dispatch`` is then typed:
    dispatching a ``Query[Order]`` is inferred to return ``Order``.
    """


TQuery = TypeVar("TQuery", bound=Query)


class QueryHandler[TQuery: Query, TResult](ABC):
    @abstractmethod
    async def handle(self, query: TQuery) -> TResult:
        pass
