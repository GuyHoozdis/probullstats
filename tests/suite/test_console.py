from testtools import TestCase

from probullstats import console


class ConsoleTestCase(TestCase):

    def test_main_succeeds(self) -> None:
        exit_code = console.main()
        self.assertEqual(0, exit_code)
