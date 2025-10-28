import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    # mock example initial commit
    url = "https://example.com/jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for item in soup.select(".job-item"):
        jobs.append({
            "title": item.select_one(".title").text.strip(),
            "company": item.select_one(".company").text.strip(),
            "link": item.select_one("a")["href"],
        })
    
    if not jobs:
        jobs = [
            {"title": "Python Developer", "company": "TechCorp", "link": "#"},
            {"title": "Frontend Engineer", "company": "Webify", "link": "#"},
        ]
    
    return jobs
