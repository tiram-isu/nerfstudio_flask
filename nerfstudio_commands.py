import subprocess
import re

checkpoint_path = "nerfstudio_output/trained_model/colmap_data/splatfacto/2024-12-01_175414/config.yml"
output_path = "renders/"


def run_nerfstudio():
    commands = f'conda activate nerfstudio && \
    cd D:/Thesis/Stonehenge_new/stonehenge/ && \
    ns-export gaussian-splat --load-config {checkpoint_path} --output-dir {output_path}'

    try:
        subprocess.run(commands, shell=True, check=True)  # Use cmd.exe for Windows
        print("Export completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during export: {e}")

    #ns-render camera-path
    # --load-config nerfstudio_output\trained_model\colmap_data\splatfacto\2024-12-01_175414\config.yml
    # --camera-path-filename D:\Thesis\Stonehenge_new\stonehenge\colmap_data\camera_paths\PDST.json
    # --output-path renders/colmap_data/PDST.mp4

def render_camera_path(path, nerfstudio_paths):
    # extract path name without extension
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
