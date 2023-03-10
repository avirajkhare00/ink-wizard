import unittest
import hashlib
import shutil
import os

from ink_wizard.template_generators.psp22 import PSP22

class TestPSP22(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.isdir("psp22"):
            shutil.rmtree("psp22")
        PSP22.generate_code(basic=True, contract_name="MyToken")

    def tearDown(self) -> None:
        shutil.rmtree("psp22")

    def test_dir_exists(self) -> None:
        self.assertEqual(os.path.isdir("psp22"), True)

    def test_file_exists(self) -> None:
        self.assertEqual(os.path.isfile("psp22/lib.rs"), True)
        self.assertEqual(os.path.isfile("psp22/Cargo.toml"), True)

    def test_file_md5(self) -> None:
        contract = open("psp22/lib.rs", "rb")
        toml = open("psp22/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "a29268c2aa91933d5f82a0b72b96cac7")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "3d3d79fa04b324b4f3489422b39c66cd")
        contract.close()
        toml.close()

    def test_file_md5_with_all_options(self) -> None:
        if os.path.isdir("psp22"):
            shutil.rmtree("psp22")
        PSP22.generate_code(contract_name="MyToken", metadata=True, mintable=True, burnable=True, wrapper=True, flashmint=True, pausable=True, capped=True)
        contract = open("psp22/lib.rs", "rb")
        toml = open("psp22/Cargo.toml", "rb")
        self.assertEqual(hashlib.md5(contract.read()).hexdigest(), "0f13603bde7c85a2beba89d5c0cec4aa")
        self.assertEqual(hashlib.md5(toml.read()).hexdigest(), "3d3d79fa04b324b4f3489422b39c66cd")
        contract.close()
        toml.close()
