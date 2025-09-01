# 🛡 Helmet-Detection

## Overview  
This project implements a helmet detection system using **YOLOv3** and **OpenCV**.  
It allows users to upload images, detect helmets, and view results with annotated outputs via a simple web interface.

---

## Repository Structure  

```

.
├── Code With Description.pdf           # Project documentation
├── app.py                             # Core detection application
├── yolov3.cfg                         # YOLOv3 configuration file
├── static/                            # Images, CSS styles
│   ├── \*.jpg / \*.webp / *.png
│   └── styles.css
├── templates/                         # Frontend HTML
│   └── index.html
└── runs/detect/                       # Training run configs
└── train*/args.yaml

````

---

## Getting Started  

### Prerequisites  
- Python 3.7+  
- pip package manager  

### Installation  
```bash
git clone https://github.com/HariN999/Helmet-Detection.git
cd Helmet-Detection
pip install -r requirements.txt
````

### Configuration

* Download the YOLOv3 weights file (`yolov3.weights`) from the official source.
* Place it in the project root directory (same location as `yolov3.cfg`).

### Running the Application

```bash
python app.py
```

Then open your browser at:

```
http://localhost:5000
```

---

## Features

* **Helmet Detection** using YOLOv3
* **Web Interface** for uploading and analyzing images
* **Configurable & Extendable** design for future improvements

---

## Contributing

1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push and open a Pull Request

👉 Do you want me to also prepare a **requirements.txt** file for your repo so others can set it up without guessing dependencies?
```
