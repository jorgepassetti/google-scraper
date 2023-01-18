from flask import Flask, jsonify, request
from googlesearch import search

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_google():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No search query provided'}), 400
    results = search(query, num_results=10)
    return jsonify([result.link for result in results])

if __name__ == '__main__':
    app.run(debug=True)