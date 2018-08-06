import json
from flask import Flask, jsonify, request

from utils import has_all_alphabet


app = Flask('text_service')

def alphacheck(version, query):
    try:
        case_insensitive = json.loads(
            request.args.get('case_insensitive', 'false')
        )
    except json.JSONDecodeError:
        case_insensitive = False

    return jsonify({
        'response': has_all_alphabet(
            query,
            version=version,
            case_insensitive=case_insensitive
        ),
    })

@app.route('/alphacheck/v1/<string:query>', methods=['GET'])
def alphacheck_v1(query):
    return alphacheck('v1', query)

@app.route('/alphacheck/v2/<string:query>', methods=['GET'])
def alphacheck_v2(query):
    return alphacheck('v2', query)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True)
