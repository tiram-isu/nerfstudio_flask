import subprocess
import re

def render_camera_path(path, nerfstudio_paths):
    """
    Render camera path using Nerfstudio.
    Requires conda environment "nerfstudio" with Nerfstudio installed.
    """
    pattern = r"([^/]+)(?=\.json$)"
    match = re.search(pattern, path)

    command = f'conda activate nerfstudio && \
    cd {nerfstudio_paths["nerfstudio_base_dir"]} && \
    ns-render camera-path \
    --load-config {nerfstudio_paths["checkpoint_path"]} \
    --camera-path-filename {path} \
    --output-path {nerfstudio_paths["output_dir"] + f"/{match.group()}.mp4"}'

    try:
        subprocess.run(command, shell=True, check=True)
        print("Rendering completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during rendering: {e}")
