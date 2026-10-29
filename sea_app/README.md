# 🌊 Sea - Claude's Brother

**Sea** is Claude's brother - an AI-powered educational app that helps YOU learn by answering ANY question and asking guiding questions in an age-appropriate way. Think of me as your supportive older/younger brother who loves teaching! 👨‍👦

## Features

- 👤 **User Authentication** - Login with Gmail (3-99 years old)
- 🤖 **Claude AI Tutor** - Answers ANY question (math, science, history, coding, languages, etc.)
- 🎯 **Direct Answers** - Gets straight to the point, then explains deeper
- 🎓 **Age-Appropriate Content** - Teaching style adapts to student age (3 to 99)
- 💡 **Socratic Teaching** - Guides students to discover understanding, not memorize
- 📚 **Real Conversation** - Interactive chat-like learning experience
- 💾 **Question History** - Keep track of what you've learned
- 📦 **Automatic Backups** - Data is safe, even after app resets
- 🔄 **Re-login with Same Email** - After an upgrade, just register with your email again

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this project**
   ```bash
   cd sea_app
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Claude API key**
   
   Get a free API key from: https://console.anthropic.com/
   
   On Windows (PowerShell):
   ```powershell
   $env:ANTHROPIC_API_KEY = "sk-ant-..."
   ```
   
   On macOS/Linux:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```
   
   See [SETUP_API.md](SETUP_API.md) for detailed instructions.

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

### First Time?
1. Click the **Register** tab
2. Enter your name, age (3-99), and Gmail address
3. Click "Register"

### Returning Users?
1. Click the **Login** tab
2. Enter your Gmail address
3. Click "Login"

### Asking Questions
1. Type your question (anything - math, science, coding, history, languages, etc.)
2. Click "Start Learning"
3. Sea explains the concept in your age level
4. You answer the follow-up question
5. Get feedback and the next question
6. Keep learning until you understand!

**New:** Sea now uses Claude AI to answer ANY question properly!

## What Sea Can Help With

Sea can answer and explain **ANY topic**, including:
- 🧮 **Math** - Algebra, geometry, calculus, statistics
- 🔬 **Science** - Biology, chemistry, physics, astronomy
- 📚 **Literature** - Books, writing, grammar, languages
- 🌍 **History & Geography** - Countries, events, cultures
- 💻 **Technology & Coding** - Python, JavaScript, web development
- 🎨 **Arts** - Music, drawing, design
- 🏃 **Sports** - Rules, techniques, history
- 💪 **Health & Fitness** - Nutrition, exercise, wellness
- **And anything else students are curious about!**

## Age Groups

- **Young Child (3-7)** - Simple explanations with familiar examples
- **Child (8-12)** - Structured learning with clear steps
- **Teen (13-17)** - Detailed concepts with connections
- **Adult (18+)** - Advanced topics and deep explanations

## Example Questions to Try

Sea can answer ANY question! Try:
- **Math:** "What is 1+1?", "How do I solve 2x + 3 = 11?", "What is the Pythagorean theorem?"
- **Science:** "How does photosynthesis work?", "What is gravity?", "Why is the sky blue?"
- **History:** "When was the moon landing?", "Who was Napoleon?", "What caused World War 2?"
- **Languages:** "How do you say hello in Spanish?", "What's the past tense of 'go'?"
- **Coding:** "What's a loop in programming?", "How do I use loops in Python?"
- **Anything else:** Ask about sports, art, technology, animals, space, cooking... anything!

## Project Structure

```
sea_app/
├── app.py              # Main Streamlit app (user interface)
├── auth.py             # Authentication & login validation
├── database.py         # SQLite user data management
├── ai_tutor.py         # Claude AI integration for teaching
├── teaching.py         # Teaching session coordination
├── content.py          # Educational content (legacy)
├── requirements.txt    # Python dependencies
├── SETUP_API.md        # API key setup instructions
├── README.md           # This file
└── .streamlit/
    └── config.toml     # Streamlit theme configuration
```

## Data & Backups

### Database
Sea uses SQLite to store:
- User profiles (name, age, email)
- Question history and responses
- Login timestamps

The database file (`sea_users.db`) is created automatically in the app folder.

### Automatic Backups 🔄
- **Backups created automatically** every time the app starts
- **Manual backups** via Settings → "Create Manual Backup"
- **Up to 5 recent backups** kept in the `/backups/` folder
- **Complete data protection** - if the app resets, you can restore!

### If You Lose Your Account
If the database gets deleted during an app upgrade:
1. **Option 1:** Restore from backup (Settings → View Backups)
2. **Option 2:** Simply register again with the **same email** - it will work!

See [DATA_RECOVERY.md](DATA_RECOVERY.md) for full recovery instructions.

## Future Features

- 📊 Progress tracking and certificates
- 🎯 Learning goals and milestones
- 🤝 Parent/teacher dashboard
- 📱 Mobile app version
- 🌐 Multi-language support
- 💬 AI improvements for more topics

## Support

If you have questions or want to suggest new topics, please let me know!

---

Made with ❤️ for students everywhere 🌊
