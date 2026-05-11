import math
from collections import Counter


SKILL_ALIASES = {
    # Languages
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "cpp": "cpp",
    "r": "r",
    "kotlin": "kotlin",
    # ML / Data
    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",
    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics",
    "stats": "statistics",
    "regression": "regression",
    "clustering": "clustering",
    "data-viz": "data_visualization",
    "data visualization": "data_visualization",
    "data viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "power bi": "data_visualization",
    "powerbi": "data_visualization",
    "pandas": "pandas",
    "numpy": "numpy",
    # Web — Frontend
    "react": "react",
    "reacts": "react",
    "reactjs": "react",
    "vue": "vue",
    "vue.js": "vue",
    "vuejs": "vue",
    "redux": "redux",
    "tailwind": "tailwind",
    "html/css": "html_css",
    "html css": "html_css",
    "html": "html_css",
    "css": "html_css",
    "jest": "jest",
    "graphql": "graphql",
    # Web — Backend
    "node.js": "nodejs",
    "nodejs": "nodejs",
    "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot",
    "springboot": "spring_boot",
    "rest api": "rest_api",
    "rest": "rest_api",
    "restapi": "rest_api",
    "microservices": "microservices",
    # Databases
    "sql": "sql",
    "mysql": "mysql",
    "mysq": "mysql",
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "mongodb": "mongodb",
    "redis": "redis",
    # DevOps / Cloud
    "docker": "docker",
    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "k8s": "kubernetes",
    "ci/cd": "ci_cd",
    "cicd": "ci_cd",
    "ci cd": "ci_cd",
    "aws": "aws",
    # Mobile
    "android": "android",
    "firebase": "firebase",
    # CS Fundamentals
    "algorithms": "algorithms",
    "algoritms": "algorithms",
    "data structure": "data_structures",
    "data structures": "data_structures",
    "competitive programming": "competitive_programming",
    # Design
    "ui/ux": "ui_ux",
    "ui ux": "ui_ux",
    "figma": "figma",
}


RESUMES = [
    {"id": "01", "name": "Arjun Sharma", "raw_skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"},
    {"id": "02", "name": "Priya Nair", "raw_skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"},
    {"id": "03", "name": "Rahul Gupta", "raw_skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"},
    {"id": "04", "name": "Sneha Patel", "raw_skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"},
    {"id": "05", "name": "Vikram Singh", "raw_skills": "C++, Algoritms, Data Structure, competitive programming, python"},
    {"id": "06", "name": "Ananya Krishnan", "raw_skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"},
    {"id": "07", "name": "Karan Mehta", "raw_skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau"},
    {"id": "08", "name": "Deepika Rao", "raw_skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"},
    {"id": "09", "name": "Aditya Kumar", "raw_skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"},
    {"id": "10", "name": "Meera Iyer", "raw_skills": "python, R, statistics, ML, regression, clustering, Power-BI"},
]


JDS = [
    {
        "label": "JD-1",
        "company": "Kakao",
        "role": "ML Engineer",
        "required": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization",
        "preferred": "NLP, BERT, Feature Engineering, Statistics",
    },
    {
        "label": "JD-2",
        "company": "Naver",
        "role": "Backend Engineer",
        "required": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes",
        "preferred": "REST API, CI/CD, Redis",
    },
    {
        "label": "JD-3",
        "company": "Line",
        "role": "Frontend Engineer",
        "required": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS",
        "preferred": "Node.js, GraphQL, Redux, Jest, AWS",
    },
]


def normalize_skills(raw_skills: str) -> list[str]:
    normalized = []
    for token in raw_skills.lower().split(","):
        key = token.strip()
        if not key:
            continue
        # Each comma-separated token is treated as a phrase first.
        canonical = SKILL_ALIASES.get(key)
        if canonical is not None:
            normalized.append(canonical)
    return normalized


def deduplicate(skills: list[str]) -> list[str]:
    seen = set()
    deduped = []
    for skill in skills:
        if skill not in seen:
            seen.add(skill)
            deduped.append(skill)
    return deduped


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


def main() -> None:
    # Step 1 + 2: normalize and deduplicate resume skills.
    processed_resumes = []
    for resume in RESUMES:
        normalized = normalize_skills(resume["raw_skills"])
        deduped = deduplicate(normalized)
        processed_resumes.append({**resume, "skills": deduped})

    # Step 3: shared vocabulary from resumes only (alphabetical).
    vocab = sorted({skill for r in processed_resumes for skill in r["skills"]})
    vocab_index = {skill: idx for idx, skill in enumerate(vocab)}

    # Step 4: compute IDF using 10 resumes and no smoothing.
    total_docs = len(processed_resumes)
    df = Counter()
    for resume in processed_resumes:
        for skill in resume["skills"]:
            df[skill] += 1
    idf = {skill: math.log(total_docs / df[skill]) for skill in vocab}

    # Step 4 continued: build resume TF-IDF vectors.
    resume_vectors = {}
    for resume in processed_resumes:
        skills = resume["skills"]
        n_unique = len(skills)
        vec = [0.0] * len(vocab)
        if n_unique > 0:
            tf = 1.0 / n_unique
            for skill in skills:
                vec[vocab_index[skill]] = tf * idf[skill]
        resume_vectors[resume["name"]] = vec

    # Step 5 + 6: build JD binary vectors, compute similarity, rank top 3.
    for jd in JDS:
        jd_raw = jd["required"] + ", " + jd["preferred"]
        jd_skills = deduplicate(normalize_skills(jd_raw))
        jd_vec = [0.0] * len(vocab)
        for skill in jd_skills:
            if skill in vocab_index:
                jd_vec[vocab_index[skill]] = 1.0

        scored = []
        for resume in processed_resumes:
            score = cosine_similarity(resume_vectors[resume["name"]], jd_vec)
            scored.append((resume["name"], score))

        scored.sort(key=lambda item: (-item[1], item[0]))
        top3 = scored[:3]

        print(f'{jd["label"]} — {jd["company"]} ({jd["role"]})')
        print(", ".join(f"{name}({score:.2f})" for name, score in top3))


if __name__ == "__main__":
    main()
