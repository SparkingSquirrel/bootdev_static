import unittest

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_bold(self):
        node = LeafNode("b", "This is a bold leaf node")
        self.assertEqual("<b>This is a bold leaf node</b>", node.to_html()) 

    def test_plain(self):
        node = LeafNode(None, "This is a plain leaf node")
        self.assertEqual("This is a plain leaf node", node.to_html()) 

    def test_with_props(self):  #this will need to get updated once props being handled
        node = LeafNode("i", "This is an italic leaf node with props", {'prop1': 'value1', 'prop2': 'value2'})
        self.assertEqual("<i>This is an italic leaf node with props</i>", node.to_html()) 


if __name__ == "__main__":
    unittest.main()