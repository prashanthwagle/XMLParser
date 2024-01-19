from flask import Flask, request, jsonify
import os
from xml_parser import ParseTree

app = Flask(__name__)
DIRECTORY = "xml_files"


@app.route('/', methods=['GET'])
def get_data():
    id_param = request.args.get('id')
    if id_param is None or not id_param.isdigit():
        return jsonify({'error': 'Invalid or missing id parameter'}), 400
    id = int(id_param)

    filename = f"doc_{id}_xml.xml"

    print(filename)

    filepath = os.path.join(os.getcwd(), DIRECTORY, filename)
    print(filepath)
    if not os.path.exists(filepath):
        return jsonify({'error': f'XML File with id {id} does not exist'}), 404

    with open(filepath, 'r') as xml_file:
        xml_string = xml_file.read()
        parseTreeObj = ParseTree(xml_string)
        parseTreeObj.build_tree()
        result = parseTreeObj.extract_tags()

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
