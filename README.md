# Resume–Job Match Analyzer

An NLP tool in Python that compares a resume with a job description using TF-IDF and cosine similarity. It calculates a match score and lists important keywords missing from the resume, helping tailor it to a role. Built with scikit-learn.

## What it does
- Converts the resume and the job description into TF-IDF vectors
- Calculates a match score using cosine similarity
- Lists important keywords from the job description that are missing from the resume

## Tech used
Python, scikit-learn

## How to run
1. Install the library: `pip install scikit-learn`
2. Create `resume.txt` with your resume text and `job_description.txt` with the job posting, in the same folder as the script
3. Run: `python match_analyzer.py`

## Example output
Tested with my own resume and an internship posting:

```
Match score: 21.0%
Top missing keywords: ['students', 'candidates', 'skills students', '2027', '2027 2028', '2028 candidates', 'ai based', 'based', 'based projects', 'candidates good']
```

## How it works
TF-IDF gives higher weight to words that are important in a document but not common everywhere. Cosine similarity then measures how close the two documents are, from 0 (nothing in common) to 1 (identical).

## Limitations
- Generic posting words such as "students" and "candidates" also appear in the missing-keywords list
- It compares word usage only, so it does not understand the meaning of sentences

## Future improvements
- Filter out generic words from the missing-keywords list
- Add a simple web interface with Streamlit
- Test on more job descriptions
