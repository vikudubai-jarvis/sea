"""
SIMPLE TEACHING ENGINE - My baby AI Sea's brain! 🌊
No complexity, just ANSWERS then QUESTIONS
"""

import re

from teach_simple import teach, is_math_question, try_simple_math

QUESTION_WORDS = {"what", "how", "why", "who", "when", "where", "explain", "tell", "can", "does", "do"}
QUESTION_PATTERN = re.compile(r'\b(' + '|'.join(QUESTION_WORDS) + r')\b')


def start_learning_session(question, age):
    """Start learning session - returns ANSWER then question"""
    return teach(question, age)


def is_new_question(text):
    """A message with a question word or a math expression is a new question, not an answer"""
    t = text.strip().lower()
    return bool(QUESTION_PATTERN.search(t)) or is_math_question(t)


def get_next_teaching_step(question, student_answer, age, step_count):
    """Give feedback on the student's answer and keep the conversation going"""
    if is_math_question(question.lower()):
        expected = try_simple_math(question)
        found = re.search(r'-?\d+', student_answer)

        if not found:
            return f"""I didn't see a number in *"{student_answer}"*.

For **{question}**, what number do you get?"""

        given = int(found.group(0))

        if expected is None:
            return f"""You said **{given}**. Walk me through how you got it - what did you do first?"""

        if given == expected:
            return f"""YES! **{question}** = **{expected}**. You got it!

Can you explain HOW you solved it?"""

        return f"""You said **{given}**. Let's check it together.

Try counting or breaking the numbers into tens and ones. What do you get now?"""

    return f"""Good thinking! You said *"{student_answer}"*.

What part of **{question}** feels most interesting to you? Tell me what you'd like to figure out next."""


def get_hint(question, age):
    """Give a hint without spoiling"""
    return f"Think about what you already know... What connections can you make with {question}?"
