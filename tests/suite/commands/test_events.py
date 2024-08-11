from __future__ import annotations

from testtools import TestCase

from probullstats.commands import events

from . import CommandTestCase


class EventsCommandTestCases(CommandTestCase, TestCase):
    command = events
