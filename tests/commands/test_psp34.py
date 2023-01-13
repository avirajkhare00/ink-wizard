import unittest
from unittest import mock
import shutil
import os

from commands.psp34 import PSP34Command

class TestPSP34Command(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("psp34"):
            shutil.rmtree("psp34")

    def tearDown(self) -> None:
        if os.path.isdir("psp34"):
            shutil.rmtree("psp34")

    def test_command(self) -> None:
        with mock.patch('typer.prompt', return_value="MyNFT"):
            with mock.patch('typer.confirm', return_value=True):
                PSP34Command.run_command()
                self.assertEqual(os.path.isdir('psp34'), True)
                self.assertEqual(os.path.isfile('psp34/lib.rs'), True)
                self.assertEqual(os.path.isfile('psp34/Cargo.toml'), True)
