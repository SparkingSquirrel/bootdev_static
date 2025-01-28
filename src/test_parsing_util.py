import unittest

from textnode import TextNode, TextType
from parsing_util import *

class TestParsingUtil(unittest.TestCase):
    def test_single_node_single_tag(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]
        self.assertEqual(new_nodes, correct_nodes)

    def test_single_node_unmatched_tag(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "`", TextType.CODE)

    def test_multiple_nodes(self):
        node1 = TextNode("Text with a `code`", TextType.TEXT)
        node2 = TextNode("More text with `more code` words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        correct_nodes = [TextNode("Text with a ", TextType.TEXT),
                         TextNode("code", TextType.CODE),
                         TextNode("More text with ", TextType.TEXT),
                         TextNode("more code", TextType.CODE),
                         TextNode(" words", TextType.TEXT),]
        self.assertEqual(new_nodes, correct_nodes)

    def test_single_node_pipe(self):
        node = TextNode("This is text with a |code block| word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "|", TextType.CODE)
        correct_nodes = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]
        self.assertEqual(new_nodes, correct_nodes)
 
    def test_single_node_multi_tag(self):
        node = TextNode("This is text with a `code block` word with `more code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct_nodes = [TextNode("This is text with a ", TextType.TEXT), 
                        TextNode("code block", TextType.CODE), 
                        TextNode(" word with ", TextType.TEXT),
                        TextNode("more code", TextType.CODE)]
        self.assertEqual(new_nodes, correct_nodes)
