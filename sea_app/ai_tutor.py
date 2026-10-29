import anthropic
import os

# Initialize Anthropic client
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    api_key = "your-api-key-here"  # Placeholder

client = anthropic.Anthropic(api_key=api_key)

def get_age_group(age):
    """Determine age group."""
    if age < 8:
        return "young child (3-7 years)"
    elif age < 13:
        return "child (8-12 years)"
    elif age < 18:
        return "teenager (13-17 years)"
    else:
        return "adult (18+ years)"

def start_learning_session_ai(question, student_name, age):
    """Start learning session with AI explanation."""
    age_group = get_age_group(age)

    prompt = f"""You are Sea, a friendly educational AI tutor. A student named {student_name} (age {age}, {age_group}) has asked: "{question}"

Your task: Provide a CLEAR, DIRECT ANSWER to their question first. Then help them understand it better.

Format your response as follows:
1. DIRECT ANSWER: Start with a clear, straightforward answer in 1-2 sentences
2. EXPLANATION: Explain the concept in a way suitable for a {age_group}
3. NEXT QUESTION: Ask them ONE follow-up question to deepen their understanding

Keep explanations simple and use examples when helpful.
If it's a math problem, show the working and the answer clearly."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def get_feedback_and_next_question(question, student_answer, student_name, age, conversation_history):
    """Get feedback on student's answer and ask next question."""
    age_group = get_age_group(age)

    # Build conversation context
    context = "Previous conversation:\n"
    for msg in conversation_history[-4:]:  # Last 2 exchanges
        if msg["type"] == "sea":
            context += f"Sea: {msg['content']}\n"
        else:
            context += f"{student_name}: {msg['content']}\n"

    prompt = f"""You are Sea, a friendly educational AI tutor. You're helping {student_name} (age {age}, {age_group}) understand "{question}".

{context}

{student_name} just answered: "{student_answer}"

Your task:
1. FEEDBACK: Give positive feedback on their thinking
2. VALIDATE: If correct, praise them. If partially correct, acknowledge what's right
3. NEXT QUESTION: Ask ONE deeper follow-up question to help them understand better

Do NOT just ask "why do you think that?" if they've already explained. Instead, move the conversation forward.
Keep responses concise and encouraging."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=400,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def get_hint_ai(question, student_name, age):
    """Generate a helpful hint without giving the answer."""
    age_group = get_age_group(age)

    prompt = f"""You are Sea, a tutor helping {student_name} (age {age}, {age_group}) with: "{question}"

Provide a helpful HINT that:
- Points them in the right direction
- Does NOT give away the answer
- Uses simple language for their age
- Is encouraging

Just provide the hint, nothing else."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=150,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def get_explanation_ai(question, student_name, age):
    """Get a detailed explanation of a topic."""
    age_group = get_age_group(age)

    prompt = f"""You are Sea, an educational tutor. {student_name} (age {age}, {age_group}) wants to understand: "{question}"

Provide a clear, friendly explanation that:
1. Is suitable for a {age_group}
2. Uses real-world examples
3. Explains WHY it works that way
4. Is 2-3 paragraphs max
5. Uses simple language

Be warm and encouraging."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=400,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text
