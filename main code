import re
import json

languages = [
    "Python", "Java", "C++", "C", "JavaScript", "HTML", "CSS",
    "SQL", "R"
]

technologies = [
    "CNN", "TensorFlow", "PyTorch", "OpenCV", "React",
    "Django", "Flask", "Git", "Docker"
]

skills = [
    "AI", "ML", "Machine Learning", "Deep Learning",
    "Data Science", "NLP", "Computer Vision",
    "Web Development", "Data Analysis"
]


def extract_information(text):
    result = {
        "skill": [],
        "technology": [],
        "language": []
    }

    text_lower = text.lower()

    for item in skills:
        if re.search(r'\b' + re.escape(item.lower()) + r'\b', text_lower):
            result["skill"].append(item)

    for item in technologies:
        if re.search(r'\b' + re.escape(item.lower()) + r'\b', text_lower):
            result["technology"].append(item)

    for item in languages:
        if re.search(r'\b' + re.escape(item.lower()) + r'\b', text_lower):
            result["language"].append(item)

    return result


text = input("Describe your experience: ")

output = extract_information(text)

print(json.dumps(output, indent=4))

jobs = {
    "AI Engineer": ["Python", "AI", "Machine Learning", "CNN"],
    "Web Developer": ["Python", "HTML", "CSS", "JavaScript"],
    "Data Scientist": ["Python", "Machine Learning", "SQL", "Data Science"]
}


candidate_skills = ["Python", "AI", "Machine Learning"]


def find_best_job(candidate_skills):
    best_job = ""
    best_score = 0

    for job, required_skills in jobs.items():

        matched = 0

        for skill in required_skills:
            if skill.lower() in [x.lower() for x in candidate_skills]:
                matched += 1

        percentage = (matched / len(required_skills)) * 100

        print(job, ":", percentage, "%")

        if percentage > best_score:
            best_score = percentage
            best_job = job

    print()
    print("You are a good match for", best_job,
          "(", int(best_score), "% )")


find_best_job(candidate_skills)
