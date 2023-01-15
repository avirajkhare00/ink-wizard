import unittest
import shutil
from contextlib import redirect_stdout
import io
import os

from ink_wizard.commands.flipper import FlipperCommand

class TestFlipperCommand(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("flipper"):
            shutil.rmtree("flipper")

    def tearDown(self) -> None:
        shutil.rmtree("flipper")

    def test_command(self) -> None:
        f = io.StringIO()
        with redirect_stdout(f):
            FlipperCommand.run_command()
        s = f.getvalue()
        self.assertEqual(s, "flipper scaffolded\n")