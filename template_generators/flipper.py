from jinja2 import Environment, FileSystemLoader
from jinja2.environment import Template
import os


class Flipper:
    def __init__(self) -> None:
        self.dir_name = ''

    def _create_dir(self, dir_name: str) -> None:
        self.dir_name = dir_name
        os.mkdir(dir_name)

    def _write_file(self, file_name: str, content: str) -> None:
        f = open(self.dir_name + '/' + file_name, "w")
        f.write(content)
        f.close()

    def _template(self, template_name) -> Template:
        environment = Environment(loader=FileSystemLoader("templates/flipper/"))
        return environment.get_template(template_name)

    def _render_content(self, template: Template, **kwargs) -> str:
        return template.render(**kwargs)

    @classmethod
    def generate_code(cls, **kwargs) -> None:
        cls._create_dir(cls, "flipper")
        template = cls._template(cls, "flipper.txt")
        content = cls._render_content(cls, template, **kwargs)
        cls._write_file(cls, "lib.rs", content)
        template = cls._template(cls, "cargo.txt")
        content = cls._render_content(cls, template, **kwargs)
        cls._write_file(cls, "Cargo.toml", content)
