from template_generators.flipper import Flipper


class Invoker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def flipper() -> None:
        Flipper.generate_code()

    @staticmethod
    def psp22(**kwargs) -> None:
        pass
