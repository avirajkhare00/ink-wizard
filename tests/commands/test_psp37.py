import unittest
from unittest import mock
import shutil
import os

from commands.psp37 import PSP37Command

class TestPSP37Command(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("psp37"):
            shutil.rmtree("psp37")

    def tearDown(self) -> None:
        if os.path.isdir("psp37"):
            shutil.rmtree("psp37")

    def test_command(self) -> None:
        with mock.patch('typer.prompt', return_value="MyToken"):
            with mock.patch('typer.confirm', return_value=True):
                PSP37Command.run_command()
                self.assertEqual(os.path.isdir('psp37'), True)
                self.assertEqual(os.path.isfile('psp37/lib.rs'), True)
                self.assertEqual(os.path.isfile('psp37/Cargo.toml'), True)
