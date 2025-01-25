import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_single_child(self):
        leaf = LeafNode('b', 'This is a bold child node')
        parent = ParentNode('p', [leaf])
        self.assertEqual('<p><b>This is a bold child node</b></p>', parent.to_html())

    def test_multinode_child(self):
        leaf1 = LeafNode('b', 'This is a bold child node')
        leaf2 = LeafNode('i', 'This is an italic child node')

        parent = ParentNode('p', [leaf1, leaf2])
        self.assertEqual('<p><b>This is a bold child node</b><i>This is an italic child node</i></p>', parent.to_html())

    def test_nested_parent(self):
        leaf = LeafNode('b', 'This is a bold child node')
        inner_parent = ParentNode('p', [leaf])
        outer_parent = ParentNode('body', [inner_parent])
        self.assertEqual('<body><p><b>This is a bold child node</b></p></body>', outer_parent.to_html())

    

if __name__ == "__main__":
    unittest.main()