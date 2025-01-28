#some cross-class parsing utils
from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT: #only parses TEXT nodeds
            new_nodes.append(node)
        inside_delimiter = False
        text_to_split = node.text
        next_delimiter = text_to_split.find(delimiter)

        while len(text_to_split) > 0:
            # print(f'PARSING: {text_to_split}')
            # print(f'NEXT DELIMITER: {next_delimiter},  INSIDE_DELIMITER: {inside_delimiter}')
            if next_delimiter == -1 and inside_delimiter:
                raise Exception('Unmatched delimiter')
            if next_delimiter == 0 and inside_delimiter: #0 length inside delimiters. Not sure if we should make empty node or discard
                inside_delimiter = not inside_delimiter
            else:
                if next_delimiter == -1:
                    new_text = text_to_split
                else:
                    new_text = text_to_split[:next_delimiter]
                new_type = text_type if inside_delimiter else node.text_type
                new_node = TextNode(new_text, new_type, node.url)
                new_nodes.append(new_node)
                # print(f'NEW NODE: {new_node}')
                inside_delimiter = not inside_delimiter
            if next_delimiter == -1:
                text_to_split = ''
            else:
                text_to_split = text_to_split[next_delimiter + 1:]
            # print(f'RECALCULATED TEXT: {text_to_split}')
            next_delimiter = text_to_split.find(delimiter)
    return new_nodes

def extract_markdown_images(text):
    # images
    image_re = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
   # print(re.findall(image_re, text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    return(re.findall(image_re, text))

def extract_markdown_links(text):
         # regular links
    link_re = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return(re.findall(link_re, text))


