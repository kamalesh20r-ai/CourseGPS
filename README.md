# 🧭 CourseGPS

> **Don't just graduate. Be future-ready.**

CourseGPS is an **AI-powered conversational career navigator and virtual professor** designed to help college students discover relevant career paths, identify the skills they need, find Open Educational Resources (OER), generate personalized learning roadmaps, and learn through an AI-powered teaching assistant.

---

## 🚀 Overview

Students often struggle with questions like:

* What career can I pursue with my degree?
* What skills are actually required for that career?
* What should I learn first?
* Where can I find reliable learning resources?
* Is my college syllabus aligned with current industry requirements?

**CourseGPS** brings these pieces together into one AI-powered learning platform.

It connects:

**Degree → Career → Skills → OER → Personalized Roadmap → AI Professor**

---

## 🎯 Problem Statement

Higher-education students face several challenges:

### 📚 Scattered Learning Resources

Students often spend significant time searching across different platforms for useful and relevant learning materials.

### 🏫 Outdated Academic Content

Traditional college syllabi may not always keep pace with rapidly changing industry technologies and skills.

### 🧭 Lack of Career Direction

Students may know their degree but remain unsure about which career path to choose and what skills they should develop.

### 🤝 Limited Collaborative Learning

Students often create useful learning paths individually without an easy way to organize and share them with peers.

---

## 💡 Solution

CourseGPS provides an AI-powered learning navigation system that helps students move from their academic background to a structured career-oriented learning journey.

### Core workflow

```text
Student Degree / Background
            ↓
      Career Selection
            ↓
      Required Skills
            ↓
     OER Discovery Engine
            ↓
   Personalized Roadmap
            ↓
       AI Professor
            ↓
      Progress Tracking
            ↓
       Peer Sharing
```

---

## ✨ Key Features

### 🎓 1. Student Mode

Students can enter their degree and academic background and begin their personalized learning journey.

Example:

> "Naan AI & DS student"

CourseGPS uses this information to guide the student toward relevant career paths.

---

### 💼 2. Career Discovery

Students who are unsure about their career can answer a set of questions to discover suitable career directions.

The prototype currently supports career paths such as:

* GenAI Engineer
* Machine Learning Engineer
* Data Scientist
* Data Analyst

---

### 🧠 3. Career-to-Skill Mapping

Once a career is selected, CourseGPS identifies the important skills associated with that career.

For example:

```text
GenAI Engineer
│
├── Python
├── Git & GitHub
├── ML Fundamentals
├── NLP Fundamentals
├── LLMs
├── Prompt Engineering
├── Embeddings
├── Vector Databases
├── RAG
├── LLM APIs
├── FastAPI
└── Docker
```

---

### 🗺️ 4. Personalized Learning Roadmap

CourseGPS uses Gemini to generate a structured learning roadmap based on:

* Student degree
* Selected career
* Required skills

The roadmap is organized into practical learning phases and helps students understand **what to learn and in what order**.

---

### 📖 5. OER Discovery Engine

CourseGPS connects learning topics with **Open Educational Resources (OER)**.

The current prototype includes resources related to topics such as:

* Python
* Git & GitHub
* Data Structures
* SQL
* Machine Learning Fundamentals
* Large Language Models
* Retrieval-Augmented Generation (RAG)

The goal is to help students discover useful learning resources without searching across multiple platforms manually.

---

### 👨‍🏫 6. AI Professor

CourseGPS includes an AI-powered virtual professor.

Students can select a topic and receive:

* Concept explanations
* Core concepts
* Practical examples
* Career relevance
* Quick checks
* Answers to topic-specific questions

Students can also ask follow-up questions while learning.

---

### 📊 7. Learning Progress Tracking

The student interface provides basic progress tracking so learners can monitor their progress through the generated learning roadmap.

---

### 🤝 8. Peer Roadmap Sharing

Students can share their personalized learning roadmaps with peers.

This supports the project's vision of creating a:

> **Peer-Shared Learning Ecosystem**

---

## 👨‍🏫 Educator Mode

CourseGPS also includes a prototype **Educator Mode**.

Educators can upload a syllabus in:

* `.txt`
* `.pdf`

CourseGPS extracts the syllabus content and uses AI to analyze it.

### Educator workflow

```text
Upload Syllabus
      ↓
Extract Content
      ↓
AI Syllabus Analysis
      ↓
Identify Potentially Outdated Areas
      ↓
Recommend Modern Skills
      ↓
Match Relevant OER
```

The system can identify areas that may need modernization and recommend relevant Open Educational Resources.

---

## 🧩 Example Educator Analysis

CourseGPS can identify areas such as:

* Traditional programming approaches
* Older database practices
* Missing version-control practices
* Lack of automated testing
* Missing cloud/containerization concepts
* Missing modern developer tooling
* Application security fundamentals

It can then recommend modern learning directions and relevant OER resources.

---

## 🏗️ System Architecture

```text
                         ┌───────────────────┐
                         │      Student      │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    Streamlit UI   │
                         └─────────┬─────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
            ┌───────────────┐             ┌───────────────┐
            │ Student Mode  │             │ Educator Mode │
            └───────┬───────┘             └───────┬───────┘
                    │                             │
                    ▼                             ▼
            ┌───────────────┐             ┌───────────────┐
            │ Career Mapping│             │ PDF/TXT Parser │
            └───────┬───────┘             └───────┬───────┘
                    │                             │
                    ▼                             ▼
            ┌───────────────┐             ┌───────────────┐
            │ Skill Mapping │             │ Gemini Analysis│
            └───────┬───────┘             └───────┬───────┘
                    │                             │
                    ▼                             ▼
            ┌───────────────┐             ┌───────────────┐
            │ Gemini API    │             │ OER Matching  │
            └───────┬───────┘             └───────────────┘
                    │
             ┌──────┴──────┐
             │             │
             ▼             ▼
       ┌───────────┐ ┌───────────────┐
       │ Roadmap   │ │ AI Professor  │
       └───────────┘ └───────────────┘
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                     |
| ----------------- | --------------------------- |
| Python            | Core application logic      |
| Streamlit         | Web application interface   |
| Google Gemini API | AI generation and teaching  |
| JSON              | Career and OER data storage |
| pypdf             | PDF syllabus extraction     |
| Git               | Version control             |
| GitHub            | Source-code hosting         |

---

## 📁 Project Structure

```text
CourseGPS/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── DATA/
│   ├── careers.json
│   └── oer_resources.json
│
└── utils/
    ├── __init__.py
    ├── ai.py
    ├── oer.py
    └── roadmap.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kamalesh20r-ai/CourseGPS.git
```

### 2. Navigate to the project

```bash
cd CourseGPS
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

CourseGPS requires a **Google Gemini API key**.

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file or API key to GitHub.

The repository already includes `.gitignore` rules for environment files and virtual environments.

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Prototype Workflow

### Student Mode

```text
1. Enter degree/background
        ↓
2. Choose whether career is known
        ↓
3. Select or discover career
        ↓
4. Identify required skills
        ↓
5. Generate personalized roadmap
        ↓
6. Select learning topic
        ↓
7. Learn with AI Professor
        ↓
8. Track progress
        ↓
9. Share roadmap with peers
```

### Educator Mode

```text
1. Upload syllabus
        ↓
2. Extract syllabus content
        ↓
3. Analyze syllabus using AI
        ↓
4. Identify potentially outdated areas
        ↓
5. Recommend modern skills
        ↓
6. Match relevant OER
```

---

## 🌍 Open Educational Resources

CourseGPS is designed around the idea of making high-quality learning resources easier to discover and organize.

The prototype demonstrates OER discovery for areas including:

* Programming
* Data Structures
* SQL
* Machine Learning
* Large Language Models
* Retrieval-Augmented Generation
* Version Control

The project aligns with the broader goal of improving access to quality educational resources.

---

## 🎓 SDG Alignment

CourseGPS is aligned with:

### **UN Sustainable Development Goal 4 — Quality Education**

The project focuses on:

* Accessible learning resources
* Personalized learning
* Career-oriented skill development
* Modern educational content
* Inclusive learning support

---

## 💰 Future Business Model

CourseGPS can follow a **Freemium + B2B** model.

### Free

* Career discovery
* Basic roadmap generation
* OER discovery

### Premium

* Deep-dive AI lessons
* Continuous AI mentorship
* Advanced progress tracking
* AI mock interviews
* Resume assistance
* Personalized career preparation

### B2B

Colleges and educational institutions could use CourseGPS for:

* Syllabus modernization
* OER recommendations
* Student skill-gap analysis
* Career guidance
* Industry-aligned curriculum planning

---

## 🔮 Future Scope

Future versions of CourseGPS can include:

* 🤖 AI-powered mock interviews
* 📄 Automated resume generation
* 🎯 Skill-gap analysis
* 📈 Advanced learning analytics
* 🧠 Adaptive learning paths
* 🏫 College-level dashboards
* 👥 Collaborative learning communities
* 🔎 Larger OER search infrastructure
* ☁️ Cloud deployment
* 🔐 User authentication and persistent profiles
* 📚 Larger career and skill knowledge base
* 💼 Corporate hiring integration

---

## ⚠️ Current Limitations

This repository represents a **functional prototype**.

Current limitations include:

* Limited career dataset
* Limited OER resource library
* Basic progress tracking
* Prototype-level peer sharing
* No persistent user database
* No authentication system
* AI responses depend on API availability and limits
* Educator modernization analysis is AI-assisted and should be reviewed by educators

The prototype is intended to demonstrate the concept and workflow rather than serve as a production-scale educational platform.

---

## 📌 Project Status

**Status: 🚧 Functional Prototype**

Core prototype capabilities currently demonstrated:

* [x] Student Mode
* [x] Career selection
* [x] Career discovery
* [x] Career-to-skill mapping
* [x] AI roadmap generation
* [x] OER discovery
* [x] AI Professor
* [x] Basic progress tracking
* [x] Peer roadmap sharing
* [x] Educator Mode
* [x] PDF syllabus extraction
* [x] AI syllabus analysis
* [x] OER recommendations
* [x] GitHub repository

---

## 👨‍💻 Author

**Kamalesh**

Department of Artificial Intelligence & Data Science
New Prince Shri Bhavani College of Engineering and Technology
Chennai, Tamil Nadu, India

---

## 📜 License

This project is currently a prototype developed for educational, research, and innovation purposes.

---

## ⭐ Support

If you find **CourseGPS** interesting, consider giving the repository a ⭐ on GitHub.

> **CourseGPS — Don't just graduate. Be future-ready.** 🧭
