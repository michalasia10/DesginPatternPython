class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name: str = name
        self.text: str = text
        self.elements: list = []

    def __str(self, indent):
        lines: list = []
        i : str = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
        for e in self.elements:
            lines.append(e.__str(indent + 1))
        lines.append(f'{i}<{self.name}')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name :str = root_name
        self.__root : HtmlElement = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)

builder = HtmlBuilder('ul')

#without return self
builder.add_child('li','hello')
builder.add_child('li','world')

#with return self
builder.add_child_fluent('li','fluent').add_child_fluent('li','fluent_second')

print(f"Ordinary builder\n {builder}")
