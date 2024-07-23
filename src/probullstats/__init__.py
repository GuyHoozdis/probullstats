"""An interface to the ProBullStats website."""

from importlib.metadata import version, PackageNotFoundError


try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"
