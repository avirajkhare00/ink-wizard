import unittest
import hashlib
import shutil
import os

from template_generators.psp37 import PSP37

class TestPSP37(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("psp37"):
            shutil.rmtree("psp37")
        PSP37.generate_code(basic=True, contract_name="MyNFT")

    def tearDown(self) -> None:
        shutil.rmtree("psp37")

    def test_dir_exists(self) -> None:
        self.assertEqual(os.path.isdir("psp37"), True)

    def test_file_exists(self) -> None:
        self.assertEqual(os.path.isfile("psp37/lib.rs"), True)
        self.assertEqual(os.path.isfile("psp37/Cargo.toml"), True)

    def test_file_md5(self) -> None:
        contract = open("psp37/lib.rs", "rb")
        toml = open("psp37/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "8b1df85a952d631665d2aea87060d88f")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "76e5d813326f1e87c40ac3a085bcc368")
        contract.close()
        toml.close()

    def test_file_md5_with_all_options(self) -> None:
        if os.path.isdir("psp37"):
            shutil.rmtree("psp37")
        PSP37.generate_code(contract_name="MyNFT", metadata=True, mintable=True, burnable=True, enumrable=True)
        contract = open("psp37/lib.rs", "rb")
        toml = open("psp37/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "35549ffa08363dacc9fc3c527ba3a558")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "76e5d813326f1e87c40ac3a085bcc368")
        contract.close()
        toml.close()
