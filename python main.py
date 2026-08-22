import re
import json

# PART 1
languages = [
    "Python", "Java", "C++", "C", "JavaScript",
    "HTML", "CSS", "SQL", "R"
]

technologies = [
    "CNN", "TensorFlow", "PyTorch", "OpenCV",
    "React", "Django", "Flask", "Git", "Docker"
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

# PART 2
jobs = {
    "AI Engineer": [
        "Python", "AI", "ML", "Machine Learning", "CNN"
    ],

    "Web Developer": [
        "Python", "HTML", "CSS", "JavaScript"
    ],

    "Data Scientist": [
        "Python", "ML", "Machine Learning", "SQL", "Data Science"
    ]
}


def find_best_job(candidate_skills):

    best_job = ""
    best_score = 0

    job_matches = {}

    for job, required_skills in jobs.items():

        matched = 0

        for skill in required_skills:

            if skill.lower() in [x.lower() for x in candidate_skills]:
                matched += 1

        percentage = (matched / len(required_skills)) * 100

        job_matches[job] = int(percentage)

        if percentage > best_score:
            best_score = percentage
            best_job = job

    return best_job, int(best_score), job_matches


text = input("Describe your experience: ")

extracted_info = extract_information(text)

candidate_skills = (
    extracted_info["skill"]
    + extracted_info["technology"]
    + extracted_info["language"]
)

best_job, best_score, job_matches = find_best_job(candidate_skills)

output = {
    "input": text,

    "extraction": extracted_info,

    "candidate_skills": candidate_skills,

    "job_matches": job_matches,

    "best_match": {
        "job": best_job,
        "match_percentage": best_score
    },

    "message": f"You are a good match for {best_job} ({best_score}%)"
}

print(json.dumps(output, indent=4))
