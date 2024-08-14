from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from types import ModuleType


class CommandTestCase(ABC):
    @property
    @abstractmethod
    def command(self) -> ModuleType: ...

    def test_it_defines_a_parser(self) -> None:
        self.assertTrue(  # type: ignore[attr-defined]
            hasattr(self.command, "add_parser"),
            f'The {self.command.__name__} module does not define an "add_parser" method.',
        )

    def test_it_defines_an_entrypoint(self) -> None:
        self.assertTrue(  # type: ignore[attr-defined]
            hasattr(self.command, "execute"),
            f'The "{self.command.__name__}" module does not define an "execute" method.',
        )
