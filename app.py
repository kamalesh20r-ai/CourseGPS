import streamlit as st
from utils.roadmap import load_careers
from utils.ai import (
    generate_roadmap,
    teach_topic,
    ask_professor,
    analyze_syllabus
)
from utils.oer import (
    load_oer_resources,
    find_resources,
    find_relevant_resources,
    detect_oer_topics,
    get_oer_reason
)

st.set_page_config(
    page_title="CourseGPS",
    page_icon="🧭",
    layout="wide"
)

careers = load_careers()
oer_resources = load_oer_resources()


# -----------------------------
# SESSION STATE
# -----------------------------

if "step" not in st.session_state:
    st.session_state.step = 1

if "degree" not in st.session_state:
    st.session_state.degree = ""

if "career" not in st.session_state:
    st.session_state.career = ""

if "career_known" not in st.session_state:
    st.session_state.career_known = None

if "roadmap" not in st.session_state:
    st.session_state.roadmap = None

if "lesson" not in st.session_state:
    st.session_state.lesson = None

if "answer" not in st.session_state:
    st.session_state.answer = None

if "current_topic_index" not in st.session_state:
    st.session_state.current_topic_index = 0

if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = []

if "lesson" not in st.session_state:
    st.session_state.lesson = None

if "answer" not in st.session_state:
    st.session_state.answer = None

if "syllabus_analysis" not in st.session_state:
    st.session_state.syllabus_analysis = None
# -----------------------------
# HEADER
# -----------------------------

st.title("🧭 CourseGPS")
st.subheader("Don't just graduate. Be future-ready.")

st.write(
    "Your AI-powered learning navigator and virtual professor."
)

st.divider()

mode = st.radio(
    "Choose your mode",
    ["🎓 Student Mode", "👨‍🏫 Educator Mode"],
    horizontal=True
)

st.divider()

if mode == "👨‍🏫 Educator Mode":

    st.header("👨‍🏫 CourseGPS Educator Mode")

    st.write(
        "Upload your syllabus and CourseGPS will help identify "
        "areas that may need modernization."
    )

    uploaded_file = st.file_uploader(
        "📄 Upload your syllabus",
        type=["txt", "pdf"]
    )

    if uploaded_file:

        if uploaded_file.name.lower().endswith(".pdf"):

            from pypdf import PdfReader

            reader = PdfReader(uploaded_file)

            syllabus_text = ""

            for page in reader.pages:
                text = page.extract_text()

                if text:
                    syllabus_text += text + "\n"

        else:

            syllabus_text = uploaded_file.read().decode("utf-8")

        st.success("✅ Syllabus uploaded successfully!")

        st.subheader("📋 Uploaded Syllabus")

        st.text_area(
            "Syllabus Content",
            syllabus_text,
            height=300
        )

        st.divider()

        if st.button("🧠 Analyze Syllabus"):

            with st.spinner(
                "🧠 CourseGPS is analyzing your syllabus..."
            ):

                try:

                    st.session_state.syllabus_analysis = analyze_syllabus(
                        syllabus_text
                    )

                except Exception as e:

                    st.error(
                        "⚡ AI analysis is temporarily unavailable."
                    )

                    st.session_state.syllabus_analysis = None

        if st.session_state.syllabus_analysis:

            st.subheader("📚 CourseGPS Syllabus Analysis")

            st.markdown(
                st.session_state.syllabus_analysis
            )
        st.divider()

        st.subheader("🔎 CourseGPS OER Recommendations")

        detected_topics = detect_oer_topics(syllabus_text)

        if detected_topics:

            st.write(
                "CourseGPS identified the following learning areas "
                "and matched them with available Open Educational Resources."
            )

            matched_resources = find_relevant_resources(
                detected_topics,
                oer_resources
            )

            if matched_resources:

                for resource in matched_resources:

                    st.markdown(
                        f"### 📘 {resource['title']}"
                    )

                    st.write(
                        f"**Topic:** {resource['topic']}"
                    )

                    st.write(
                        f"**Provider:** {resource['provider']}"
                    )

                    st.write(
                        f"**Type:** {resource['type']}"
                    )

                    st.write(f"💡 **Why CourseGPS recommends it:** "f"{get_oer_reason(resource['topic'])}")

                    st.link_button(
                        "🔗 Open Resource",
                        resource["url"]
                    )

                    st.divider()

            else:

                st.info(
                    "No matching OER resources are currently "
                    "available in the CourseGPS resource library."
                )

        else:

            st.info(
                "No supported learning topics were detected "
                "for OER matching."
            )

    st.stop()

# =========================================================
# STEP 1 — DEGREE
# =========================================================

if st.session_state.step == 1:

    st.header("👋 Let's get started")

    degree = st.text_input(
        "What are you currently studying?",
        placeholder="Example: B.Tech Artificial Intelligence and Data Science"
    )

    if st.button("Continue →", type="primary"):

        if degree.strip():

            st.session_state.degree = degree
            st.session_state.step = 2

            st.rerun()

        else:

            st.warning("Please enter your degree first.")


# =========================================================
# STEP 2 — CAREER KNOWLEDGE
# =========================================================

elif st.session_state.step == 2:

    st.header("🎯 Let's understand your career goal")

    st.success(
        f"You are studying **{st.session_state.degree}**."
    )

    st.write(
        "Do you already know which career you want to pursue?"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "✅ Yes, I know my career",
            use_container_width=True
        ):

            st.session_state.career_known = True
            st.session_state.step = 3

            st.rerun()

    with col2:

        if st.button(
            "🤔 No, help me choose",
            use_container_width=True
        ):

            st.session_state.career_known = False
            st.session_state.step = 4

            st.rerun()


# =========================================================
# STEP 3 — DIRECT CAREER SELECTION
# =========================================================

elif st.session_state.step == 3:

    st.header("🚀 Choose your target career")

    career = st.selectbox(
        "Which career are you interested in?",
        list(careers.keys())
    )

    st.session_state.career = career

    st.info(
        careers[career]["description"]
    )

    st.write("### 📚 Skills you'll need")

    for skill in careers[career]["skills"]:
        st.write(f"• {skill}")

    if st.button(
        "Create My Roadmap 🚀",
        type="primary"
    ):

        st.session_state.step = 5
        st.rerun()

    if st.button("← Back"):

        st.session_state.step = 2
        st.rerun()


# =========================================================
# STEP 4 — CAREER DISCOVERY
# =========================================================

elif st.session_state.step == 4:

    st.header("🧭 Let's discover what career fits you")

    st.write(
        "Answer a few questions and CourseGPS will help you "
        "explore career paths."
    )

    st.divider()

    # Question 1

    interest = st.radio(
        "What type of work interests you most?",
        [
            "🤖 Building AI systems and applications",
            "📊 Working with data and finding insights",
            "💻 Building software and applications",
            "🔬 Researching technology and solving complex problems"
        ]
    )

    # Question 2

    work_style = st.radio(
        "What kind of work do you enjoy?",
        [
            "🛠️ Building and creating things",
            "📈 Analyzing data and finding patterns",
            "🧩 Solving technical problems",
            "🧠 Exploring new concepts and technologies"
        ]
    )

    # Question 3

    preference = st.radio(
        "Which sounds most exciting to you?",
        [
            "✨ Creating AI-powered products",
            "📊 Turning data into useful decisions",
            "⚙️ Building intelligent software systems",
            "🧪 Experimenting with new AI/ML ideas"
        ]
    )

    if st.button(
        "🔎 Discover Career Paths",
        type="primary"
    ):

        # Simple prototype recommendation logic

        if (
            "AI systems" in interest
            or "AI-powered products" in preference
        ):

            suggestions = [
                "GenAI Engineer",
                "Machine Learning Engineer"
            ]

        elif (
            "data" in interest.lower()
            or "data" in work_style.lower()
        ):

            suggestions = [
                "Data Scientist",
                "Data Analyst"
            ]

        elif "software" in interest.lower():

            suggestions = [
                "GenAI Engineer",
                "Machine Learning Engineer"
            ]

        else:

            suggestions = [
                "Machine Learning Engineer",
                "GenAI Engineer"
            ]

        st.session_state.suggestions = suggestions
        st.session_state.step = 6

        st.rerun()

    if st.button("← Back"):

        st.session_state.step = 2
        st.rerun()

# =========================================================
# STEP 5 — AI GENERATED ROADMAP
# =========================================================

elif st.session_state.step == 5:

    st.header("🧭 Your CourseGPS Roadmap")

    career = st.session_state.career
    degree = st.session_state.degree

    st.success(
        f"Career selected: **{career}**"
    )

    skills = careers[career]["skills"]

    # Learning progress
    completed_count = len(st.session_state.completed_topics)
    total_topics = len(skills)

    progress_percentage = (
    completed_count / total_topics
    if total_topics > 0
    else 0
)

    st.subheader("📊 Your Learning Progress")

    st.progress(progress_percentage)

    st.write(
    f"**{completed_count} / {total_topics} topics completed** "
    f"({progress_percentage * 100:.0f}%)"
)
    st.write("### 🗺️ Learning Path")

    for index, topic in enumerate(skills):

        if topic in st.session_state.completed_topics:

            st.success(
            f"✅ {index + 1}. {topic}"
        )

        elif index == st.session_state.current_topic_index:

            st.info(
            f"📖 {index + 1}. {topic} — Current"
        )

        else:

            st.write(
            f"🔒 {index + 1}. {topic}"
        )
    # Generate roadmap only once
    if st.session_state.roadmap is None:

        with st.spinner(
        "🧠 CourseGPS is creating your personalized roadmap..."
    ):

            try:

                st.session_state.roadmap = generate_roadmap(
                degree,
                career,
                skills
            )

            except Exception as e:

                st.warning(
                "⚡ AI generation is temporarily unavailable. "
                "CourseGPS is loading a ready-to-use roadmap."
            )

            st.session_state.roadmap = f"""
# Career Goal

Your goal is to become a **{career}**.

CourseGPS has created a practical learning path based on the
skills required for this career.

## Phase 1 — Foundations

- Python Programming
- Basic Data Structures
- Problem Solving
- Git & GitHub
- Fundamental Statistics

Build strong fundamentals before moving into advanced topics.

## Phase 2 — Core Skills

{chr(10).join(f"- {skill}" for skill in skills[:5])}

Focus on understanding the core technologies and concepts
required for your target career.

## Phase 3 — Advanced Skills

{chr(10).join(f"- {skill}" for skill in skills[5:9])}

Apply these concepts through practical projects and
real-world problem solving.

## Phase 4 — Production Skills

- Build real-world applications
- Create APIs where required
- Learn deployment fundamentals
- Use Git and version control
- Test and document your projects

## Practical Projects

1. Beginner project related to {career}
2. Intermediate project using multiple required skills
3. End-to-end real-world project

## Final Job-Ready Skills

{chr(10).join(f"- {skill}" for skill in skills)}

- Problem solving
- Project development
- Git & GitHub
- Communication
"""
    # Display the stored roadmap
    if st.session_state.roadmap:

        st.markdown(
            st.session_state.roadmap
        )

    st.divider()

    st.header("📚 Recommended Open Learning Resources")

    st.write(
        "CourseGPS has matched open learning resources "
        "to the skills required for your career."
    )

    for skill in skills:

        resources = find_resources(
            skill,
            oer_resources
        )

        if resources:

            st.subheader(f"📖 {skill}")

            for resource in resources:

                st.markdown(
                    f"**{resource['title']}**  \n"
                    f"Provider: {resource['provider']}  \n"
                    f"Type: {resource['type']}  \n"
                    f"[Open Resource ↗]({resource['url']})"
                )

    st.divider()

    st.header("👨‍🏫 CourseGPS AI Professor")

    st.write(
    "CourseGPS will guide you through your career roadmap "
    "one topic at a time."
)

    # Current topic
    current_index = st.session_state.current_topic_index

    if current_index < len(skills):

        current_topic = skills[current_index]

        st.info(
        f"📖 Current Topic: **{current_topic}**"
    )

        st.progress(
        current_index / len(skills)
    )

        st.write(
        f"Topic {current_index + 1} of {len(skills)}"
    )

        # Generate lesson
        if st.session_state.lesson is None:

            if st.button("🎓 Start This Lesson"):

                with st.spinner(
                f"👨‍🏫 CourseGPS is preparing your lesson on {current_topic}..."
            ):

                    try:

                        st.session_state.lesson = teach_topic(
                        current_topic,
                        career,
                        degree
                    )

                    except Exception:

                        st.session_state.lesson = f"""
# {current_topic}

## What is it?

**{current_topic}** is an important skill for becoming a
**{career}**.

## Why does it matter?

This topic is part of your CourseGPS learning path and helps
you build the knowledge required for your target career.

## Core Concepts

- Understand the basic terminology
- Learn the fundamental concepts
- Practice with simple examples
- Apply the concept to real-world problems

## Practical Example

Try building a small practical project using **{current_topic}**.

## Career Connection

Understanding **{current_topic}** will help you progress
towards becoming a **{career}**.

## Quick Check

1. What is {current_topic}?
2. Why is it useful?
3. Give one practical application.
"""

    # Display lesson
        if st.session_state.lesson:

            st.markdown(
            st.session_state.lesson
        )

            st.divider()

            st.subheader("💬 Ask CourseGPS")

            question = st.text_area(
            "Have a doubt about this topic?",
            placeholder=f"Ask anything about {current_topic}..."
        )

            if st.button("🤖 Ask Professor"):

                if question.strip():

                    with st.spinner(
                    "👨‍🏫 CourseGPS is thinking..."
                ):

                        try:

                            st.session_state.answer = ask_professor(
                            question,
                            current_topic,
                            career,
                            degree
                        )

                        except Exception:

                            st.session_state.answer = (
                            "⚡ The AI Professor is temporarily "
                            "unavailable. Please try again later."
                        )

                else:

                    st.warning(
                    "Please enter a question first."
                )

            if st.session_state.answer:

                st.subheader("👨‍🏫 Professor's Answer")

                st.markdown(
                st.session_state.answer
            )

            st.divider()

            if current_topic in st.session_state.completed_topics:

                st.success(
                f"✅ {current_topic} completed!"
            )

            else:

                if st.button(
                "✅ Mark Topic Complete & Continue"
            ):

                    st.session_state.completed_topics.append(
                    current_topic
                )

                    st.session_state.current_topic_index += 1

                    st.session_state.lesson = None

                    st.session_state.answer = None

                    st.rerun()

    else:

        st.success(
        "🎉 Congratulations! You have completed all the topics "
        "in your CourseGPS learning path."
    )

    st.divider()

    st.header("🤝 Share Your Roadmap")

    st.write(
    "Share your personalized CourseGPS learning roadmap "
    "with your friends and classmates."
)

    share_text = f"""
COURSEGPS
Don't just graduate. Be future-ready.

Student Background:
{degree}

Target Career:
{career}

Learning Progress:
{completed_count} / {total_topics} topics completed

Learning Roadmap:
{st.session_state.roadmap}
"""

    st.text_area(
    "📋 Your Shareable Roadmap",
    share_text,
    height=300
)

    st.download_button(
    label="📥 Download Roadmap",
    data=share_text,
    file_name="CourseGPS_Roadmap.txt",
    mime="text/plain"
)
    
    if st.button("← Back to Career"):

        st.session_state.step = 3
        st.session_state.roadmap = None
        st.session_state.current_topic_index = 0
        st.session_state.completed_topics = []
        st.session_state.lesson = None
        st.session_state.answer = None
        st.rerun()


# =========================================================
# STEP 6 — CAREER DISCOVERY RESULTS
# =========================================================

elif st.session_state.step == 6:

    st.header("🎯 Career paths you can explore")

    st.write(
        "Based on your answers, CourseGPS found these "
        "career paths worth exploring:"
    )

    suggestions = st.session_state.suggestions

    for career in suggestions:

        st.subheader(f"💼 {career}")

        st.write(
            careers[career]["description"]
        )

        st.write("**Key skills:**")

        skills_preview = careers[career]["skills"][:5]

        st.write(
            " • ".join(skills_preview)
        )

        if st.button(
            f"Explore {career}",
            key=f"explore_{career}"
        ):

            st.session_state.career = career
            st.session_state.step = 5

            st.rerun()

        st.divider()

    if st.button("← Try Again"):

        st.session_state.step = 4
        st.rerun()