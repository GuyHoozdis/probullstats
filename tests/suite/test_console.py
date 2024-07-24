from __future__ import annotations

from testtools import TestCase

from probullstats import console


class ConsoleTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parser = console.create_parser()

    def test_main_succeeds(self) -> None:
        args = self.parser.parse_args([])
        returncode = console.main(args)
        self.assertEqual(0, returncode)
