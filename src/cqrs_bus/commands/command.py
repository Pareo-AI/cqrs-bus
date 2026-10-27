from abc import ABC, abstractmethod
from typing import TypeVar

TResult = TypeVar("TResult")


class Command[TResult](ABC):
    """Marker base class for commands (state-changing intents).

    Carries no fields of its own — subclass it and add data with ``@dataclass``,
    Pydantic, ``attrs``, or whatever you prefer.

    Optionally parameterize it with the result type its handler returns, e.g.
    ``class CreateOrder(Command[str])``. ``CommandBus.dispatch`` is then typed:
    dispatching a ``Command[str]`` is inferred to return ``str``.
    """


TCommand = TypeVar("TCommand", bound=Command)


class CommandHandler[TCommand: Command, TResult](ABC):
    @abstractmethod
    async def handle(self, command: TCommand) -> TResult:
        pass
