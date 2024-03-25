#Enter in terminal for installation:
#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup

with open("home.html","r")as html_file:
    content=html_file.read()
    soup=BeautifulSoup(content,"lxml")

    #scrapping using tag name
    # courses=soup.find_all("h5")
    # # print(courses) #prints full tag
    # for courses in courses:
    #     print(courses.text) #only prints text from the tag
    
    # fee=soup.find_all("a")
    # for fee in fee:
    #     print(fee.text)

    #scrapping using html classes
    #Note:when we specify which html class we are using as filter we 
    #need to mention it as class_ as class is also a keyword in python
    # course_card=soup.find_all("div",class_="card")
    # for i in course_card:
    #     name=i.h5.text
    #     fee=i.a.text.split()[-1]

    #     print(f"{name} costs {fee}")

    #write file
    course_card=soup.find_all("div",class_="card")
    with open("data.txt","a")as data_file:
        for i in course_card:
            name=i.h5.text
            fee=i.a.text.split()[-1]

            data_file.write(f"{name} costs {fee}\n")
    
    