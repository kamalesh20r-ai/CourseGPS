import json


def load_oer_resources():

    with open(
        "data/oer_resources.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def find_resources(topic, resources):

    return resources.get(topic, [])
def find_relevant_resources(topics, resources):
    matches = []

    for topic in topics:

        topic_lower = topic.lower()

        for resource_topic, resource_list in resources.items():

            if (
                topic_lower in resource_topic.lower()
                or resource_topic.lower() in topic_lower
            ):

                for resource in resource_list:

                    matches.append({
                        "topic": topic,
                        "title": resource["title"],
                        "provider": resource["provider"],
                        "url": resource["url"],
                        "type": resource["type"]
                    })

    return matches
def detect_oer_topics(syllabus_text):
    topic_map = {
        "Python": [
            "python",
            "programming"
        ],
        "Data Structures": [
            "data structures",
            "linked lists",
            "stacks",
            "queues",
            "trees",
            "graphs"
        ],
        "SQL": [
            "sql",
            "database",
            "databases",
            "relational"
        ],
        "Git & GitHub": [
            "git",
            "github",
            "version control"
        ],
        "Machine Learning Fundamentals": [
            "machine learning",
            "machine learning fundamentals"
        ],
        "Large Language Models": [
            "large language models",
            "llm",
            "llms"
        ],
        "RAG": [
            "retrieval augmented generation",
            "rag"
        ]
    }

    detected_topics = []

    text = syllabus_text.lower()

    for topic, keywords in topic_map.items():

        for keyword in keywords:

            if keyword in text:

                detected_topics.append(topic)
                break

    return detected_topics
def get_oer_reason(topic):
    reasons = {
        "Python": (
            "This resource provides structured material for building "
            "programming fundamentals and practical coding skills."
        ),
        "Data Structures": (
            "This resource provides interactive explanations and "
            "visualizations that can help students understand "
            "data structures and algorithms."
        ),
        "SQL": (
            "This resource provides practical SQL learning and "
            "query-based exercises."
        ),
        "Git & GitHub": (
            "This resource helps students learn modern version "
            "control and collaborative software development."
        ),
        "Machine Learning Fundamentals": (
            "This resource provides structured introductory material "
            "for understanding core machine learning concepts."
        ),
        "Large Language Models": (
            "This resource helps learners understand modern "
            "language-model and NLP concepts."
        ),
        "RAG": (
            "This resource introduces retrieval-augmented approaches "
            "for building knowledge-grounded AI applications."
        )
    }

    return reasons.get(
        topic,
        "This resource is relevant to the identified learning area."
    )