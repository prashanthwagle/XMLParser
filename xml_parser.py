

class TreeNode:
    def __init__(self, tag):
        self.tag = tag
        self.children = []
        self.parent = None


        if tag.startswith('/'):
            handle_closing_tag(tag[1:])
        elif len(tag) > 3 and tag[-2] == "/":
            handle_self_closing_tag(tag[1:-2])
        else:
            handle_opening_tag(tag)

    def handle_opening_tag(tag):
        stack.append(tag)
        print("Opening tag", stack)

    def handle_self_closing_tag(tag):
        print("Self Closing tag", stack)

    def handle_closing_tag(tag):
        if stack and stack[-1] == tag:
            print("Closing tag", stack)
            stack.pop()
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
