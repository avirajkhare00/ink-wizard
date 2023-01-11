import unittest
from contextlib import redirect_stdout
import io

from commands.template_select import TemplateSelect

class TestTemplateSelectCommand(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_show_option_command(self) -> None:
        f = io.StringIO()
        with redirect_stdout(f):
            TemplateSelect.show_options()
        s = f.getvalue()
        
        assert "Type 1 to scaffold flipper contract\n" in s
        assert "Type 2 to scaffold psp22 contract\n" in s
        assert "Type 3 to scaffold psp34 contract\n" in s
        assert "Type 4 to scaffold psp37 contract\n" in s
