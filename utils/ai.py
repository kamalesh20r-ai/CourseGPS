import os
from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_roadmap(degree, career, skills):

    prompt = f"""
You are CourseGPS, an AI-powered career navigator and virtual professor.

Student background:
{degree}

Target career:
{career}

Required skills for this career:
{", ".join(skills)}

Create a practical learning roadmap for this student.

Requirements:

1. Organize the roadmap into logical phases.
2. Put topics in the correct learning order.
3. Explain briefly why each phase matters.
4. Include the important topics from the required skills.
5. Add practical projects where appropriate.
6. Keep the roadmap suitable for a college student.
7. Do not assume the student already knows advanced concepts.
8. Focus on skills needed to become job-ready.
9. Make the roadmap practical rather than just listing technologies.
10. Include a clear progression from fundamentals to advanced topics.

Return the response in clear Markdown.

Use this structure:

# Career Goal

Briefly explain the selected career and what the student will eventually be able to build.

## Phase 1 — Foundations

- Topic
- Topic
- Topic

Explain why this phase matters.

## Phase 2 — Core Skills

- Topic
- Topic
- Topic

Explain why this phase matters.

## Phase 3 — Advanced Skills

- Topic
- Topic
- Topic

Explain why this phase matters.

## Phase 4 — Production Skills

- Topic
- Topic
- Topic

Explain why this phase matters.

## Practical Projects

1. Project
2. Project
3. Project

## Final Job-Ready Skills

- Skill
- Skill
- Skill
"""


    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        generation_config={
            "thinking_level": "low"
        }
    )

    return interaction.output_text
def teach_topic(topic, career, degree):
    prompt = f"""
You are CourseGPS, an AI virtual professor.

Student degree/background:
{degree}

Target career:
{career}

Topic to teach:
{topic}

Teach this topic to a college student who is learning it
for the first time.

Requirements:

1. Start with a simple explanation.
2. Explain the important concepts step by step.
3. Use a practical real-world example.
4. Explain how this topic is useful for the student's target career.
5. Include a small example where appropriate.
6. Avoid unnecessary advanced mathematics.
7. End with a short "Quick Check" containing 3 questions.
8. Use clear Markdown.
9. Keep the lesson practical and understandable.

Structure:

# {topic}

## What is it?

## Why does it matter?

## Core Concepts

## Practical Example

## How it helps in {career}

## Quick Check

1.
2.
3.
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        generation_config={
            "thinking_level": "low"
        }
    )

    return interaction.output_text
def ask_professor(question, topic, career, degree):
    prompt = f"""
You are CourseGPS, an AI virtual professor.

Student background:
{degree}

Target career:
{career}

Current learning topic:
{topic}

Student's question:
{question}

Answer the student's question clearly and practically.

Requirements:

1. Answer the exact question first.
2. Explain the concept in simple language.
3. Give a small example when useful.
4. Relate the explanation to {career} when relevant.
5. Do not assume advanced knowledge.
6. If the question is outside the current topic, briefly explain
   that and answer it if it is still relevant to the student's learning.
7. Use Markdown.
8. Do not unnecessarily repeat the entire lesson.
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        generation_config={
            "thinking_level": "low"
        }
    )

    return interaction.output_text
def analyze_syllabus(syllabus_text):
    prompt = f"""
You are CourseGPS, an AI assistant for college educators.

Analyze the following college syllabus:

--- SYLLABUS ---
{syllabus_text}
--- END SYLLABUS ---

Identify areas where the syllabus may need modernization.

Return the analysis using this structure:

# 📚 Syllabus Analysis

## 1. Current Topics

List the major topics found in the syllabus.

## 2. Potentially Outdated Areas

Identify topics, tools, technologies, or approaches that may be
outdated or need updating.

For each one:
- Existing topic
- Why it may need modernization
- Suggested modern topic or technology

## 3. Recommended Modern Skills

List important modern skills that could complement the syllabus.

## 4. Suggested OER Resources

For each recommended area, suggest useful types of
Open Educational Resources that an educator could use.

## 5. Modernized Syllabus Direction

Give a concise suggestion for how the syllabus could be
updated while preserving its core academic purpose.

Keep the analysis practical and suitable for a college educator.
Do not claim that a topic is outdated merely because it is old;
explain why an update may be useful.
"""

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        generation_config={
            "thinking_level": "low"
        }
    )

    return interaction.output_text