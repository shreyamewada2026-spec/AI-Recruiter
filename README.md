# AI-Recruiter
A rule-based NLP system that extracts skills, technologies, and programming languages from conversational text and converts them into structured JSON.

## Project Overview

AI Recruiter is a simple rule-based Natural Language Processing (NLP) system designed to assist with the recruitment process.

The system takes conversational input from a candidate describing their experience or skills, extracts relevant **skills, technologies, and programming languages**, and organizes the information into a structured JSON format.
The extracted information can then be used to compare the candidate's skills with the requirements of different job roles and calculate a job-match percentage.
The project is designed without using an LLM API key.

## Problem Statement

Recruiters have to go through large amounts of candidate information to identify relevant skills and determine which job roles a candidate may be suitable for.

The aim of this project is to create a simple AI-assisted recruitment system that can:
* Extract useful information from unstructured text.
* Identify skills, technologies, and programming languages.
* Convert the extracted information into structured JSON.
* Compare candidate skills with job requirements.
* Calculate a percentage match for different job roles.
* Identify the job role with the highest match.

## Installation Instructions

### Requirements
The project uses Python's built-in libraries:

* `re` — for pattern matching and word detection.
* `json` — for generating structured JSON output.

No external Python libraries are required for the current version.

### Steps
1. Install Python 3 from the official Python website.

2. Clone this repository

3. Open the project folder:
cd AI-Recruiter

4. Run the Python program:
python main.py

5. Enter a sentence describing the candidate's experience when prompted.

## Dataset Used
No external dataset is used in the current version.

Instead the project uses manually created lists of:

* Programming languages
* Technologies
* Skills

For example:

languages = [
    "Python", "Java", "C++", "C",
    "JavaScript", "HTML", "CSS", "SQL", "R"
]

These lists act as the knowledge base for the rule-based extraction system.

## Methodology

The project consists of two main stages.

### 1. Information Extraction

The candidate enters conversational text such as:
'I worked in the AI/ML department and worked with CNN models using Python.'

The program converts the input to lowercase and searches for known terms.
Regular expressions are used to identify complete words so that short language names such as 'C' and 'R' are not incorrectly detected inside other words.

The extracted information is placed into three categories:

Skills
Technologies
Languages

The result is then converted into JSON format.

Example:

```json
{
    "skill": [
        "AI",
        "ML"
    ],
    "technology": [
        "CNN"
    ],
    "language": [
        "Python"
    ]
}
```

### 2. Candidate-Job Matching

The extracted candidate skills are compared with the skills required for different jobs.

For example:

AI Engineer:
Python, AI, Machine Learning, CNN

If a candidate has:
Python, AI, Machine Learning

then 3 out of 4 required skills match.

The percentage is calculated as:
Match Percentage =
(Number of Matching Skills / Total Required Skills) × 100

Therefore:
3 / 4 × 100 = 75%

The program compares the scores of different jobs and identifies the role with the highest match.

## Technologies Used

### Programming Language

* Python

### Python Libraries

* re — Regular Expressions for word and pattern matching.
* json — Formatting and displaying the extracted information as JSON.

### Concepts Used

* Python dictionaries
* Python lists
* Functions
* for loops
* Conditional statements
* String methods
* List comprehensions
* Regular expressions
* JSON formatting
* Rule-based NLP
* Skill matching and percentage calculation

No LLM is required by the current implementation.

## Results

The system successfully extracts relevant information from conversational input.

### Example Input:
I worked in the AI/ML department and worked with CNN models using Python.

### Example Extraction Result:

```json
{
    "skill": [
        "AI",
        "ML"
    ],
    "technology": [
        "CNN"
    ],
    "language": [
        "Python"
    ]
}
```

The extracted skills can then be compared against job requirements.
### For example:
AI Engineer       → 75%
Web Developer     → 25%
Data Scientist    → 50%

The system identifies:
AI Engineer → 75%
as the best match.

## Challenges Faced

### 1. Incorrect detection of C and R

Initially, the program searched for terms using a simple substring check.

For example:
if item.lower() in text_lower:

This caused 'C' or 'R' to be detected even when they were simply letters inside other words.

This was solved by using regular expressions and word boundaries:
re.search(r'\b' + re.escape(item.lower()) + r'\b', text_lower)

This allows the program to distinguish between a programming language such as 'C' and the letter 'c' appearing inside another word.

### 2. Different capitalization

Users may write:
Python
python
PYTHON

The program solves this by converting the input to lowercase before searching.

### 3. Matching different job requirements

Different jobs require different combinations of skills.
The program solves this by storing each job and its required skills in a dictionary and calculating the percentage of required skills that the candidate possesses.

## Future Improvements

The current system is a basic rule-based NLP implementation. It can be improved in several ways:

* Add more skills, technologies, and programming languages.
* Add synonyms for skills, such as treating "ML" and "Machine Learning" as related terms.
* Use NLP techniques such as tokenization and stemming.
* Add a larger and more realistic job dataset.
* Add experience levels such as beginner, intermediate, and advanced.
* Add a chatbot interface for recruiters and candidates.
* Allow recruiters to enter job descriptions instead of manually defining job requirements.
* Add a user interface.
* Improve the matching algorithm by giving different skills different weights.
* Add candidate ranking when multiple candidates are provided.
