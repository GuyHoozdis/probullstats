from __future__ import annotations

from argparse import Namespace
from typing import Any, TypedDict, Unpack


# See: https://behave.readthedocs.io/en/latest/tutorial/#debug-on-error-in-case-of-step-failures
#
# $ -D BEHAVE_DEBUG_ON_ERROR
# $ -D BEHAVE_DEBUG_ON_ERROR=yes
# $ -D BEHAVE_DEBUG_ON_ERROR=no
class _Configuration(Namespace):
    _instance = None

    class Options(TypedDict):
        debug_on_error: bool
        # Additional custom configuration options can be formalized here.

    def __new__(cls, **kwargs: Unpack[_Configuration.Options]) -> _Configuration:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            for attr, value in kwargs.items():
                setattr(cls, attr, value)
        return cls._instance


kwargs: _Configuration.Options = {"debug_on_error": False}
_config = _Configuration(**kwargs)


def setup_debug_on_error(userdata: Any) -> None:
    _config.debug_on_error = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context: Any) -> None:
    setup_debug_on_error(context.config.userdata)


def after_step(_: Any, step: Any) -> None:
    if _config.debug_on_error and step.status == "failed":
        import ipdb

        ipdb.post_mortem(step.exc_traceback)
