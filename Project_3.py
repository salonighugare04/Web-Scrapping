import requests
from bs4 import BeautifulSoup
import pandas as pd

lst = []
base_url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Home_Search&cboPresFuncArea=42&pDate=Y&sequence={}&startPage={}"

for page_no in range(1,54):
    url = base_url.format(page_no, page_no)
    response = requests.get(url)
    # if response.status_code != 200:
    #     print(f"Failed to retrieve page {page_no}")
    #     continue
    
    converted_data = BeautifulSoup(response.text, 'html.parser')
    job_divs = converted_data.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in job_divs:

        title = job.find('h2').text.strip()
        name = job.find('h3', class_="joblist-comp-name").text.strip()
        experience = job.find('i', class_="material-icons").next_sibling.strip()
        package_element = job.find('i', class_="material-icons rupee")
        if package_element:
            Package = package_element.next_sibling.strip()
        else:
            Package = 'N.A'
        location = job.find('ul', class_="top-jd-dtl clearfix").find('span').text.strip()
        description = job.find('ul', class_='list-job-dtl clearfix').find('li').get_text(strip=True)   #.a['href]
        key_skills = job.find('span', class_='srp-skills').text.strip()

        job_data = {
            "Job Title": title,
            "Company Name": name,
            "Experience": experience,
            "Package" : Package,
            "Location": location,
            "Job Description": description,
            "Key Skills": key_skills
        }

        for key, value in job_data.items():
         if value == '' or value is None:
          job_data[key] = 'N.A'

        lst.append(job_data)
            
    print(f"Page {page_no} processed")
 
jobs_df = pd.DataFrame(lst)
jobs_df.to_excel('Third-Data.xlsx', index=False)

print("Excel file 3 has been created!")