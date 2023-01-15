import unittest
from unittest import mock
import shutil
import os

from ink_wizard.commands.psp22 import PSP22Command

class TestPSP22Command(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("psp22"):
            shutil.rmtree("psp22")

    def tearDown(self) -> None:
        if os.path.isdir("psp22"):
            shutil.rmtree("psp22")

    def test_command(self) -> None:
        with mock.patch('typer.prompt', return_value="MyToken"):
            with mock.patch('typer.confirm', return_value=True):
                PSP22Command.run_command()
                self.assertEqual(os.path.isdir('psp22'), True)
                self.assertEqual(os.path.isfile('psp22/lib.rs'), True)
                self.assertEqual(os.path.isfile('psp22/Cargo.toml'), True)
