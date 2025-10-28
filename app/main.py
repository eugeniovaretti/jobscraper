from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper.jobs import scrape_jobs

app = FastAPI(title="Job Scraper API")

# Allow frontend (React) to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # depends on your React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/jobs")
def get_jobs():
    jobs = scrape_jobs()
    return {"jobs": jobs}
