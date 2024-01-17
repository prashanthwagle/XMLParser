from collections import deque


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
        self.xml_data = []

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
            new_node = TreeNode(tag)
            self.curr_node.children.append(new_node)
            new_node.parent = self.curr_node
            self.curr_node = new_node
        self.stack.append(tag)
        print("Opening tag", self._stack_dump())

    def _handle_self_closing_tag(self, tag):
        print("Self Closing tag", self._stack_dump())
        new_node = TreeNode(tag)
        self.curr_node.children.append(new_node)
        new_node.parent = self.curr_node
        self.curr_node = new_node

    def _handle_closing_tag(self, tag):
        self.curr_node = self.curr_node.parent
        if self.stack and self.stack[-1] == tag:
            print("Closing tag", self._stack_dump())
            self.stack.pop()
        else:
            print(f"Error: Mismatched closing tag '{tag}'")

    def _stack_dump(self):
        return self.stack

    def print_tree(self):
        queue = deque()
        queue.append(self.root_node)

        level = 0

        while queue:
            curr_level = []
            curr_node = queue.popleft()
            if len(curr_node.children) > 0:
                curr_level.extend([node.tag for node in curr_node.children])
                for child_node in curr_node.children:
                    queue.append(child_node)
                print(curr_level)

    def extract_tags(self):
        def dfs(curr_node):
            if len(curr_node.children) == 0:
                xml_tag = f"<{curr_node.tag}></{curr_node.tag}>"
                self.xml_data.append(xml_tag)
                return xml_tag

            child_nodes = []
            for child in curr_node.children:
                child_nodes.append(dfs(child))

            children = "".join(child_nodes)
            xml_tag = f"<{curr_node.tag}>{children}</{curr_node.tag}>"
            self.xml_data.append(xml_tag)
            return xml_tag

        curr_node = self.root_node
        dfs(curr_node)
        print(self.xml_data)


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

    parseTreeObj = ParseTree(xml_string)
    parseTreeObj.build_tree()
    # parseTreeObj.print_tree()
    parseTreeObj.extract_tags()
