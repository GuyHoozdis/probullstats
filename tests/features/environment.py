# See: https://behave.readthedocs.io/en/latest/tutorial/#debug-on-error-in-case-of-step-failures
#
# $ -D BEHAVE_DEBUG_ON_ERROR
# $ -D BEHAVE_DEBUG_ON_ERROR=yes
# $ -D BEHAVE_DEBUG_ON_ERROR=no
BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import ipdb

        ipdb.post_mortem(step.exc_traceback)
