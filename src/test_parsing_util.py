import unittest

from textnode import TextNode, TextType
from parsing_util import *

class TestParsingUtil(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]
        self.assertEqual(new_nodes, correct_nodes)