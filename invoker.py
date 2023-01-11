from template_generators.flipper import Flipper
from template_generators.psp22 import PSP22


class Invoker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def flipper(**kwargs) -> None:
        Flipper.generate_code()

    @staticmethod
    def psp22(**kwargs) -> None:
        PSP22.generate_code(**kwargs)
