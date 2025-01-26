from flask import Flask, request, jsonify
from nerfstudio_commands import run_nerfstudio, render_camera_path
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test erfolgreich!"}), 200

@app.route('/api/status', methods=['POST'])
def handle_status():
    """
    Empfängt den Status vom Backend und führt Aktionen basierend darauf aus.
    """
    try:
        data = request.get_json()
        status = data.get("status")
        message = data.get("message")
        
        print(f"Empfangene Daten: {data}")
        if status == "completed":
            run_nerfstudio()
            return jsonify({"success": True, "message": "Aktion wurde ausgeführt."}), 200
        elif status == "error":
            print(f"Fehler empfangen: {message}")
            return jsonify({"success": False, "message": "Fehler wurde verarbeitet."}), 200
        else:
            return jsonify({"success": False, "message": "Unbekannter Status."}), 400
    except Exception as e:
        print(f"Fehler bei der Verarbeitung der Anfrage: {e}")
        return jsonify({"success": False, "message": "Fehler bei der Anfrage-Verarbeitung."}), 500

@app.route('/api/path_render', methods=['POST'])
def handle_path_render():
    try:
        data = request.get_json()
        path = data.get("path")
        nerfstudio_paths = data.get("nerfstudio_paths")

        render_camera_path(path, nerfstudio_paths)
        return jsonify({"success": True}), 200
    except Exception as e:
        print(f"Error receiving request: {e}")
        return jsonify({"success": False}), 500    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
