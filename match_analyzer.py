from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

resume = read("resume.txt")
job = read("job_description.txt")

vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
tfidf = vec.fit_transform([resume, job])

score = cosine_similarity(tfidf[0], tfidf[1])[0][0]
print(f"Match score: {score * 100:.1f}%")

# Keywords in the job description that are missing from the resume
terms = vec.get_feature_names_out()
res_vec = tfidf[0].toarray()[0]
job_vec = tfidf[1].toarray()[0]
missing = [(terms[i], job_vec[i]) for i in range(len(terms))
           if res_vec[i] == 0 and job_vec[i] > 0]
missing.sort(key=lambda x: -x[1])
print("Top missing keywords:", [w for w, _ in missing[:10]])