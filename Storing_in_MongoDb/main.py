from bs4 import BeautifulSoup 
import requests
import pymongo

#set up mongo
def db_setup():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    myDb=client["College_Scrapped_Info"]
    return myDb

def insert_data(stream,link_data,myDb):
    myCol = myDb[f"{stream.capitalize()}_Data"]
    for i in link_data:
        doc=myCol.insert_one(i)
        print(doc)

#get data of a page
def get_soup(url):
    soup=BeautifulSoup(url,"lxml")
    return soup

#check if next page is available
def next_page(soup,stream):
    page=soup.find("a",class_="pagination_list_last")
    if page:
        next_link=requests.get(page["href"]).text
        new_soup=get_soup(next_link)
        get_data(new_soup,stream)
    else:
        return

#scrap and store data in .txt files
def get_data(soup,stream,link_data=[]):
    clg_details=soup.findAll("div",class_="tupple")
    for clg_details in clg_details:
        clg={}
        clg_name=clg_details.find("h3",class_="college_name").text.strip()
        clg["Name"]=clg_name
        location=clg_name.split()[-1]
        clg["Location"]=location
        NIRF=clg_details.find("div",class_="tupple_top_block_left").text.strip()
        clg["NIRF Ranking"]=NIRF
        ownership=clg_details.find("strong",class_="strong_ownership").text.strip()
        clg["Ownership"]=ownership
        course_list=clg_details.find_all("ul",class_="snippet_list")
        link=clg_details.h3.a["href"]
        clg["Link"]=link
        link_data.append(clg)
          
    next_page(soup,stream)

def scrapper(myDb):
    link_data=[]
    stream=["medicine","law","pharmacy","engineering"]
    for stream in stream:
        url=requests.get(f"https://{stream}.careers360.com/colleges/ranking").text
        soup=get_soup(url)
        get_data(soup,stream,link_data)
        insert_data(stream,link_data,myDb)

myDb=db_setup()
scrapper(myDb)


