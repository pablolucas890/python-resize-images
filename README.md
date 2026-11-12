# Python Resize Images

Batch-resize images from a folder. Drop files into `in/`, run one command, and pick up the results from `out/`.

## Requirements

- Python 3.10 or newer
- [Pillow](https://python-pillow.github.io)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with `.venv\Scripts\activate`.

## Usage

1. Put your images in the `in/` folder.
2. Run:

```bash
python main.py 800 600
```

`800` is the width and `600` is the height, both in pixels. Every supported image in `in/` is resized to that exact size and saved in `out/` with the same file name.

```
.
├── in/                 # put images here
├── out/                # resized images appear here
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

Supported formats: PNG, JPG, JPEG, WEBP, BMP, and TIFF.

Show the built-in help with:

```bash
python main.py --help
```

## License

MIT. See [LICENSE](LICENSE).
