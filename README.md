# XMLParser

## Files

- xml_parser.py: The core logic to parse the XML files and build the tree structure

  - Class `TreeNode`: Class to create a node of the XML tree
  - Class `ParseTree`: A class to parse the XML string
    - `build_tree()`: Given an XML string, it builds a tree with the help of several helper functions such as \_handle_tag
    - `print_tree()`: Prints the tree structure (level order traversal)
    - `extract_tags()`: Traverses through the built tree and extracts `xml_data`using Depth First Search

- `unit_tests.py`: A list of unit tests to verify the working of `xml_parser.py`

- `app.py`: the flask server which invokes `xml_parser.py` and delivers the result

- `run_app.py`: Runs the flask server on port 3456, as per the requirements

# How to run the server

## First things first

Download this repository to a folder. You should have a folder XMLParser in your machine.

## Install Prerequisites

Install Python 3 and pip

## After installation of prerequisites

Navigate to the folder XMLParser via terminal
Run `python3 run_server.py` on UNIX-based systems OR
Run `python run_server.py` on Windows

# Error Logging

Errors are logged to the terminal. The errors and warnings are described in `xml_parser.py`

# Future work

- For now the errors and warnings are logged. Robust exception handling mechanisms should be introduced
  - For now, due to lack of time, I have focused on catching the errors but not on handling them
- Logging the data should enable insights and some sort of visualization
- Standardizing the error logs and connecting it to a database like Elasticache would enable better insights for the future
- Need to integerate it with some kind of a database so that the document is parsed only once and not on every request
