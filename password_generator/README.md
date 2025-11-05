# Password Generator

This repository contains two simple implementations of a secure password generator:

1. **Python (Tkinter)** - `python_app/main.py`
   - Uses Python's `secrets` module for cryptographically secure random passwords.
   - GUI built with Tkinter.
   - Optional clipboard support using `pyperclip`.

2. **Web (HTML/JavaScript)** - `web_app/index.html`
   - Uses the Web Crypto API for secure random values.
   - Simple responsive UI with copy-to-clipboard.

## Usage

### Python
1. Install dependencies:
```
pip install -r python_app/requirements.txt
```
2. Run:
```
python python_app/main.py
```

### Web
Open `web_app/index.html` in your browser. No server required.

## Files
- `python_app/main.py` - Tkinter GUI application (Python 3).
- `web_app/index.html`, `web_app/script.js`, `web_app/style.css` - Web version.