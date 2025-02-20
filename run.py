# # run.py
# from app import app

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Flask app is running!"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from app.ai.resume_parser import parse_resume

app = Flask(__name__)

@app.route('/parse-resume', methods=['POST'])
def parse_resume_endpoint():
    file = request.files['resume']
    parsed_data = parse_resume(file)
    return jsonify(parsed_data)

if __name__ == '__main__':
    app.run(debug=True)

