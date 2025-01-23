from textnode import *

def main():
    node1 = TextNode('testing text', TextType.BOLD)

    node2 = TextNode('image?', TextType.IMAGE, 'urltext')
    print(node1)
    print(node2)

if __name__ == "__main__":
    main()