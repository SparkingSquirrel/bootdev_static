import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a different node', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_different_url(self):
        node = TextNode('This is a text node', TextType.BOLD, 'a url')
        node2 = TextNode('This is a text node', TextType.BOLD, 'a different url')
        self.assertNotEqual(node, node2)

    def test_convert_text(self):
        text = TextNode('Normal text', TextType.TEXT)
        html = text_node_to_html_node(text)
        self.assertEqual('Normal text', html.to_html())

    def test_convert_bold(self):
        text = TextNode('Bold text', TextType.BOLD)
        html = text_node_to_html_node(text)
        self.assertEqual('<b>Bold text</b>', html.to_html())

    def test_convert_italic(self):
        text = TextNode('Italic text', TextType.ITALIC)
        html = text_node_to_html_node(text)
        self.assertEqual('<i>Italic text</i>', html.to_html())

    def test_convert_code(self):
        text = TextNode('Code text', TextType.CODE)
        html = text_node_to_html_node(text)
        self.assertEqual('<code>Code text</code>', html.to_html())

    def test_convert_link(self): #revise once properties
        text = TextNode('Anchor text', TextType.LINK, 'linkurl')
        html = text_node_to_html_node(text)
        self.assertEqual('<a>Anchor text</a>', html.to_html())

    def test_convert_image(self): #revise once properties
        text = TextNode('image alt', TextType.IMAGE, 'imageurl')
        html = text_node_to_html_node(text)
        self.assertEqual('<img></img>', html.to_html())


if __name__ == "__main__":
    unittest.main()