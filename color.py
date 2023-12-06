
class Color:

    def __init__(self, name, r, g, b, a, description=""):
        self.name = name
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.description = description

    def to_css(self):
        css_name=f"--{self.name.replace(' ', '-').replace('/', '-').lower()}"
        # figma colours normalised between 0..1, rgba constructor rgb in range 0..255 hence scaling.
        return f"/* {self.description} */ \n \t{css_name}: rgba({self.r*255}, {self.g*255}, {self.b*255}, {self.a});"
