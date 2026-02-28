from pathlib import Path

BASE_DIR = Path("lab-vc")

structure = [
    "notebooks",
    "src/io",
    "src/preprocessing",
    "src/utils",
    "data/raw",
    "data/processed",
    "docs",
    "scripts"
]

files = {
    "src/__init__.py": "",
    "src/io/__init__.py": "",
    "src/preprocessing/__init__.py": "",
    "src/utils/__init__.py": "",
    "data/README.md": "# Data directory\n\nDatasets não versionados.",
    "README.md": "# Lab-VC — Laboratório de Visão Computacional",
    "requirements.txt": "numpy\nopencv-python\nPillow\nmatplotlib\nscikit-image\ntqdm\n",
    ".gitignore": "__pycache__/\n.ipynb_checkpoints/\ndata/raw/\ndata/processed/\n"
}

for folder in structure:
    (BASE_DIR / folder).mkdir(parents=True, exist_ok=True)

for file, content in files.items():
    file_path = BASE_DIR / file
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")

print("✅ Estrutura do Lab-VC criada com sucesso!")
