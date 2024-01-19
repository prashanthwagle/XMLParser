from collections import deque
import re


class TreeNode:
    def __init__(self, tag):
        self.tag = tag
        self.children = []
        self.parent = None
        self.is_self_closing = False
        self.contents = ""


class ParseTree:
    def __init__(self, xml_string):
        self.stack = []
        self.root_node = None
        self.curr_node = None
        self.xml_string = xml_string
        self.xml_data = []
        self.metadata = {"title": None, "description": None,
                         "author": None, "creationDate": None}

    def __standardize_json(self, ip_dict):
        """
        Logic to standardize json
        """
        for key, value in ip_dict.items():
            if isinstance(value, str) and value == "":
                ip_dict[key] = None
        return ip_dict

    def __clean_tags(self, tag):
        """
        Logic to clean tags aka remove whitespaces and attributes of tags (maybe attributes can be a part of treenodes in the future)
        """
        match = re.search(r"\s+", tag)
        if match:
            tag = tag[:match.start()]
        return tag

    # TODO: Metadata should only be captured if it is present in the <header> tag i.e., header should be present in the stack
    def build_tree(self):
        current_tag = ""
        capturing_metadata = False
        metadata_contents = ""
        for char in self.xml_string:
            if char == '<':
                if capturing_metadata:
                    capturing_metadata = False
                    # ErrorCheck if this field has already been filled (duplicate metadata)
                    self.metadata[current_tag] = metadata_contents
                    metadata_contents = ""
                current_tag = ""
                # ErrorCheck: What if metadata is already filled?

                # If metadata has already been captured, and you encounter a closing tag

            elif char == '>':
                # If metadata is yet to be captured (current tag is an opening tag)
                if current_tag not in self.stack and current_tag in self.metadata:
                    capturing_metadata = True

                # ErrorCheck: What if metadata is already filled?
                # if current_tag in self.metadata:
                #     # capturing_metadata = not capturing_metadata
                #     self._handle_tag(current_tag)
                #     metadata_contents = ""
                self._handle_tag(current_tag)
            else:
                if capturing_metadata == True:
                    metadata_contents += char
                else:
                    current_tag += char

    # TODO Abstact all regexes
    def _handle_tag(self, tag):
        if "section" in tag and "sectionTitle" not in tag:
            print("Reached Section")

        if tag.startswith('!') and bool(re.search(r'!--(.*?)--', tag, re.DOTALL)):
            return

        if tag.startswith('/'):
            self._handle_closing_tag(self.__clean_tags(tag[1:]))
        elif len(tag) > 3 and tag[-1] == "/":
            self._handle_self_closing_tag(self.__clean_tags(tag[:-1]))
        else:
            self._handle_opening_tag(self.__clean_tags(tag))

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
        new_node.is_self_closing = True
        self.curr_node.children.append(new_node)
        new_node.parent = self.curr_node
        self.curr_node = new_node

    def _handle_closing_tag(self, tag):
        # if len(metadata_contents) > 0 and tag in self.metadata:
        #     # ErrorCheck if this field has already been filled (duplicate metadata)
        #     self.metadata[tag] = metadata_contents

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
                if curr_node.is_self_closing:
                    xml_tag = f"<{curr_node.tag}/>"
                else:
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
        return self.__standardize_json({"title": self.metadata["title"], "description": self.metadata["description"],
                                        "author": self.metadata["author"], "xml_data": self.xml_data, "created_at": self.metadata["creationDate"]})


# TODO: Handle for  <?xml version="1.0" encoding="UTF-8"?>
if __name__ == "__main__":
    xml_string = """
            <legalDocument>
                <header>
                    <title></title> <!-- Empty title -->
                    <meta>
                        <author>Author: Jane Doe</author>
                        <creationDate></creationDate> <!-- Missing creation date -->
                    </meta>
                </header>
                <body>
                    <section>
                        <title>Background</title>
                        <!-- Missing content section -->
                        <undefinedTag>Some undefined content</undefinedTag>
                    </section>
                    <ambiguous>
                        <content>Initial <b>content</b> with <i>tags</i></content>
                        <content> <!-- Nested content tags with missing information -->
                            <subContent></subContent> <!-- Empty subcontent -->
                            More text here
                            <subContent>
                                <p>Paragraph inside subcontent</p>
                            </subContent>
                        </content>
                        <undefinedStructure>
                            Irregular formatting and structure
                            <randomTag>Random information</randomTag>
                        </undefinedStructure>
                    </ambiguous>
                    <conclusion>
                        <summary>
                            <point>This is a summary point</point>
                            <!-- Missing summary point -->
                        </summary>
                        <finalThoughts></finalThoughts> <!-- Empty final thoughts -->
                    </conclusion>
                </body>
                <attachments>
                    <file>attachment1.pdf</file>
                    <!-- Missing file tag -->
                    <file>attachment3.docx</file>
                </attachments>
                <!-- Missing footer -->
            </legalDocument>
                """

    parseTreeObj = ParseTree(xml_string)
    parseTreeObj.build_tree()
    # parseTreeObj.print_tree()
    print(parseTreeObj.extract_tags())
