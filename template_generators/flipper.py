from templates.flipper.base_template import code, toml

import os


class Flipper:
    def __init__(self):
        self.dir_name = ''

    def __create_dir(self, dir_name):
        self.dir_name = dir_name
        os.mkdir(dir_name)

    def __write_file(self, file_name, content):
        f = open(self.dir_name + '/' + file_name, "w")
        f.write(content)
        f.close()

    @classmethod
    def generate_code(cls):
        cls.__create_dir(cls, "flipper")
        cls.__write_file(cls, "lib.rs", code)
        cls.__write_file(cls, "Cargo.toml", toml)
