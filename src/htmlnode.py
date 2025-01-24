class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def propst_to_html(self):
        prop_string = ''
        for prop in self.props:
            prop_string = f'{prop_string} {prop}= "{self.props[prop]}"'
        return prop_string
    
    def __repr__(self):
        return f'HTMLNode: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}'