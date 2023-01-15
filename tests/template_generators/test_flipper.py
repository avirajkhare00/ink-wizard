import unittest
import hashlib
import shutil
import os

from ink_wizard.template_generators.flipper import Flipper

class TestFlipper(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("flipper"):
            shutil.rmtree("flipper")
        Flipper.generate_code()

    def tearDown(self) -> None:
        shutil.rmtree("flipper")

    def test_dir_exists(self) -> None:
        self.assertEqual(os.path.isdir("flipper"), True)

    def test_file_exists(self) -> None:
        self.assertEqual(os.path.isfile("flipper/lib.rs"), True)
        self.assertEqual(os.path.isfile("flipper/Cargo.toml"), True)

    def test_file_md5(self) -> None:
        contract = open("flipper/lib.rs", "rb")
        toml = open("flipper/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "841fad71d8f7d5f14bc063bd75b47263")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "48953a9a94e285ce1b33551960fcdba8")
        contract.close()
        toml.close()
