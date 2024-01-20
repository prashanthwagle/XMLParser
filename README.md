# XMLParser

## Files

- xml_parser.py: The core logic to parse the XML files and build the tree structure

  - Class TreeNode: Class to create a node of the XML tree
  - Class ParseTree: A class to parse the XML string
    - build_tree(): Given an XML string, it builds a tree with the help of several helper functions such as \_handle_tag
    - print_tree(); Prints the tree structure (level order traversal)
    - extract_tags(): Traverses through the built tree and extracts xml_data using Depth First Search

- unit_tests.py: A list of unit tests to verify the working of xml_parser.py

- app.py: the flask server which invokes xml_parser.py and delivers the result

-run_app.py: Runs the flask server on port 3456, as per the requirements

# How to run the server

Make sure you have python3 installed
Run `python3 app.py` on UNIX-based systems OR
Run `python app.py` on Windows

# Error Logging

Errors are logged to the terminal. The errors and warnings are described in xml_parser.py
