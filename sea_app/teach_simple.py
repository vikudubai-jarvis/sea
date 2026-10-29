"""
SOCRATIC TEACHING - Help them figure it out, don't give answers! 🌊
"""

import re

def teach(question, age):
    """Main teaching - HELP them think, don't answer!"""
    guidance = get_guidance(question, age)
    return guidance


def get_guidance(question, age):
    """Guide them to figure it out themselves"""

    # Clean up
    q = question.lower().strip()
    original = question

    # IS IT MATH? Help them solve it, don't give answer
    if is_math_question(q):
        return guide_math(q, age)

    # IS IT A CONCEPT? Help them understand it
    if is_concept_question(q):
        return guide_concept(original, age)

    # OTHERWISE: Ask what they think
    return guide_general(original, age)


def normalize_math(text):
    """Turn words like 'divided into' or 'times' into symbols"""
    t = text.lower()
    t = re.sub(r'divided\s+(by|into)', '/', t)
    t = re.sub(r'multiplied\s+by|\btimes\b', '*', t)
    t = re.sub(r'\bplus\b', '+', t)
    t = re.sub(r'\bminus\b', '-', t)
    return t.replace('×', '*').replace('÷', '/')


def is_math_question(q):
    """Check if it's a math problem"""
    return re.search(r'\d\s*[+\-*/%]\s*\d', normalize_math(q)) is not None


def try_simple_math(expression):
    """Safely evaluate simple math - returns answer or None"""
    try:
        match = re.search(r'(\d+)\s*([+\-*/%])\s*(\d+)', normalize_math(expression))
        if not match:
            return None
        num1, op, num2 = match.groups()
        num1, num2 = int(num1), int(num2)

        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return int(num1 / num2) if num2 != 0 else None
        elif op == '%':
            return num1 % num2 if num2 != 0 else None
        return None
    except:
        return None


def is_concept_question(q):
    """Check if it's asking 'what is'"""
    return 'what' in q or 'how' in q or 'why' in q or 'explain' in q


def guide_math(expression, age):
    """GUIDE them through math, don't just answer!"""

    # Extract the numbers
    normalized = normalize_math(expression)
    m = re.search(r'(\d+)\s*[+\-*/%]\s*(\d+)', normalized)
    if not m:
        return guide_general(expression, age)
    num1, num2 = int(m.group(1)), int(m.group(2))

    # Find operator
    if '+' in normalized:
        if age < 8:
            return f"""Great question about **{expression}**!

Let me help you figure this out:
- You have **{num1}** things
- You GET **{num2}** more things
- If you count them all together... how many do you have?

Try counting! Use your fingers if you want! 🖐️

**What do YOU think the answer is?**"""
        elif age < 13:
            return f"""Good question: **{expression}**

Here's how to solve it:
1. Start with **{num1}**
2. Count UP **{num2}** more times
3. See where you land!

Try it! What number do you get?"""
        else:
            return f"""You're asking: **{expression}**

Here's the method:
- Start at {num1}
- Add {num2}
- Count carefully

What's your answer? Show me how you got it!"""

    elif '-' in normalized:
        if age < 8:
            return f"""You asked: **{expression}**

Let me help:
- You START with **{num1}** things
- You TAKE AWAY **{num2}**
- How many are LEFT?

Try it! **What's your answer?**"""
        elif age < 13:
            return f"""Subtraction question: **{expression}**

Here's how:
1. Start with {num1}
2. Take away {num2}
3. Count what's left

What do you get?"""
        else:
            return f"""Problem: **{expression}**

Solve this by:
- Beginning at {num1}
- Subtracting {num2}
- Finding the result

What's your answer?"""

    elif '*' in normalized:
        if age < 8:
            return f"""Multiplication: **{expression}**

Think of it like:
- **{num1}** groups
- **{num2}** items in each group
- How many TOTAL?

Can you figure it out?"""
        elif age < 13:
            return f"""Multiplication: **{expression}**

Remember:
- {num1} groups of {num2}
- OR {num2} groups of {num1}
- What's the total?

Give it a try!"""
        else:
            return f"""Problem: **{expression}**

Multiply {num1} × {num2}. What do you get?"""

    elif '/' in normalized:
        if age < 8:
            return f"""Sharing question: **{expression}**

Imagine you have **{num1}** cookies and you share them with **{num2}** friends.
- Give one cookie to each friend
- Keep going until no cookies are left over

How many cookies does each friend get?"""
        elif age < 13:
            return f"""Division question: **{expression}**

Think of it as sharing:
1. Start with **{num1}**
2. Split it into **{num2}** equal groups
3. How many are in each group?

What do you get?"""
        else:
            return f"""Problem: **{expression}**

How many times does **{num2}** fit into **{num1}**? What's the result?"""

    return f"""You asked: **{expression}**

Try solving this step by step. What do YOU think the answer is?"""


def guide_concept(question, age):
    """GUIDE them to understand concepts"""

    if age < 8:
        return f"""You asked: **{question}** 🤔

That's a GREAT question! Let me ask YOU something:

**What do you ALREADY know about it?**
Tell me what you think! 💭"""

    elif age < 13:
        return f"""Good question: **{question}**

Before I explain, I want to know:
**What do YOU think it means?**

Tell me your guess - there's no wrong answer!"""

    elif age < 18:
        return f"""Interesting: **{question}**

Here's what I want YOU to think about:
- What CONNECTS this to things you know?
- What's your CURRENT understanding?

Let's build from there!"""

    else:
        return f"""You're asking about: **{question}**

Before we dive deeper:
- What framework do you use to think about this?
- What would help you understand it better?

Let's explore together!"""


def guide_general(question, age):
    """Guide for any other question"""

    if age < 8:
        return f"""You asked: **{question}** 🤔

**I want to know - what do YOU think?**
What's your guess? 💭"""

    elif age < 13:
        return f"""Great question: **{question}**

Before I help, tell me:
**What do you already know about this?**
What's your guess?"""

    elif age < 18:
        return f"""Interesting question: **{question}**

What's your CURRENT understanding of this?
What would help you figure it out?"""

    else:
        return f"""Regarding **{question}**:

What's your initial take? What do you think?"""
