# 🌊 Sea - Features & How They Work

## ✅ Complete Features

### 1. **User Authentication**
- ✅ Register with name, age (3-99), Gmail
- ✅ Login with email
- ✅ Logout button (top right)
- ✅ Re-login to same account anytime
- ✅ SQLite database stores all user data securely

### 2. **AI-Powered Teaching (Claude API)**
- ✅ Answers **ANY question** - not just predefined topics
- ✅ Gives **direct answers first** - no more avoiding the question
- ✅ Shows working for math problems
- ✅ Explains concepts clearly
- ✅ Age-appropriate explanations (adapts to 3-99 years old)
- ✅ Interactive conversation style
- ✅ Progressive questioning to deepen understanding

### 3. **Interactive Learning Session**
- ✅ Student asks a question
- ✅ Sea explains the concept
- ✅ Sea asks an initial question
- ✅ Student answers
- ✅ Sea gives feedback on their thinking
- ✅ Sea asks a deeper follow-up question
- ✅ Repeat until student understands
- ✅ **Get Hint** button for stuck students
- ✅ **More Details** button for deeper explanation
- ✅ **End Session** button to finish

### 4. **Age-Appropriate Content**
All explanations adapt to age:
- **Young Child (3-7)** - Simple words, daily examples
- **Child (8-12)** - Structured, step-by-step
- **Teen (13-17)** - Detailed concepts, connections
- **Adult (18+)** - Advanced, sophisticated

### 5. **Question Topics**
Sea can answer about:
- 🧮 Math (algebra, geometry, calculus, etc.)
- 🔬 Science (biology, chemistry, physics, etc.)
- 📚 Languages & Literature
- 🌍 History & Geography
- 💻 Coding & Technology
- 🎨 Arts & Design
- 🏃 Sports & Fitness
- 💪 Health & Wellness
- **+ Anything else!**

### 6. **User Data**
- ✅ Login/register information saved
- ✅ Age-based content preferences stored
- ✅ Question history kept (optional feature)
- ✅ All data stays private in local SQLite database

---

## 🎯 How It Works (Step by Step)

### Example: A 10-year-old asking "What is 1+1?"

1. **Student** registers: "Sam, age 10, sam@gmail.com"
2. **Student** asks: "What is 1+1?"
3. **Sea** responds: 
   - **ANSWER:** "1 + 1 = 2"
   - **EXPLANATION:** "When you have one apple and get one more apple, you have two apples total..."
   - **QUESTION:** "If you have 1 penny and your friend gives you 1 more penny, how many pennies do you have?"
4. **Student** answers: "I have 2 pennies!"
5. **Sea** responds:
   - **FEEDBACK:** "Exactly! You understand addition!"
   - **NEXT QUESTION:** "Now, if you had 2 pennies and got 1 more, how many would you have?"
6. **Student** continues answering...
7. After a few exchanges, **Student** fully understands!
8. **Student** clicks "End Session"
9. Later, **Student** can logout and login again to ask more questions

---

## 🚀 Setup Checklist

- [ ] Download/clone the project
- [ ] Install Python 3.8+
- [ ] Get Claude API key (https://console.anthropic.com/)
- [ ] Set ANTHROPIC_API_KEY environment variable
- [ ] `pip install -r requirements.txt`
- [ ] `streamlit run app.py`
- [ ] Register first time
- [ ] Start asking questions!

---

## 💡 Key Improvements from Original Request

| What You Asked | What We Built |
|---|---|
| Help but not give answers | Now gives direct answers, then guides deeper understanding |
| Login system | ✅ Name, age, Gmail |
| Age-appropriate content | ✅ Fully adapted to 3-99 years old |
| Answer any question | ✅ Uses Claude AI for unlimited topics |
| Interactive teaching | ✅ Real Socratic method conversation |
| Backend database | ✅ SQLite stores users & history |
| Logout/re-login | ✅ Works with same account |

---

## 🔧 Technical Stack

- **Frontend:** Streamlit (Python web framework)
- **Backend:** SQLite database
- **AI:** Claude API (Anthropic)
- **Authentication:** Email-based (Gmail)
- **Deployment:** Runs locally on your computer

---

## 📈 Example Conversations

### Math (Age 12)
```
Student: What is 5 × 3?
Sea: 5 × 3 = 15. When you have 5 groups of 3 items...
Student: So like 5 baskets with 3 apples each?
Sea: Perfect! That's exactly right!
```

### Science (Age 15)
```
Student: How does photosynthesis work?
Sea: Plants use sunlight, water, and CO₂ to make glucose...
Student: So the sun's energy becomes chemical energy?
Sea: Exactly! Now can you explain what happens to that glucose?
```

### Coding (Age 16)
```
Student: What's a loop in Python?
Sea: A loop repeats code multiple times. Here's an example...
Student: So it runs the same code over and over?
Sea: Yes! What would you use a loop for?
```

---

Made with ❤️ using Claude AI 🌊
