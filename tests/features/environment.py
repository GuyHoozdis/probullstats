from __future__ import annotations

from argparse import Namespace
from typing import Any


class _Configuration(Namespace):
    """Global configuraiton manager."""

    _instance = None

    def __new__(cls, **kwargs: bool) -> _Configuration:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            for attr, value in kwargs.items():
                setattr(cls, attr, value)
        return cls._instance


# See: https://behave.readthedocs.io/en/latest/tutorial/#debug-on-error-in-case-of-step-failures
#
# $ -D BEHAVE_DEBUG_ON_ERROR
# $ -D BEHAVE_DEBUG_ON_ERROR=yes
# $ -D BEHAVE_DEBUG_ON_ERROR=no
_config = _Configuration(debug_on_error=False)


def setup_debug_on_error(userdata: Any) -> None:
    _config.debug_on_error = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context: Any) -> None:
    setup_debug_on_error(context.config.userdata)


def after_step(_: Any, step: Any) -> None:
    if _config.debug_on_error and step.status == "failed":
        import ipdb

        ipdb.post_mortem(step.exc_traceback)


def before_step(context: Any, step: Any) -> None:
    """Add step to context for generating messages in the NotImplementedError"""
    context.step = step
