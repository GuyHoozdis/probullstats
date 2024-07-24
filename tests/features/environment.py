from __future__ import annotations

from argparse import Namespace
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from behave.model import Step
    from behave.runner import Context
    from behave.userdata import UserData


# See: https://behave.readthedocs.io/en/latest/tutorial/#debug-on-error-in-case-of-step-failures
#
# $ -D BEHAVE_DEBUG_ON_ERROR
# $ -D BEHAVE_DEBUG_ON_ERROR=yes
# $ -D BEHAVE_DEBUG_ON_ERROR=no
class _Configuration(Namespace):
    _instance = None

    def __new__(cls, **kwargs: dict[str, Any]) -> _Configuration:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            for attr, value in kwargs.items():
                setattr(cls, attr, value)
        return cls._instance


_config = _Configuration(
    debug_on_error=False,
)


def setup_debug_on_error(userdata: UserData) -> None:
    _config.debug_on_error = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context: Context) -> None:
    setup_debug_on_error(context.config.userdata)


def after_step(_: Context, step: Step) -> None:
    if _config.debug_on_error and step.status == "failed":
        import ipdb

        ipdb.post_mortem(step.exc_traceback)
