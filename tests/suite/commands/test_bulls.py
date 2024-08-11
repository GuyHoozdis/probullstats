from __future__ import annotations

from testtools import TestCase

from probullstats.commands import bulls

from . import CommandTestCase


class BullsCommandTestCase(CommandTestCase, TestCase):
    command = bulls
