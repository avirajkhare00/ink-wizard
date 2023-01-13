import unittest
import hashlib
import shutil
import os

from template_generators.psp34 import PSP34

class TestPSP34(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("psp34"):
            shutil.rmtree("psp34")
        PSP34.generate_code(basic=True, contract_name="MyNFT")

    def tearDown(self) -> None:
        shutil.rmtree("psp34")

    def test_dir_exists(self) -> None:
        self.assertEqual(os.path.isdir("psp34"), True)

    def test_file_exists(self) -> None:
        self.assertEqual(os.path.isfile("psp34/lib.rs"), True)
        self.assertEqual(os.path.isfile("psp34/Cargo.toml"), True)

    def test_file_md5(self) -> None:
        contract = open("psp34/lib.rs", "rb")
        toml = open("psp34/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "233532e6dacb8959b84a83e56c6405d8")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "a855b502f79366206e5010ec996f24a8")
        contract.close()
        toml.close()

    def test_file_md5_with_all_options(self) -> None:
        if os.path.isdir("psp34"):
            shutil.rmtree("psp34")
        PSP34.generate_code(contract_name="MyNFT", metadata=True, mintable=True, burnable=True, enumrable=True)
        contract = open("psp34/lib.rs", "rb")
        toml = open("psp34/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "ecaf4f0db0b23a88a224f0aae3ba3415")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "a855b502f79366206e5010ec996f24a8")
        contract.close()
        toml.close()
