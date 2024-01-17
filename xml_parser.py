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
        pass


if __name__ == "__main__":
    xml_string = """
<?xml version="1.0" encoding="UTF-8"?>
<legalDocument>
    <title>Title of Document</title>
    <description>Description of Legal Matter</description>
    <author>Author Name</author>
    <creationDate></creationDate>
    <content>
        <section>
            <sectionTitle>Introduction</sectionTitle>
            <paragraph>This is the introductory paragraph of the legal document.</paragraph>
        </section>
        <section>
            <sectionTitle>Background</sectionTitle>
            <paragraph>The background section provides context to the legal matter.</paragraph>
        </section>
        <section>
            <sectionTitle>Legal Analysis</sectionTitle>
            <subSection>
                <subSectionTitle>Analysis Part 1</subSectionTitle>
                <paragraph>Details of the first part of the legal analysis. Creation date is January 22, 2022.</paragraph>
            </subSection>
            <subSection>
                <subSectionTitle>Analysis Part 2</subSectionTitle>
                <paragraph>Details of the second part of the legal analysis.</paragraph>
            </subSection>
        </section>
        <section>
            <sectionTitle>Conclusion</sectionTitle>
            <paragraph>Concluding remarks and final thoughts on the legal matter.</paragraph>
        </section>
    </content>
</legalDocument>
    """

    parseTreeObj = ParseTree(xml_string)
    parseTreeObj.build_tree()
    parseTreeObj.print_tree()
