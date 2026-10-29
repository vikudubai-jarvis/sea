import streamlit as st
from auth import login_user, register_user, check_login
from ai_tutor import start_learning_session_ai, get_feedback_and_next_question, get_hint_ai
from database import init_db
from guest_mode import (
    is_guest_trial_active, get_guest_info, create_guest_session,
    record_guest_usage, reset_guest_session, check_trial_expired
)
from sessions import (
    init_sessions_table, create_new_session, add_message_to_session,
    end_session, get_user_sessions, get_session_details, get_session_stats, delete_session
)
import os

# Initialize database
init_db()
init_sessions_table()

# Page configuration
st.set_page_config(
    page_title="Sea - Student Education AI",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        max-width: 800px;
    }
    .sea-header {
        text-align: center;
        color: #0066cc;
        margin-bottom: 30px;
    }
    .welcome-box {
        background-color: #e6f2ff;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_data = None
    st.session_state.show_settings = False
    st.session_state.is_guest = False
    st.session_state.current_session_id = None
    st.session_state.view_page = "learn"  # "learn" or "sessions"

# Main app logic
if not st.session_state.logged_in:
    st.markdown("<h1 class='sea-header'>🌊 Sea - Claude's Brother</h1>", unsafe_allow_html=True)
    st.write("Hey there! 👋 I'm **Sea**, Claude's brother. I'm here to help you learn about anything you want to know. Ask me anything - we'll figure it out together!")

    tab1, tab2, tab3 = st.tabs(["Login", "Register", "Try Free (1 Month)"])

    with tab1:
        st.subheader("Login")
        email = st.text_input("Gmail Account", key="login_email")

        if st.button("Login", key="login_btn"):
            if email:
                user_data = check_login(email)
                if user_data:
                    st.session_state.logged_in = True
                    st.session_state.user_data = user_data
                    st.success(f"Welcome back, {user_data['name']}!")
                    st.rerun()
                else:
                    st.error("Account not found. Please register first.")
            else:
                st.error("Please enter your Gmail address.")

    with tab2:
        st.subheader("Create New Account")
        name = st.text_input("Your Name", key="reg_name")
        age = st.slider("Your Age", min_value=3, max_value=99, value=13, key="reg_age")
        email = st.text_input("Gmail Account", key="reg_email")

        if st.button("Register", key="register_btn"):
            if name and email:
                success, message = register_user(name, age, email)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Please fill in all fields.")

    with tab3:
        st.subheader("🎉 Free Trial - 1 Month")

        # Check if trial is expired
        if check_trial_expired():
            st.error("❌ Your 1-month free trial has ended!")
            st.warning("Please **Login** or **Register** to continue using Sea.")
            st.info("💾 All your questions and chats are saved! Just login with your email.")
        else:
            guest_info = get_guest_info()

            if not guest_info['locked_out']:
                st.success(f"✅ Free trial active! You have **{guest_info['days_left']} days** left")
                st.write(f"📊 Questions asked so far: **{guest_info['usage_count']}**")
                st.info("💾 All your learning will be saved! After 1 month, just login to continue.")

                if st.button("Start Free Trial", key="guest_btn", type="primary"):
                    st.session_state.logged_in = True
                    st.session_state.is_guest = True
                    st.session_state.user_data = {
                        "name": "Guest User",
                        "age": 13,
                        "email": "guest@sea.local",
                        "is_guest": True
                    }
                    st.rerun()
            else:
                st.error("❌ Your trial has expired!")
                st.warning("Please login or register to continue.")

else:
    # Main app after login
    user_name = st.session_state.user_data['name']
    user_age = st.session_state.user_data['age']
    user_email = st.session_state.user_data['email']
    is_guest = st.session_state.is_guest

    # Check if guest trial expired
    if is_guest and check_trial_expired():
        st.error("⏰ Your 1-month free trial has ended!")
        st.warning("Please **Login** or **Register** with your email to continue.")
        st.info("💾 All your questions are saved! When you login, you can see everything.")

        if st.button("Login Now"):
            st.session_state.logged_in = False
            st.session_state.is_guest = False
            st.rerun()
        st.stop()

    st.markdown(f"<h1 class='sea-header'>🌊 Hey {user_name}! Sea here (Claude's brother)</h1>", unsafe_allow_html=True)
    st.write("Ready to learn something awesome? Ask me ANYTHING! 💪")

    if is_guest:
        guest_info = get_guest_info()
        st.write(f"⏳ **Free Trial:** {guest_info['days_left']} days left | Questions: {guest_info['usage_count']}")
        st.info("After 1 month, you'll need to login to continue. All your chats are saved! 💾")
    else:
        st.write(f"**You:** {user_age} years old | **Me:** Claude's brother, ready to teach!")

    # Top menu with navigation
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("📚 Learn", use_container_width=True):
            st.session_state.view_page = "learn"
            st.rerun()
    with col2:
        if st.button("📋 Sessions", use_container_width=True):
            st.session_state.view_page = "sessions"
            st.rerun()
    with col4:
        if st.button("⚙️ Settings", use_container_width=True):
            st.session_state.show_settings = not st.session_state.get("show_settings", False)
            st.rerun()
    with col6:
        if st.button("Logout", use_container_width=True):
            # End current session if in learn mode
            if st.session_state.view_page == "learn" and st.session_state.learning_active:
                if st.session_state.current_session_id and not is_guest:
                    end_session(st.session_state.current_session_id, user_email)
            st.session_state.logged_in = False
            st.session_state.user_data = None
            st.rerun()

    # Settings panel
    if st.session_state.get("show_settings", False):
        st.divider()
        st.subheader("⚙️ Settings & Backup")

        with st.expander("📦 Data Backup & Recovery", expanded=True):
            st.write("**Automatic backups** are created every time the app starts.")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("💾 Create Manual Backup"):
                    from backup import backup_database
                    success, message = backup_database()
                    if success:
                        st.success(message)
                    else:
                        st.error(message)

            with col2:
                if st.button("📂 View Backups"):
                    from backup import list_backups
                    backups = list_backups()
                    if backups:
                        st.write("Available backups:")
                        for backup in backups:
                            size_kb = backup['size'] / 1024
                            st.caption(f"📁 {backup['name']} ({size_kb:.1f} KB)")
                    else:
                        st.info("No backups yet")

            st.info("💡 **Tip:** If the app resets and you can't login with your old account, you can restore from a backup here!")

        st.divider()

    st.divider()

    # SESSIONS PAGE VIEW
    if st.session_state.view_page == "sessions" and not is_guest:
        st.subheader("📋 Your Learning Sessions")

        # Get stats
        stats = get_session_stats(user_email)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Sessions", stats["total_sessions"])
        with col2:
            st.metric("Questions Asked", stats["total_questions"])
        with col3:
            if stats["last_session"]:
                st.metric("Last Session", stats["last_session"][:10])

        st.divider()

        # Get all sessions
        sessions = get_user_sessions(user_email, limit=50)

        if sessions:
            st.write(f"**Your {len(sessions)} Recent Sessions:**")

            for session in sessions:
                session_id, question, started_at, ended_at, status, questions_count = session

                with st.expander(f"📌 {question[:50]}... ({status}) - {started_at[:10]}", expanded=False):
                    st.write(f"**Session ID:** {session_id}")
                    st.write(f"**Started:** {started_at}")
                    if ended_at:
                        st.write(f"**Ended:** {ended_at}")
                    st.write(f"**Questions Asked:** {questions_count}")
                    st.write(f"**Status:** {status}")

                    # Show session details
                    if st.button(f"View Full Session", key=f"view_{session_id}"):
                        session_info, messages = get_session_details(session_id, user_email)

                        st.write("---")
                        st.write("**Session Conversation:**")

                        for msg_type, content, timestamp in messages:
                            if msg_type == "student":
                                with st.chat_message("user"):
                                    st.write(content[:200] + "..." if len(content) > 200 else content)
                            else:
                                with st.chat_message("assistant", avatar="🌊"):
                                    st.write(content[:300] + "..." if len(content) > 300 else content)

                    # Delete option
                    if st.button(f"🗑️ Delete Session", key=f"delete_{session_id}"):
                        delete_session(session_id, user_email)
                        st.success("Session deleted!")
                        st.rerun()
        else:
            st.info("No learning sessions yet. Start learning to create your first session! 🌊")

        st.stop()  # Don't show learning interface when viewing sessions

    # Initialize session state for learning session
    if "learning_active" not in st.session_state:
        st.session_state.learning_active = False
        st.session_state.current_question = None
        st.session_state.learning_stage = "initial"
        st.session_state.student_answer = ""
        st.session_state.conversation = []
        st.session_state.step_count = 0

    # Main question answering interface
    if not st.session_state.learning_active:
        # Show "New Session" button to reset the form
        if st.button("➕ New Session", use_container_width=False):
            st.session_state.current_session_id = None
            st.rerun()

        st.subheader("💡 Ask Me Anything")
        st.write("Ask any question, and I'll help you learn by explaining concepts and asking guiding questions.")

        question = st.text_area("Your Question:", placeholder="e.g., How does photosynthesis work? What is algebra? How do magnets work?", height=100, key="user_question")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start Learning", type="primary"):
                if question.strip():
                    # Create new session (unless guest)
                    if not is_guest:
                        session_id = create_new_session(user_email, question)
                        st.session_state.current_session_id = session_id

                    st.session_state.learning_active = True
                    st.session_state.current_question = question
                    st.session_state.learning_stage = "intro"
                    st.session_state.conversation = []
                    st.session_state.step_count = 0
                    st.rerun()
                else:
                    st.warning("Please enter a question first!")

    else:
        # Interactive learning conversation with AI (or offline mode)
        st.subheader("📚 Learning Session")
        st.caption(f"Question: {st.session_state.current_question}")

        # Check if API is available
        api_available = os.getenv("ANTHROPIC_API_KEY")

        if not api_available:
            st.info("💡 Running in **Offline Mode** (no API key needed!) - Uses built-in knowledge for common topics")

        # Get initial explanation if starting
        if st.session_state.learning_stage == "intro":
            with st.spinner("🌊 Sea is thinking..."):
                try:
                    # Record guest usage if guest mode
                    if is_guest:
                        record_guest_usage()

                    if api_available:
                        # Use AI mode
                        intro_response = start_learning_session_ai(
                            st.session_state.current_question,
                            user_name,
                            user_age
                        )
                    else:
                        # Use offline mode with knowledge base
                        from teaching import start_learning_session
                        intro_response = start_learning_session(
                            st.session_state.current_question,
                            user_age
                        )

                    st.session_state.conversation.append({
                        "type": "sea",
                        "content": intro_response
                    })
                    st.session_state.learning_stage = "answering"
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        # Chat interface
        if st.session_state.learning_stage == "answering":
            # Chat options bar
            col1, col2 = st.columns([6, 1])

            with col2:
                if st.button("💡 Hint", use_container_width=True):
                    with st.spinner("Getting hint..."):
                        try:
                            if api_available:
                                hint = get_hint_ai(st.session_state.current_question, user_name, user_age)
                            else:
                                from teaching import get_hint
                                hint = get_hint(st.session_state.current_question, user_age)
                            st.session_state.conversation.append({
                                "type": "hint",
                                "content": hint
                            })
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {str(e)}")

            st.divider()

            # Chat messages
            chat_container = st.container(height=400)

            with chat_container:
                for msg in st.session_state.conversation:
                    if msg["type"] == "sea":
                        with st.chat_message("assistant", avatar="🌊"):
                            st.markdown(msg["content"])
                    elif msg["type"] == "student":
                        with st.chat_message("user"):
                            st.markdown(msg["content"])
                    elif msg["type"] == "hint":
                        with st.chat_message("assistant", avatar="💡"):
                            st.markdown(f"**Hint:** {msg['content']}")

            st.divider()

            # Chat input - bottom row
            col1, col2 = st.columns([6, 1])

            with col1:
                user_message = st.chat_input("Type your answer or ask a question...", key="chat_input")

            # Process message if entered
            if user_message:
                st.session_state.conversation.append({
                    "type": "student",
                    "content": user_message
                })

                with st.spinner("🌊 Sea is thinking..."):
                    try:
                        from teaching import start_learning_session, get_next_teaching_step, is_new_question

                        if is_new_question(user_message):
                            if api_available:
                                response = start_learning_session_ai(user_message, user_name, user_age)
                            else:
                                response = start_learning_session(user_message, user_age)
                        elif api_available:
                            response = get_feedback_and_next_question(
                                st.session_state.current_question,
                                user_message,
                                user_name,
                                user_age,
                                st.session_state.conversation
                            )
                        else:
                            response = get_next_teaching_step(
                                st.session_state.current_question,
                                user_message,
                                user_age,
                                st.session_state.step_count
                            )

                        st.session_state.conversation.append({
                            "type": "sea",
                            "content": response
                        })
                        st.session_state.step_count += 1
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

            with col2:
                if st.button("🏁 End", use_container_width=True, key="end_session_btn"):
                    # End session in database (if not guest)
                    if st.session_state.current_session_id and not is_guest:
                        end_session(st.session_state.current_session_id, user_email)

                    st.session_state.learning_active = False
                    st.session_state.learning_stage = "initial"
                    st.session_state.conversation = []
                    st.session_state.current_session_id = None
                    st.success("Great learning session! 🌊")
                    st.rerun()
