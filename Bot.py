from flask import Flask, request, Response
import json

app = Flask(__name__)

latest_announcement = ""

@app.route('/announce', methods=['POST'])
def announce():
    global latest_announcement
    data = request.get_json()
    message = data.get('message')
    if not message:
        return Response(json.dumps({"error": "message is required"}, ensure_ascii=False), mimetype='application/json'), 400
    latest_announcement = message
    print(f"새 공지: {message}")
    return Response(json.dumps({"status": "success"}, ensure_ascii=False), mimetype='application/json')

@app.route('/announce', methods=['GET'])
def get_announce():
    response = Response(json.dumps({"message": latest_announcement}, ensure_ascii=False), mimetype='application/json')
    return response

if __name__ == '__main__':
    app.run(debug=True)