from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError('Parent node needs a tag')
        if self.children == None or len(self.children) < 1:
            raise ValueError('Parent node needs children')
        html_string = f'<{self.tag}>'
        for child in self.children:
            html_string = f'{html_string}{child.to_html()}'
        return f'{html_string}</{self.tag}>'
        