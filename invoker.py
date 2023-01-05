from template_generators.flipper import Flipper


class Invoker:
    def __init__(self):
        pass

    @staticmethod
    def flipper():
        Flipper.generate_code()
