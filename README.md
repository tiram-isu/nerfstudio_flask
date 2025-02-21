# 3D Gaussian Splatting Path Rendering
This repository provides a Flask server that receives motion planning paths via HTTP and renders them using Nerfstudio. It is designed to work alongside the `ompl_path_planning` repository, which generates paths using OMPL.

# Prerequisites
- **Conda**  
- **Nerfstudio** `1.1.5`
- **Flask** `3.0.3`

# Installation
- Create conda environment named `nerfstudio`.
- Install Nerfstudio in this environment following the [installation guide](https://docs.nerf.studio/quickstart/installation.html).

# Usage
Start the Flask server:
```bash
python app.py
```
