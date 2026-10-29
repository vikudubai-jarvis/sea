# Setting Up Claude API for Sea

Sea now uses Claude AI to answer **ANY question** - not just predefined topics! Here's how to set it up:

## Step 1: Get a Free API Key

1. Go to: https://console.anthropic.com/
2. Sign up for a free account (if you don't have one)
3. Click "API Keys" in the sidebar
4. Click "Create Key"
5. Copy your API key (keep it secret!)

## Step 2: Set the Environment Variable

### On Windows (PowerShell)
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

Or set it permanently:
```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-...", "User")
```

### On Windows (Command Prompt)
```cmd
set ANTHROPIC_API_KEY=sk-ant-...
```

### On macOS/Linux
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Or add to your `.bashrc` or `.zshrc`:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```

## Step 3: Run the App

```bash
streamlit run app.py
```

## Features with AI

Now Sea can:
- ✅ Answer **ANY question** (math, science, history, languages, coding, etc.)
- ✅ Give **clear answers** - no more generic responses
- ✅ Show **working and explanations**
- ✅ Ask **follow-up questions** to deepen understanding
- ✅ Provide **hints** without giving away answers
- ✅ Adapt to **any age level** (3-99 years old)

## Test It Out

Try asking Sea:
- "What is 1+1?" → Gets the answer (2) AND explains it
- "How do photosynthesis work?" → Full explanation with follow-ups
- "What is the capital of France?" → Answer with context
- "Explain recursion in programming" → Age-appropriate coding explanation
- **Any question your students ask!**

## Pricing

- **Free tier**: 5M tokens/month (usually enough for personal use)
- **Paid**: Very affordable (check console.anthropic.com for rates)
- 1 educational conversation ≈ 1,000-5,000 tokens

## Troubleshooting

**"API Key not found"**
- Make sure you set the environment variable
- Restart your terminal after setting it
- Check the key starts with "sk-ant-"

**"Invalid API Key"**
- Double-check you copied it correctly
- Generate a new key on the console

**"Rate Limited"**
- You've used too many tokens this month
- Upgrade to paid plan or wait for reset

---

Need help? Visit: https://docs.anthropic.com/
