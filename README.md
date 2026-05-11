# Resume Matching Engine

This project implements the Redrob Hackathon workflow in Python using only standard libraries.

## What it does

- Normalizes noisy resume skills with the provided `SKILL_ALIASES`
- Deduplicates skills per resume
- Builds a shared vocabulary from resume skills
- Computes resume TF-IDF vectors (`TF = 1/N`, `IDF = ln(10/df)`)
- Builds binary vectors for JDs
- Calculates cosine similarity and prints top 3 candidates per JD

## File

- `resume_matching_engine.py` - complete implementation

## Run

```bash
python resume_matching_engine.py
```

## Output format

```text
JD-1 — Kakao (ML Engineer)
Name(score), Name(score), Name(score)
JD-2 — Naver (Backend Engineer)
Name(score), Name(score), Name(score)
JD-3 — Line (Frontend Engineer)
Name(score), Name(score), Name(score)
```

Scores are rounded to 2 decimals, and ties are broken alphabetically by candidate name.
