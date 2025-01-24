import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    pass
    def test_repr(self):
        children = ['dummy child']
        props = {'prop1': 'value1', 'prop2': 'value2'}
        node = HTMLNode('tag', 'This string is the value', children, props)
        correct_string = "HTMLNode: tag=tag, value=This string is the value, children=['dummy child'], props={'prop1': 'value1', 'prop2': 'value2'}"
        self.assertEqual(node.__repr__(), correct_string)

    def test_props_two(self):
        children = ['dummy child']
        props = {'prop1': 'value1', 'prop2': 'value2'}
        node = HTMLNode('tag', 'This string is the value', children, props)    
        self.assertEqual(node.props_to_html(), ' prop1="value1" prop2="value2"')

    def test_props_one(self):
        children = ['dummy child']
        props = {'prop1': 'value1'}
        node = HTMLNode('tag', 'This string is the value', children, props)    
        self.assertEqual(node.props_to_html(), ' prop1="value1"')            

    def test_props_one(self):
        children = ['dummy child']
        node = HTMLNode('tag', 'This string is the value', children)    
        self.assertEqual(node.props_to_html(), '')    

if __name__ == "__main__":
    unittest.main()