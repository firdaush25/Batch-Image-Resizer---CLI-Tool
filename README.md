---

## 🖼️ Batch Image Resizer – CLI Tool using Pillow

![GitHub repo size](https://img.shields.io/github/repo-size/firdaush25/Batch-Image-Resizer)
![GitHub stars](https://img.shields.io/github/stars/your-username/Batch-Image-Resizer?style=social)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License](https://img.shields.io/github/license/your-username/Batch-Image-Resizer)

Resize all images in a folder to a fixed dimension via a lightweight and customizable CLI tool. Built with Pillow, clean logic, and portfolio-ready organization.

---

### ✨ Features

- 📁 Resize multiple image formats (.png, .jpg, .jpeg)
- 🧠 Uses LANCZOS for high-quality resampling
- 🔧 Auto-creates output folder if missing
- 🏷️ Adds `_resized` suffix to all filenames
- 🧼 Easy integration with other image tools

---

### 🚀 Getting Started

#### ✅ Prerequisites

```bash
pip install Pillow
```

#### 🔗 Run the Script

```bash
python Image_resizer.py <source_folder> <destination_folder> <width> <height>
```

#### 📌 Example

```bash
python Image_resizer.py images/ output/ 300 300
```

This resizes every image in `images/` to 300x300 pixels and saves them in `output/`.

---

### 🧩 Code Breakdown

| Function                        | Description                                              |
|-------------------------------|----------------------------------------------------------|
| `resize_single_image()`       | Resizes one image, handles errors, saves to destination |
| `resize_images_in_directory()`| Iterates through folder, applies `resize_single_image()`|

---

### 🧠 Time Complexity

| Function                     | Complexity |
|-----------------------------|------------|
| `resize_single_image`       | O(1)       |
| `resize_images_in_directory`| O(n)       |

Where `n` is the number of image files.

---

### 📁 File Structure

```
Batch-Image-Resizer/
│
├── Image_resizer.py
├── images/                  # Source images
├── output/                  # Resized images output
└── README.md
```

---

### 📸 Sample Output

<img width="1919" height="595" alt="image" src="https://github.com/user-attachments/assets/e077b94c-cf2c-439b-a92f-160238c63eab" />


### 🔮 Future Upgrades

- ✅ Add aspect ratio support
- ✅ Preserve original formats
- ✅ Handle unusual image modes (e.g. RGBA, CMYK)
- ✅ Add tqdm progress bar and logging

---

### 👤 Author

**👨‍💻 Firdaush Alam**  
Python Developer Intern @ BroskiesHub  
Computer Science Engineering Student @ SECAB Institute of Engineering & Technology  
🚀 Passionate about real-world tools, clean code, and professional documentation.

---
