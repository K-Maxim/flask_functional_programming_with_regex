import os

from flask import Flask, request, abort, Response

from utils import build_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST', 'GET'])
def perform_query() -> Response:
    cmd_1 = request.args.get('cmd_1')
    value_1 = request.args.get('value_1')
    cmd_2 = request.args.get('cmd_2')
    value_2 = request.args.get('value_2')
    file_name = request.args.get('file_name')

    if not (cmd_1 and value_1 and cmd_2 and value_2 and file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400)

    with open(file_path, 'r') as file:
        data = build_query(cmd_1, value_1, file)

        if cmd_2 and value_2:
            data = build_query(cmd_2, value_2, iter(data))

    return app.response_class(data, content_type="text/plain")
    # нужно взять код из предыдущего ДЗ !!!DONE!!!
    # добавить команду regex
    # добавить типизацию в проект, чтобы проходила утилиту mypy app.py


if __name__ == '__main__':
    app.run(debug=True, port=5001)