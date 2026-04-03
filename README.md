# 🌌 Conflict Management Website
**Peehu Gupta — 25BAI0056**

---

## 📁 Folder Structure

```
conflict_management/
│
├── app.py                  ← Main Flask file (RUN THIS)
├── requirements.txt        ← Python packages needed
│
├── templates/
│   ├── base.html           ← Shared layout (bg, nav, fonts)
│   ├── home.html           ← Home page with 3 widgets
│   ├── written.html        ← Essay page
│   ├── visual.html         ← Image gallery page
│   └── audio.html          ← Audio page
│
└── static/
    ├── images/
    │   ├── bg.jpg                  ← Background wallpaper
    │   ├── img1_perspectives.png
    │   ├── img2_6or9.png
    │   ├── img3_puzzle.png
    │   ├── img4_thomas.png
    │   ├── img5_confusion.png
    │   ├── img6_competing.png
    │   └── img7_strength.png
    └── audio/              ← DROP YOUR AUDIO FILES HERE (create this folder)
```

---

## 🚀 How to Run (Step by Step)

### 1. Open VS Code
Open the `conflict_management` folder in VS Code.

### 2. Open the Terminal
Press `` Ctrl + ` `` (backtick) to open the terminal.

### 3. Install Flask
```bash
pip install flask
```

### 4. Run the App
```bash
python app.py
```

### 5. Open in Browser
Go to: **http://127.0.0.1:5000**

That's it! 🎉

---

## 🎧 How to Add Audio

1. Create a folder: `static/audio/`
2. Drop your `.mp3` file inside (e.g., `my_audio.mp3`)
3. Open `templates/audio.html`
4. Find the placeholder track and replace with:
```html
<audio controls>
  <source src="/static/audio/my_audio.mp3" type="audio/mpeg">
</audio>
```

---

## 🛠 Editing Tips

- **Change text content** → Edit the `.html` files in `/templates/`
- **Change colors/fonts** → Edit the CSS in `base.html` under `:root { ... }`
- **Add more images** → Drop them in `/static/images/` and add a card in `visual.html`
