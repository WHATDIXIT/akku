# Happy Birthday My Baby 💖 — Web App

A cute, pink & red love-themed Streamlit website made for a special birthday surprise!

## What it does
1. **Welcome page** — "Happy Birthday My Baby!" with a pointer telling her to tap **Thank You**.
2. **Memory gallery** — your photos appear one by one with sweet captions, followed by your video.
3. **The big question** — "Do you love me?" with **Yes** and **No** buttons. The **No** button keeps
   jumping to a new spot every time it's clicked, until she finally taps **Yes**.
4. **Final surprise** — a heartfelt love message + balloons 🎈

---

## How to put this online so anyone with a link can open it (FREE)

The easiest way is **Streamlit Community Cloud** (free hosting by Streamlit).

### Step 1 — Create a GitHub account & repository
1. Go to [github.com](https://github.com) and sign up (if you don't already have an account).
2. Click **New repository** → name it something like `birthday-surprise`.
3. Set it to **Public** (required for the free Streamlit plan) and click **Create repository**.

### Step 2 — Upload these files
Upload the **entire contents of this folder** to your new repo, keeping the same structure:

```
your-repo/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── assets/
    ├── images/
    │   ├── img01.jpg ... img14.jpg
    └── video/
        └── our_memory.mp4
```

You can do this by:
- Clicking **Add file → Upload files** on GitHub and dragging the whole folder in (do it in a
  couple of batches if it complains about size — GitHub allows files up to 25MB each, and
  everything here is well under that), **or**
- Using GitHub Desktop / git command line if you're comfortable with that.

### Step 3 — Deploy on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
2. Click **"New app"**.
3. Choose your repository, branch (`main`), and set the main file path to `app.py`.
4. Click **Deploy**.
5. Wait a minute while it installs and builds — then you'll get a public link like:
   `https://your-app-name.streamlit.app`

### Step 4 — Share the love!
Send that link to your girlfriend on **16th June** 💌. Anyone with the link can open it on
their phone or laptop — no login or app install needed.

---

## Running it locally (optional, to preview first)
If you have Python installed on your computer:

```bash
pip install -r requirements.txt
streamlit run app.py
```

It will open in your browser at `http://localhost:8501`.

---

## Customizing
- **Captions**: edit the `CAPTIONS` list near the top of `app.py` — one caption per photo, in order.
- **Final message**: edit the text inside the `final-message` div in the "STAGE 4" section.
- **Photos/video order**: rename files in `assets/images/` (img01.jpg → img14.jpg) and
  `assets/video/our_memory.mp4` to change order or swap media. Keep the same names so the
  app finds them, or update the filenames referenced in `app.py`.
- **Colors**: tweak the gradient and colors in the `<style>` block (search for `#ff8fab`,
  `#d6336c`, etc.) or in `.streamlit/config.toml`.

Happy Birthday to her! 🎂💕
