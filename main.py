import typer

from invoker import Invoker

def main() -> None:
    
    print("Welcome to Ink Wizard!")
    print("Type 1 to scaffold flipper contract")
    print("Type 2 to scaffold psp22 contract")
    print("Type 3 to scaffold psp34 contract")
    print("Type 4 to scaffold psp37 contract")

    contract_type = typer.prompt("Enter your choice to continue")

    if contract_type == "1":
        Invoker.flipper()
        print("flipper scaffolded")
    if contract_type == "2":
        contract_name = typer.prompt("Please enter name of contract")
        metadata = typer.confirm("Do you want to store Metadata?")
        mintable = typer.confirm("Do you want it to be mintable?")
        burnable = typer.confirm("Do you want it to be burnable?")
        wrapper = typer.confirm("Do you want it to be wrapper?")
        flashmint = typer.confirm("Do you want it to be flashmint?")
        pausable = typer.confirm("Do you want it to be pausable?")
        capped = typer.confirm("Do you want it to be capped?")
        Invoker.psp22(contract_name=contract_name, mintable=mintable, metadata=metadata, burnable=burnable, wrapper=wrapper, flashmint=flashmint, pausable=pausable, capped=capped)
        print("psp22 contract scaffolded")


if __name__ == "__main__":
    typer.run(main)
