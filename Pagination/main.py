from bs4 import BeautifulSoup
import requests

# def url_maker():

def get_soup(url):
    soup=BeautifulSoup(url,"lxml")
    return soup

def next_page(soup,stream):
    page=soup.find("a",class_="pagination_list_last")
    if page:
        next_link=requests.get(page["href"]).text
        new_soup=get_soup(next_link)
        get_data(new_soup,stream)
    else:
        return

def get_data(soup,stream):
    clg_details=soup.findAll("div",class_="tupple")
    for clg_details in clg_details:
        clg_name=clg_details.find("h3",class_="college_name").text.strip()
        location=clg_name.split()[-1]
        NIRF=clg_details.find("div",class_="tupple_top_block_left").text.strip()
        ownership=clg_details.find("strong",class_="strong_ownership").text.strip()
        course_list=clg_details.find_all("ul",class_="snippet_list")
        link=clg_details.h3.a["href"]
        
        with open(f"Top_{stream.capitalize()}_Colleges.pdf","a", encoding="utf-8")as file:
            file.write(f"College Name: {clg_name}\n")
            file.write(f"College Location: {location}\n")
            file.write(f"NIRF Ranking: {NIRF}\n")
            file.write(f"Ownership Type: {ownership}\n")
            for course_list in course_list:
                course_text = course_list.get_text().strip()  # Use get_text() instead of text
                file.write(f"Courses Offered: {course_text}\n")
            file.write(f"More Details: {link}\n\n")

    next_page(soup,stream)

stream=["law","medicine","engineering","pharmacy"]
for stream in stream:
    url=requests.get(f"https://{stream}.careers360.com/colleges/ranking").text
    soup=get_soup(url)
    get_data(soup,stream)


