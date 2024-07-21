from typing import Any
# NOTE: No plans to support type hints in Behave until they drop support for Python2.7.
#  https://github.com/behave/behave/issues/1168#issuecomment-2028020747
#
# For now, I did what I could to bring these, this and the steps/*, modules
# into compliance with with strict type checking.  See the mypy.ini sections
# that address errors I could not fix any other way.  For the typehints that I
# did add here, I started with something very generic and permissive to satisfy
# the type-checker.  I'd like to come back and find some definitions that are
# more narrowly scoped.


# See: https://behave.readthedocs.io/en/latest/tutorial/#debug-on-error-in-case-of-step-failures
#
# $ -D BEHAVE_DEBUG_ON_ERROR
# $ -D BEHAVE_DEBUG_ON_ERROR=yes
# $ -D BEHAVE_DEBUG_ON_ERROR=no
BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata: Any) -> None:
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context: Any) -> None:
    setup_debug_on_error(context.config.userdata)


def after_step(context: Any, step: Any) -> None:
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb

        ipdb.post_mortem(step.exc_traceback)
