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

    def __is_meta_data(self, tag):
        """
        My logic of checking if a tag is a metadata tag or not
        Either it should be a direct child of legalDocument or it should be nested in the header tag
        """
        return True if 'header' in self.stack or len(self.stack) == 1 else False

    # TODO: Metadata should only be captured if it is present in the <header> tag i.e., header should be present in the stack

    def build_tree(self):
        current_tag = ""
        capturing_metadata = False
        metadata_contents = ""

        for char in self.xml_string:
            if char == '<':
                if capturing_metadata:
                    # If the metadata tags is nested in the header tag, only then consider it as metadata
                    capturing_metadata = False
                    # TODO: ErrorCheck if this field has already been filled (duplicate metadata)
                    self.metadata[current_tag] = metadata_contents
                    metadata_contents = ""
                current_tag = ""
                # TODO: ErrorCheck: What if metadata is already filled?

                # If metadata has already been captured, and you encounter a closing tag

            elif char == '>':
                # If metadata is yet to be captured (current tag is an opening tag)
                if current_tag not in self.stack and current_tag in self.metadata:
                    capturing_metadata = True and self.__is_meta_data(
                        current_tag)

                # TODO: ErrorCheck: What if metadata is already filled?
                self._handle_tag(current_tag)
            else:
                if capturing_metadata == True:
                    metadata_contents += char
                else:
                    current_tag += char

    # TODO Abstact all regexes
    def _handle_tag(self, tag):
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
        # TODO: ErrorCheck if this field has already been filled (duplicate metadata)
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
                <title>Complex Legal Document</title>
                <meta>
                    <author>John Smith</author>
                    <co-author>Emily Johnson</co-author>
                    <creationDate>2024-04-01</creationDate>
                </meta>
            </header>
            <body>
                <section id="1">
                    <title>Introduction</title>
                    <content>Overview of the document's purpose.</content>
                    <note>Some notes <highlight>with <b>mixed</b> formatting</highlight> inside.</note>
                </section>
                <section id="2">
                    <title>Background</title>
                    <content>
                        <paragraph>Background information with <inlineTag>various</inlineTag> inline elements.</paragraph>
                        <list>
                            <item>Point 1</item>
                            <item>Point 2 with <b>bold</b> text</item>
                        </list>
                    </content>
                </section>
                <content>
                    <mixedContent>
                        This is <b>mixed</b> content outside a <normalTag>regular tag structure</normalTag>.
                        <moreContent>
                            More nested content with <a href="http://example.com">links</a> and other elements.
                        </moreContent>
                    </mixedContent>
                </content>
                <section id="3">
                    <title>Conclusion</title>
                    <content>
                        <conclusion>
                            Final thoughts and <unusualTag>remarks</unusualTag>.
                        </conclusion>
                    </content>
                    <attachments>
                        <file>attachment1.pdf</file>
                        <file>attachment2.jpg</file>
                        <file>attachment3.docx</file>
                    </attachments>
                </section>
            </body>
            <footer>
                <comments>
                    <comment>First comment</comment>
                    <comment>Second comment with <b>bold</b> text</comment>
                </comments>
            </footer>
        </legalDocument>
            """

    parseTreeObj = ParseTree(xml_string)
    parseTreeObj.build_tree()
    # parseTreeObj.print_tree()
    print(parseTreeObj.extract_tags())
