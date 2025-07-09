import requests
from bs4 import BeautifulSoup
import pandas as pd


lst=[]
#url1="https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35"
url="https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&postWeek=60&searchType=Home_Search&cboPresFuncArea=35&pDate=Y&sequence=1&startPage=1"
res= requests.get(url).text
converted_data= BeautifulSoup (res, 'html.parser') 

pg1_divs= converted_data.find_all('div',class_="inside-rhs main-search-block")

for item in pg1_divs:
    Job_Title=item.find('h2').text.strip()
    Company_Name=item.find('h3',class_="joblist-comp-name").text.strip()
    Experience_years=item.find('i',class_="material-icons").next_sibling
    element = item.find('i', class_="material-icons")
    if element:
        Experience_years= element.next_sibling.strip() if element.next_sibling else None
    else:
        Experience_years = None
    
    Package=item.find('i',class_="material-icons rupee").next_sibling
    element = item.find('i', class_="material-icons rupee")
    if element:
        Package = element.next_sibling.strip() if element.next_sibling else None
    else:
        Package = None
        
    Location=item.find('ul',class_="top-jd-dtl clearfix").find('span').text
    Job_Description=item.find('ul',class_='list-job-dtl clearfix').find('li').text.strip()
    #description=Job_Description.get_text()
    Key_Skills=item.find('span',class_="srp-skills").text.strip()
    pg1_dic = {
            "Job_Title":Job_Title,
            "Company_Name":Company_Name,
            "Experience":Experience_years,
            "Package":Package,
            "Location":Location,
            "Description":Job_Description,
            "Key_skills":Key_Skills
    }
     
lst.append(pg1_dic)
print(pg1_dic)
    

# page_df=pd.DataFrame(lst)
# page_df.to_excel('Page-Data.xlsx')
 


# element = job.find('i', class_="material-icons")
    # if element.next_sibling is not None:
    #     Experience_years = element.next_sibling.strip()
    # else:
    #     Experience_years = print("N.A")
 
# Package=item.find('i',class_="material-icons rupee").next_sibling
#     element = item.find('i', class_="material-icons rupee")
#     if element:
#         Package = element.next_sibling.strip() if element.next_sibling else None
#     else:
#         Package = None