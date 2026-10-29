# Quick Start Guide - Sea 🌊

Get up and running in 5 minutes! Sea now uses Claude AI to answer ANY question.

## What You Need

1. Python 3.8+ installed
2. A free Claude API key (2-minute setup)

## Step 0: Get Claude API Key (2 minutes)

1. Go to: https://console.anthropic.com/ and sign up (free!)
2. Click "API Keys" → "Create Key"
3. Copy your key (starts with `sk-ant-`)

**Keep this key secret!**

## Windows

### Step 1: Install Python
- Download from: https://www.python.org/downloads/
- **Important:** Check "Add Python to PATH" during installation

### Step 2: Set Your API Key
Open PowerShell and run:
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-YOUR-KEY-HERE"
```

Replace `sk-ant-YOUR-KEY-HERE` with your actual key from Step 0.

### Step 3: Install Dependencies
In the `sea_app` folder, open PowerShell and run:
```bash
pip install -r requirements.txt
```

### Step 4: Run the App
In the same PowerShell window (where you set the API key):
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`!

---

## macOS / Linux

### Step 1: Install Python (if not already installed)
```bash
# macOS with Homebrew:
brew install python3

# Or download from: https://www.python.org/downloads/
```

### Step 2: Set Your API Key
```bash
export ANTHROPIC_API_KEY="sk-ant-YOUR-KEY-HERE"
```

Replace `sk-ant-YOUR-KEY-HERE` with your actual key from Step 0.

### Step 3: Create Virtual Environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`!

---

## Troubleshooting

### "Python not found"
- Install Python from https://www.python.org
- Make sure to check "Add Python to PATH"
- Restart your terminal

### "streamlit: command not found"
```bash
pip install streamlit
```

### "Module not found"
```bash
pip install -r requirements.txt
```

### App won't start
- Make sure you're in the `sea_app` directory
- Check that all Python dependencies are installed
- Try: `pip install --upgrade streamlit`

---

## Using the App

1. **Register** with your name, age, and Gmail
2. **Login** with your Gmail address
3. **Ask questions** - any topic!
4. **Read the explanation** - tailored to your age
5. **Answer the guiding questions** - think deeply!

---

## Example Questions to Try

- "How does photosynthesis work?"
- "What is gravity?"
- "How do I solve algebra equations?"
- "Why is the sky blue?"
- "How do magnets work?"

Enjoy learning! 🌊
