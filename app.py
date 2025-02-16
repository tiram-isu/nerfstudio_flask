from flask import Flask, request, jsonify
from nerfstudio_commands import render_camera_path

app = Flask(__name__)

@app.route('/api/path_render', methods=['POST'])
def handle_path_render():
    """
    Get data from POST request and render camera path using Nerfstudio.
    """
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
