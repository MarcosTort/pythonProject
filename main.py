from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import requests
from difflib import SequenceMatcher
import numpy as np
texts_home = {

    "title": "Let's transform your ideas into sky-reaching apps",

    "sub_title": "Flutter Development Company ready to design, build and scale world-class software applications.",

    "Mobile App Development": "We build high-quality mobile applications with Flutter for both Android & iOS mobile devices in record time.",

    "Web Development": "We develop unique web apps with modern approaches and latest technologies to meet your business’ needs.",

    "UX/UI": "We are passionate about creating beautiful and practical user interfaces that provide a smooth and intuitive experience.",

    "Why we use Flutter": "Flutter has changed the game. Now you can transform your great ideas into applications from a single codebase that natively compiles for iOS, Android, Desktop, and Web. You can make the most of your productivity without having to waste time setting things up and still getting top-notch results.",

    "Full Product Development": "Transform your ideas into high-quality products through a full development cycle. Together we can build your dreamed mobile app or web from scratch and achieve a before-and-after in your industry. From strategy and design to development and delivery we are your trusted Software Development team.",

    "Staff Augmentation": "Finding the right person with the precise skills to join your in-house team is an incredible hard and expensive task, plus it takes time. We have a solution to that! We can reinforce your existing team with ours by bringing experienced developers to effectively meet project timelines.",

    "Jaac": "Jaac is a platform that improves customer service for restaurants and at the same time helps the restaurant to manage better and save revenue.",

    "CrimeDoor": "Crime database for the most notorious unsolved mysteries. You can be the detective and investigate the crime scenes with the use of augmented reality and other formats.",

    "ProWallet": "ProWallet is an instant payment solution for the construction industry that digitalizes and facilitates payment processes.",

    "Tony": "“The project was successful. Somnio Software tackled challenges head-on and created client-oriented solutions. They deliver what they promise within the timeframe that they promise.”",

    "Hassan": "“I was surprised to see the level of achievement reached for such a heavy project. I selected Somnio because we knew that they are not just regular programmers but mostly engineers that can think through any challenge.”",

    "TonyL": "“Their breadth of knowledge and professionalism impressed us. There's nothing that i could think of for them to do better. They knew what they were doing and they did a good job on that. They were excellent.”",

    "Trac": "“Somnio is our technical team that guides us in all the steps of the process to build a mobile application, giving us a better understanding of what is the current state, helping us define what we need, and suggesting next steps.”",

    "About us": "We are a team of passionate and creative engineers, developers, and designers that work hand in hand with our clients in order to build the best solutions for their needs.",

}

init(autoreset=True)
titles = texts_home.keys()
driver = webdriver.Chrome()
driver.get("http://www.somniosoftware.com")
diferentes = []
assert driver.title == 'Somnio Software | Flutter App & Web Development Company'
for x in titles:
    if texts_home[x] in driver.page_source:
        print(Fore.WHITE + x, Fore.GREEN + "Coincide" )

    else:
        diferentes.append(x)
        print(Fore.WHITE + x, Fore.RED + "Diferencias encontradas")
driver.close()


r = requests.get('http://www.somniosoftware.com')
soup = BeautifulSoup(r.text, 'lxml')
res = soup.find_all("p")
lista = []
for c in res:
    for d in diferentes:
        cad = str(c.string)
        try:
            print(SequenceMatcher(None, cad, texts_home[d]).ratio())
        except TypeError:
            print()




