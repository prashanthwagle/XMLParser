

class TreeNode:
    def __init__(self, tag):
        self.tag = tag
        self.children = []
        self.parent = None


class ParseTree:
    def __init__(self, xml_string):
        self.stack = []
        self.root_node = None
        self.curr_node = None
        self.xml_string = xml_string

    def build_tree(self):
        current_tag = ""
        for char in self.xml_string:
            if char == '<':
                current_tag = ""
            elif char == '>':
                self._handle_tag(current_tag)
            else:
                current_tag += char

    def _handle_tag(self, tag):
        if tag.startswith('/'):
            self._handle_closing_tag(tag[1:])
        elif len(tag) > 3 and tag[-2] == "/":
            self._handle_self_closing_tag(tag[1:-2])
        else:
            self._handle_opening_tag(tag)

    def _handle_opening_tag(self, tag):
        if self.root_node == None:
            self.root_node = TreeNode(tag)
            self.curr_node = self.root_node
        else:
            newNode = TreeNode(tag)
            self.curr_node.children.append(newNode)
            newNode.parent = self.curr_node
            self.curr_node = newNode
        self.stack.append(tag)
        print("Opening tag", self._stack_dump())

    def _handle_self_closing_tag(self, tag):
        print("Self Closing tag", self._stack_dump())
        newNode = TreeNode(tag)
        self.curr_node.children.append(newNode)
        newNode.parent = self.curr_node
        self.curr_node = newNode

    def _handle_closing_tag(self, tag):
        self.curr_node = self.curr_node.parent
        if self.stack and self.stack[-1] == tag:
            print("Closing tag", self._stack_dump())
            self.stack.pop()
        else:
            print(f"Error: Mismatched closing tag '{tag}'")

    current_tag = ""
    for char in xml_string:
        if char == '<':
            current_tag = ""
        elif char == '>':
            handle_tag(current_tag)
        else:
            current_tag += char


if __name__ == "__main__":
    xml_string = """
    <a>
        <b>
            <e></e>
            <f>
                <g></g>
            </f>
        </b>
        <c>
            <h>
                <i></i>
                <j></j>
            </h>
        </c>
        <d></d>
    </a>
    """
    build_tree(xml_string)
