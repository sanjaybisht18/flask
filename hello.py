from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_input():
    # Get the input from the request's JSON body
    data = request.get_json()

    if 'body' not in data:
        return jsonify({'error': 'Missing "body" parameter'}), 400

    input_text = data['body']
    response_text = f"{input_text}, all good"

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)

