from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify({"message": "Hello from Backend API!", "status": "success"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)