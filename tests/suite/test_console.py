from __future__ import annotations

import io
import sys

from testtools import TestCase

from probullstats import console


class ConsoleTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parser = console.create_parser()

    def test_main_requires_command(self) -> None:
        stderr = io.StringIO()
        self.patch(sys, "stderr", stderr)

        error = self.assertRaises(SystemExit, self.parser.parse_args, [])

        self.assertEqual(error.code, 2)
        self.assertIn("the following arguments are required", stderr.getvalue())
