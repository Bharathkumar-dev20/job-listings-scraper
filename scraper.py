import requests
import csv
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_data = []

for job in jobs:
    title_element = job.find("h2", class_="title")
    company_element = job.find("h3", class_="company")
    location_element = job.find("p", class_="location")
    link_element = job.find("a", string="Apply")

    title = title_element.text.strip() if title_element else "N/A"
    company = company_element.text.strip() if company_element else "N/A"
    location = location_element.text.strip() if location_element else "N/A"
    url = link_element["href"] if link_element else "N/A"

    job_data.append({
        "title": title,
        "company": company,
        "location": location,
        "url": url
    })

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["title", "company", "location", "url"]
    )

    writer.writeheader()
    writer.writerows(job_data)

print("Jobs saved successfully!")