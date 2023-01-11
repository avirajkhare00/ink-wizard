import typer

from commands.template_select import TemplateSelect
from commands.flipper import FlipperCommand
from commands.psp22 import PSP22Command

def main() -> None:
    
    TemplateSelect.show_options()

    contract_type = TemplateSelect.ask_user()

    if contract_type == "1":
        FlipperCommand.run_command()
    if contract_type == "2":
        PSP22Command.run_command()


if __name__ == "__main__":
    typer.run(main)
