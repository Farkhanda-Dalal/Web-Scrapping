from bs4 import BeautifulSoup
import requests #was installed using pip install requests
import time

html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
soup=BeautifulSoup(html_text,"lxml")

# #FIND 1 INSTANCE
#job=soup.find("li",class_="clearfix job-bx wht-shd-bx")
# #strip() removes leading adn trailing whitespaces
# company_name=job.find("h3","joblist-comp-name").text.strip()
# skills=job.find("span","srp-skills").text.replace(" ","").strip()
# print(f'''
# Company Name:{company_name}
# Skills Required:{skills} ''')

#LOOPING THROUGH ALL POSTS
# jobs=soup.findAll("li",class_="clearfix job-bx wht-shd-bx")
# for job in jobs:
#         posted=job.find("span",class_="sim-posted").text.strip()
#         if(posted=="Posted few days ago"):
#             company_name=job.find("h3","joblist-comp-name").text.strip()
#             skills=job.find("span","srp-skills").text.replace(" ","").strip()
        
#             print(f"Company Name:{company_name}\nSkills Required:{skills}\nPosted:{posted}\n")


unfamiliar_skills=input("Enter skills that you are not familiar with:").casefold()
print(f"Filtering out {unfamiliar_skills}.....")
#Formating retrieved data
def find_jobs():
    jobs=soup.findAll("li",class_="clearfix job-bx wht-shd-bx")
    for i,job in enumerate(jobs):
            posted=job.find("span",class_="sim-posted").text.strip()
            skills=job.find("span","srp-skills").text.replace(" ","").strip()
            if(posted=="Posted few days ago" and unfamiliar_skills not in skills):
                company_name=job.find("h3","joblist-comp-name").text.strip()
                
                #more_info=job.header.h2.a willprint the entire <a></a> while more_info=job.header.h2.a.text will only print the text inside the a tag
                more_info=job.header.h2.a["href"]

                with open("job_list.pdf","a")as job_list:
                     job_list.write(f"{i}. Company Name:{company_name}\n")
                     job_list.write(f"Skills Required:{skills}\n")
                     job_list.write(f"More Info:{more_info}\n\n")

    print(f"Job Data after filtering {unfamiliar_skills} was saved in file")

# if __name__=="__main__":
#      while True:
find_jobs()
        #   print("Waiting for 10 secs.....")
        #   time.sleep(10)
