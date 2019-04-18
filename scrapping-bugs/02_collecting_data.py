
# coding: utf-8

# # Import libraries

# In[ ]:


import os, glob, csv, sys, re
from os import path
import pandas as pd
from bs4 import BeautifulSoup
import tensorflow


# Set directory

# In[ ]:


userhome = os.path.expanduser("~")
datasource = userhome + r"/local-repo/scrapping-bugs/webdata/"
analyze_dir = userhome + r"/local-repo/scrapping-bugs/analyze/"


# In[ ]:

# Counting filenumber

file_list = glob.iglob(datasource + "*")
filenum = ";".join(file_list).split(';')
filenum.sort()
print ("Found " + str(len(filenum)) + " files")


# In[ ]:


filenum


# In[ ]:


num = '4033'
file = datasource + "webfile_page_AMQ-" + num + ".html"
f = open(file)
f = f.read()
print (f)


# In[ ]:


import pandas as pd

df1 = pd.DataFrame({'A': [0.1,0.2,0.3,0.1,0.2,0.3], 'B': [7,8,9,10,11,12], 'C': ['k','k','k','j','j','j']})
df2 = pd.DataFrame({'A': [1,2,3,1,2,3], 'B': [1,2,3,4,5,6], 'C': ['k','k','k','j','j','j']})

# df3 = pd.concat([df1[df1['C']=='k']['A'], df2[df2['C']=='k']['A']])
# df3.reset_index(drop=True,inplace=True)
df3=(df1[df1['C']=='k']['A']) + (df2[df2['C']=='k']['A'])
df3


# In[ ]:


job_list = ['assistant manager', 'salesperson', 'doctor', 'production manager', 
            'sales manager', 'schoolteacher', 'mathematics teacher']

def search_multiple_words(search_words):
    search_words = [search_words]

    for line in job_list:
        if any(word in line for word in search_words):
            print(line)

search_words = input("input keywords: ").split(' ')
for w in search_words:
    search_multiple_words(w)


# In[ ]:


import re
line = " say hi /* comment"
regex = re.compile(r'\s*(?P<command>.*?)/[/*](?P<optional>.*)')
result = regex.search(line)
print(result.group('command','optional'))


# In[ ]:


import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.idx.co.id/en-us/listed-companies/company-profiles/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

rows = soup.find_all('tr')
rows


# In[ ]:


from collections import defaultdict

tags = defaultdict(set)
for tag in soup():
    tags[tag.name] |= set(tag.attrs)

for tag_name in sorted(tags):
    print("{name}:{attrs}".format(name=tag_name, attrs=",".join(sorted(tags[tag_name]))))


# # Code trial

# In[ ]:


import collections

rtList = ["EVT","EVT","EVT","EVT","EVT","EVT","EVT","HIL"]
raList = ["C64G","C64R","C64O","C32G","C96G","C96R","C96O","RA96O"]

d = collections.defaultdict(list)

for k,v in zip(rtList, raList):
    d[k].append(v)


# In[ ]:


d


# # Scrape data from multiple URLs

# In[ ]:


import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url_list = ['https://nocable.org/browse-stations/callsign/cadenatres-linares-nl',
            'https://nocable.org/browse-stations/callsign/k27hm-d-quanah-tx',
            'https://nocable.org/browse-stations/callsign/ksnb-tv-superior-ne'
           ]

data = []
for url in url_list:
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    urldict = {}
    tr = soup.find_all('tr')
    for row in tr:
        th = soup.find_all('th')
        td = soup.find_all('td')

    for item in range(0,len(th)):    
        urldict.update({th[item].text:td[item].text})

    data.append(urldict)
data


# In[ ]:


cols = []
for d in range(0,len(data)):
    for i in data[d].keys():
        if i not in cols:
            cols.insert(len(cols),i)
cols


# In[ ]:


with open('file_url.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, cols)
    dict_writer.writeheader()
    dict_writer.writerows(data)


# In[ ]:


df = pd.read_csv("file_url.csv")
df


# In[ ]:


import urllib, sys
from urllib.request import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib.request.urlopen(page)
                except:
                    print ("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), "lxml")
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)
        pages = indexed_url
    return indexed_url


# In[ ]:


mainpage = ["http://yusufsn.staff.ums.ac.id/"]
urls = crawl(mainpage, depth=2) # you can configure this number to set the depth of pages

table = 0
for r, url in enumerate (urls):
    sys.stdout.write("\rExtracting url %i" %(r+1) + " from %i" % (len(urls)) + " url")
    sys.stdout.flush()
    try:
        df = pd.read_html(url)
        if df:
            table += 1
    except:
        pass
print ("\nNumber of table = %i" %(table))


# In[ ]:


table = 0
for url in urls:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        table = len(soup) + table
    except:
        pass
print (table)


# In[ ]:


import pandas as pd

url = 'https://web.stanford.edu/class/cs101/table-data.html'
dfs=pd.read_html(url)

print ("Number of table: %i" % len(dfs))


# In[ ]:


import requests
from bs4 import BeautifulSoup

r = requests.get(url)
soup=BeautifulSoup(r.text,'lxml')

len(soup.find_all('table'))


# # Regex

# In[ ]:


import re

mylist = ['2.1 [ii] Agreement and Plan of Reorganization, by and among the Company, Force Acq. Corp. and Force Computers, Inc. as amended.',
          '3.1 [viii] Articles of Incorporation of Company, as amended.',
          '3.2 [viii] Bylaws of Company.',
          '10.1 [I] Preferred Stock Purchase Agreement dated September 29, 1983, together with amendments thereto dated February 28, 1984 and',
          '10.2 [I] Form of Indemnification Agreement between Company and its officers, directors and certain other key employees.'
         ]
for item in mylist:
    regex = re.search('(?P<chapter>\d+[.]\d+)\s+(?P<subchapter>\[.*\])\s+(?P<title>.*)', item)
    regex = regex.groups()
    print (regex[0], regex[1], regex[2])


# # List

# In[ ]:


My_List = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

#Outcome =[[1,2,3],[4,5,6],[7,8,9]]
outcome = My_List[:-3]
outcome


# # Physics

# In[ ]:


def getInput():
        h = int(input("Enter the initial height of the ball: "))
        v = int(input("Enter the initial velocity of the ball: "))
        isValid(h,v)

def isValid(h,v):
    if (h<= 0):
        print("Please enter positive values")

    elif(v<= 0):
        print("Please enter positive values")

    else:
        height = maxHeight(h,v)
        print("The maximum height of the ball is", height, "feet.")
        groundTime = ballTime(h,v)
        print("The ball will hit the ground after approximately", groundTime, "seconds.")


def maxHeight(h,v):
    t = (v/32)
    maxH = (h + (v*t) - (16*t*t))
    return maxH


def ballTime(h,v):
    t = 0.1
    while(True):
        ballHeight = (h + (v*t) - (16*t*t))
        if (ballHeight <= 0):
            break
        else:
            t += 0.1

    return t

getInput()


# In[ ]:


def load_data(file_name):
    university_data=[]
    with open(file_name,'r') as rd_file:
        for line in rd_file.readlines():
            line=line.strip().split(',')
            T = line[0],line[1]
            university_data.append(T)
    return university_data

def search(key, mydata):
    for l in mydata:
        if key in (''.join(l)).lower():
            print('University: %s Name: %s' % (l[0], l[1]))

def main():
    filename='list.txt'
    university_data = load_data(filename)
    print('[1] University\n[2] Contact Name\n[3] Exit\n[4] Search')
    while True:

        choice=input('Enter choice 1/2/3? ')
        if choice=='1':
            for university in university_data:
                print(university[0])
        elif choice=='2':
            for university in university_data:
                print(university[1])
        elif choice =='3':
            print('Thank You')
            break
        elif choice =='4':
            words = str(input('Enter your word to search:'))
            search(words,university_data)
        else:
            print('Invalid selection')

main()


# # Text-based game

# In[ ]:


import time
import random

def  game():
#intro text
    print('******************************')
    print('     Welcome to the game!')
    print('*******************************')

time.sleep(1)

print('You awaken in a cave, unable to see. Darkness surrounds you.')
time.sleep(1)
print('\nSuddenly a small flickering light is seen in the distance.')
time.sleep(1)
print('\nyou get on your feet and decide wether you should head towards the light or wait where you are and hope help finds its way.')

#first question
def firstquestion():
    while True:
        print('\nDo you get up and see what could be the source of this light? \nOr do you wait?')
        Answer = input()
        if Answer == 'get up' or Answer == 'I get up':
            print('You begin to walk towards the light.')
            break
        elif Answer == 'wait':
            print('you wait, no one comes and you die...')
            break
        else:
            print('try again...')
    #second question
def secondquestion():
    while True:
        print('\nThe light turns out to be a torch. Do you take this torch? enter y / n. ')
        Answer = input()
        if Answer == 'y':
            print('good choice, you pick up the torch and walk the out of the cave.')
            break
        elif Answer == 'n':
            print('well now your blind and dead...')
            break
        else:
            print('try again...')

game()
firstquestion()
secondquestion()
print()


# In[ ]:


d = {'Pass_ID': [100,101,102,103], 'Actual': [1,0,1,1], 'Modeled':[1,1,0,1]}
df = pd.DataFrame(data=d)
df


# In[ ]:


def isolate_diff(df):
    print(df[df['Modeled']!=df['Actual']])
    print(df.loc[df['Modeled']!=df['Actual'],'Pass_ID'].tolist())


# In[ ]:


isolate_diff(df)


# In[ ]:


s = df[df.Pass_ID != 100]
s


# In[ ]:


occupation_lst = ['ALL OCCUPATIONS', 'MANAGEMENT', 'Chief executives', 'General and operations managers', 'Marketing and sales managers', 'Administrative services managers', 'Computer and information systems managers', 'Financial managers', 'Human resources managers', 'Industrial production managers', 'Purchasing managers', 'Transportation storage and distribution managers', 'Farmers ranchers and other agricultural managers', 'Construction managers', 'Education administrators', 'Architectural and engineering managers', 'Food service managers', 'Lodging managers', 'Medical and health services managers', 'Property real estate and community association managers', 'Social and community service managers', 'Managers all other', 'BUSINESS', 'Wholesale and retail buyers except farm products', 'Purchasing agents except wholesale retail and farm products', 'Claims adjusters appraisers examiners and investigators', 'Compliance officers', 'Cost estimators', 'Human resources workers', 'Logisticians', 'Management analysts', 'Market research analysts and marketing specialists', 'Business operations specialists all other', 'Accountants and auditors', 'Financial analysts', 'Personal financial advisors', 'Credit counselors and loan officers', 'COMPUTATIONAL', 'Computer systems analysts', 'Information security analysts', 'Computer programmers', 'Software developers applications and systems software', 'Web developers', 'Computer support specialists', 'Database administrators', 'Network and computer systems administrators', 'Computer network architects', 'Computer occupations all other', 'Operations research analysts', 'ENGINEERING', 'Architects except naval', 'Aerospace engineers', 'Chemical engineers', 'Civil engineers', 'Computer hardware engineers', 'Electrical and electronics engineers', 'Industrial engineers including health and safety', 'Mechanical engineers', 'Engineers all other', 'Drafters', 'Engineering technicians except drafters', 'Surveying and mapping technicians', 'SCIENCE', 'Medical scientists', 'Chemists and materials scientists', 'Environmental scientists and geoscientists', 'Physical scientists all other', 'Miscellaneous life physical and social science technicians', 'SOCIAL SERVICE', 'Counselors', 'Social workers', 'Clergy', 'LEGAL', 'Lawyers', 'EDUCATION', 'Postsecondary teachers', 'Elementary and middle school teachers', 'Secondary school teachers', 'Other teachers and instructors', 'ARTS', 'Designers', 'Producers and directors', 'Athletes coaches umpires and related workers', 'Editors', 'Broadcast and sound engineering technicians and radio operators', 'HEALTHCARE PROFESSIONAL', 'Pharmacists', 'Physicians and surgeons', 'Physical therapists', 'Registered nurses', 'Clinical laboratory technologists and technicians', 'Diagnostic related technologists and technicians', 'Emergency medical technicians and paramedics', 'Health practitioner support technologists and technicians', 'HEALTHCARE SUPPORT', 'Nursing psychiatric and home health aides', 'PROTECTIVE SERVICE', 'First-line supervisors of police and detectives', 'First-line supervisors of protective service workers all other', 'Firefighters', 'Bailiffs correctional officers and jailers', 'Detectives and criminal investigators', "Police and sheriff's patrol officers", 'Security guards and gaming surveillance officers', 'CULINARY', 'Chefs and head cooks', 'First-line supervisors of food preparation and serving workers', 'Cooks', 'Food preparation workers', 'Bartenders', 'Combined food preparation and serving workers including fast food', 'Waiters and waitresses', 'Dining room and cafeteria attendants and bartender helpers', 'Dishwashers', 'GROUNDSKEEPING', 'First-line supervisors of housekeeping and janitorial workers', 'First-line supervisors of landscaping lawn service and groundskeeping workers', 'Janitors and building cleaners', 'Maids and housekeeping cleaners', 'Pest control workers', 'Grounds maintenance workers', 'SERVICE', 'First-line supervisors of gaming workers', 'Baggage porters bellhops and concierges', 'Personal care aides', 'Recreation and fitness workers', 'SALES', 'First-line supervisors of retail sales workers', 'First-line supervisors of non-retail sales workers', 'Cashiers', 'Parts salespersons', 'Retail salespersons', 'Advertising sales agents', 'Insurance sales agents', 'Securities commodities and financial services sales agents', 'Sales representatives services all other', 'Sales representatives wholesale and manufacturing', 'Real estate brokers and sales agents', 'Sales and related workers all other', 'OFFICE', 'First-line supervisors of office and administrative support workers', 'Bill and account collectors', 'Bookkeeping accounting and auditing clerks', 'Customer service representatives', 'Hotel motel and resort desk clerks', 'Receptionists and information clerks', 'Couriers and messengers', 'Dispatchers', 'Postal service clerks', 'Postal service mail carriers', 'Production planning and expediting clerks', 'Shipping receiving and traffic clerks', 'Stock clerks and order fillers', 'Secretaries and administrative assistants', 'Data entry keyers', 'Insurance claims and policy processing clerks', 'Office clerks general', 'Office and administrative support workers all other', 'AGRICULTURAL', 'Miscellaneous agricultural workers', 'CONSTRUCTION', 'First-line supervisors of construction trades and extraction workers', 'Brickmasons blockmasons and stonemasons', 'Carpenters', 'Carpet floor and tile installers and finishers', 'Construction laborers', 'Operating engineers and other construction equipment operators', 'Drywall installers ceiling tile installers and tapers', 'Electricians', 'Painters construction and maintenance', 'Pipelayers plumbers pipefitters and steamfitters', 'Roofers', 'Sheet metal workers', 'Structural iron and steel workers', 'Construction and building inspectors', 'Highway maintenance workers', 'Mining machine operators', 'Other extraction workers', 'MAINTENANCE', 'First-line supervisors of mechanics installers and repairers', 'Computer automated teller and office machine repairers', 'Radio and telecommunications equipment installers and repairers', 'Security and fire alarm systems installers', 'Aircraft mechanics and service technicians', 'Automotive body and related repairers', 'Automotive service technicians and mechanics', 'Bus and truck mechanics and diesel engine specialists', 'Heavy vehicle and mobile equipment service technicians and mechanics', 'Miscellaneous vehicle and mobile equipment mechanics installers and repairers', 'Heating air conditioning and refrigeration mechanics and installers', 'Industrial and refractory machinery mechanics', 'Maintenance and repair workers general', 'Electrical power-line installers and repairers', 'Telecommunications line installers and repairers', 'Precision instrument and equipment repairers', 'Other installation maintenance and repair workers', 'PRODUCTION', 'First-line supervisors of production and operating workers', 'Electrical electronics and electromechanical assemblers', 'Miscellaneous assemblers and fabricators', 'Bakers', 'Butchers and other meat poultry and fish processing workers', 'Food processing workers all other', 'Computer control programmers and operators', 'Cutting punching and press machine setters operators and tenders metal and plastic', 'Machinists', 'Welding soldering and brazing workers', 'Metal workers and plastic workers all other', 'Printing press operators', 'Laundry and dry-cleaning workers', 'Stationary engineers and boiler operators', 'Water and wastewater treatment plant and system operators', 'Chemical processing machine setters operators and tenders', 'Crushing grinding polishing mixing and blending workers', 'Inspectors testers sorters samplers and weighers', 'Packaging and filling machine operators and tenders', 'Painting workers', 'Production workers all other', 'TRANSPORTATION', 'Supervisors of transportation and material moving workers', 'Aircraft pilots and flight engineers', 'Bus drivers', 'Driver/sales workers and truck drivers', 'Taxi drivers and chauffeurs', 'Railroad conductors and yardmasters', 'Automotive and watercraft service attendants', 'Crane and tower operators', 'Industrial truck and tractor operators', 'Cleaners of vehicles and equipment', 'Laborers and freight stock and material movers hand', 'Packers and packagers hand', 'Refuse and recyclable material collectors']
m_weekly_lst = [895, 1486, 2251, 1347, 1603, 1451, 1817, 1732, 1495, 1528, 1404, 1006, 847, 1357, 1585, 1892, 820, 1171, 1422, 1137, 1142, 1525, 1327, 886, 1020, 1134, 1375, 1264, 1158, 1075, 1519, 1411, 1461, 1345, 1680, 1738, 1186, 1503, 1462, 1562, 1501, 1751, 1233, 1135, 1829, 1266, 1577, 1252, 1574, 1452, 1492, 1668, 1583, 1474, 1871, 1819, 1430, 1550, 1537, 977, 984, 1031, 1379, 1362, 1496, 1740, 1770, 1001, 973, 908, 943, 1021, 1877, 1914, 1144, 1405, 1077, 1149, 1024, 1088, 1099, 1340, 818, 1205, 937, 1272, 2117, 1915, 1347, 1222, 1089, 1106, 899, 652, 577, 526, 851, 1425, 825, 1052, 779, 1265, 1001, 592, 481, 656, 621, 427, 414, 569, 401, 501, 389, 401, 517, 700, 653, 547, 475, 591, 473, 597, 900, 606, 537, 684, 880, 825, 1140, 471, 600, 694, 1155, 1028, 1461, 1147, 1066, 1052, 1088, 693, 878, 674, 690, 690, 486, 619, 750, 759, 974, 1021, 978, 604, 537, 786, 589, 762, 609, 852, 477, 460, 751, 1047, 652, 687, 634, 642, 859, 595, 891, 587, 862, 580, 776, 864, 965, 755, 1098, 918, 842, 1033, 865, 879, 913, 1032, 849, 724, 830, 928, 591, 810, 894, 771, 1105, 880, 1009, 810, 729, 924, 566, 637, 570, 582, 679, 857, 674, 840, 767, 678, 729, 487, 1012, 868, 1082, 668, 844, 605, 733, 666, 679, 898, 1830, 681, 751, 600, 1137, 470, 1016, 612, 498, 547, 462, 496]
f_weekly_lst = [726, 1139, 1836, 1002, 1258, 981, 1563, 1130, 1274, 0, 1226, 749, 0, 0, 1252, 0, 680, 902, 1156, 823, 965, 1213, 1004, 985, 986, 824, 1025, 0, 984, 0, 1348, 1239, 969, 988, 1171, 1033, 906, 1245, 1256, 0, 1302, 1415, 1026, 908, 0, 0, 0, 1145, 1325, 1257, 0, 0, 0, 0, 0, 0, 0, 0, 1448, 0, 827, 0, 1067, 1082, 0, 0, 1170, 780, 845, 902, 862, 924, 1135, 1717, 907, 1144, 957, 1006, 817, 942, 918, 1234, 0, 1125, 0, 991, 1811, 1533, 1215, 1098, 796, 908, 0, 633, 490, 457, 655, 0, 0, 0, 686, 0, 1009, 515, 414, 492, 458, 400, 388, 493, 380, 411, 0, 0, 419, 571, 0, 429, 407, 0, 0, 475, 680, 0, 441, 526, 578, 614, 896, 405, 0, 494, 729, 717, 767, 699, 917, 735, 727, 646, 781, 648, 692, 604, 467, 569, 0, 655, 833, 854, 732, 566, 506, 683, 638, 675, 622, 718, 437, 398, 704, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 761, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 519, 623, 544, 512, 475, 463, 508, 0, 0, 0, 0, 581, 0, 460, 0, 0, 0, 0, 583, 482, 0, 501, 494, 0, 0, 572, 632, 0, 0, 0, 0, 0, 0, 455, 424, 0]

missing_data_occupations = []
for x,y,z in zip(occupation_lst, m_weekly_lst, f_weekly_lst):
    word = "less" if y - z > 0 else "more"
    amount = y - z if y - z > 0 else z - y
    print (x + ":" + " Female workers make " + "$" + str(amount) + "/week " + word + " than male workers.")
    
# for x in range (0,len(occupation_lst)):
#     col_occ = occupation_lst[x]
#     col_m = m_weekly_lst[x]
#     col_f = f_weekly_lst[x]
    
#     diff = abs(col_m - col_f)
#     if col_m > col_f:
#         status = "Male workers make $" + str(diff) + "/week more than Female workers."
#     elif col_m < col_f:
#         status = "Female workers make $" + str(diff) + "/week more than Male workers."
#     else:
#         status = "Both Male and Female workers make same amount of salary $" + str(diff)
#     print (col_occ + ": " + status)


# In[ ]:


import numpy as np

df = pd.DataFrame({'A': [1.6,1.2,3.9,4.5, np.nan]})  
df['B'] = df['A'] 
df


# In[ ]:


import glob,os

words = ['Thank you for being a loyal customer.',
         'Thank you for being a horrible customer.',   
         'Thank you for being a nice customer.']    

def convert(path):
    a = []
    z = 0
    for files in glob.glob(path + "/*.csv"):
        temp = [words[z],files]
        a.append(temp)
        z += 1
    print (a)

dirs = os.path.expanduser('~')
convert(dirs + '/local-repo/scrapping-bugs')


# In[ ]:


import time

def hi ():
    i = int(input("Enter the max number of iteration: "))
    s = input("Enter the string to print: ")
    for n in range(i):
        print(n+1, s)
        time.sleep(1)
        
hi()


# In[ ]:


import more_itertools as mit

my_list = [1,2,3,4,5, 9,10,11,12,13,14, 20,21,22,23,24,25,26,27]

x = [list(group) for group in mit.consecutive_groups(my_list)]

output = []
for i in x:
    temp = [i[0],i[1],i[-2],i[-1]]
    output.extend(temp)    
output


# In[ ]:


import sys, time

x = 10
while x>=0:
    if x < 10:
        s = '0' + str(x)
    else:
        s = str(x)
    sys.stdout.write("\rCounting down: " + s)
    sys.stdout.flush()
    time.sleep(1)
    x -= 1
print ("\nYour time is over")


# In[ ]:


import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://dnedesign.us.to/tables/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

status = []
for rows in soup.find_all('tr'):
    x = 0
    for td in rows.find_all('td'):      
        if 'a:' in td.text:
            status.append(td.text[4:])
            print(td.text[4:])


# In[ ]:


import re

time = []
for rg in status:
    try:
        regex = re.search(".*\"(?P<day>\w*day).*\"(?P<starttime>\d+:\d+).*\"(?P<endtime>\d+:\d+)",rg)
        regex = regex.groups()
        temp = [regex[0], regex[1], regex[2]]
    except:
        regex = re.search(".*\"(?P<day>\w*day)",rg)
        regex = regex.groups()
        temp = [regex[0]]
    time.append(temp)

print (time)


# In[ ]:


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])


# In[ ]:


import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://dnedesign.us.to/tables/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

status = []
for div in soup.find_all('div'):
    try:
        print ('id : ' + ''.join(div['id']))
        print ('class : ' + ' '.join(div['class']))
        print()
    except:
        pass


# In[ ]:


stuff = []
N = int(input("Enter the size of N: "))
for n in range(N):
    s = input("Enter stuff %i : " %(n+1))
    stuff.append(str(s))   

for ss in range(len(stuff)):
    st = stuff[ss]
    for x in range(ss+1, len(stuff)):
        comb = st + stuff[x]
        print (comb)


# In[ ]:


from itertools import combinations   

stuff = []
N = int(input("Enter the size of N: "))
for n in range(N):
    s = input("Enter stuff %i : " %(n+1))
    stuff.append(str(s)) 
    
result = [''.join(i) for i in combinations(stuff, 2)]
print (result)


# In[ ]:


type(result)


# In[ ]:


string = input()
# string = string.replace('word', 'word.2')
word = string.find('word')
if word >= 0:
    string = string.replace('word', 'word.2')
print(string)


# In[ ]:


import pandas as pd

df = pd.DataFrame({'Col1':['A','B','C','D','E'], 'Col2': [4,2,6,3,2], 'Col3':[3,6,4,3,1]})        
for x in range(len(df)):
    dt = df.iloc[x]
    if dt[1] > dt[2]:
        print ('Col2:{}'.format(dt[1]))
    elif dt[1] < dt[2]:
        print ('Col3:{}'.format(dt[2]))
    else:
        print ('Both cols are same')


# In[ ]:


df = pd.DataFrame({'Col1':['A','B','C','D','E'], 'Col2': [4,2,6,3,2], 'Col3':[3,6,4,3,1]})
for key in df:
    print (key)


# In[ ]:


iput = []
final = []

while True:
    iput += [input('Enter words here: ')]
    if not iput[-1]:
        break

z = 1
while i < len(iput) - 1:
    print(i)
while iput[i][0] != iput[i][z]:
    if z == len(iput[i]):
        break
        z += 1
        i += 1

print(final)


# In[ ]:


import re

text = 'star *tar s*ar st*r sta* (*tar) (sta*) sta*.'

p = re.findall(r'[\w*]+', text)
print(p)


# In[ ]:


def square(x):
    temp = []
    for num in x:
        temp.append(int(math.pow(num,2)))
    return temp

chunks = [[1,2,3],[4,5,6],[7,8,9]]
text = []
for ch in range(len(chunks)):
    text.append(square(chunks[ch]))
text


# # Timing

# In[ ]:


import time

# timeout variable can be omitted, if you use specific value in the while condition
# timeout = 10   # [seconds]

timeout_start = time.time()
test = 1
while time.time() < timeout_start + timeout:
    print (test)
    time.sleep(1)
    if test == 5:
        break
    test += 1


# In[ ]:


import time
import random
import datetime

class TimeoutException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def busy_work():

    # Pretend to do something useful
    time.sleep(random.uniform(0.3, 0.6))

def train_loadbatch_from_lists(batch_size, timeout_sec):

    time_start = datetime.datetime.now()
    batch_xs = []
    batch_ys = []

    for i in range(0, batch_size+1):
        busy_work()
        batch_xs.append(i)
        batch_ys.append(i)

        time_elapsed = datetime.datetime.now() - time_start
        print ('Elapsed:', time_elapsed)
        if time_elapsed > timeout_sec:
            raise TimeoutException()

    return batch_xs, batch_ys

def main():
    timeout_sec = datetime.timedelta(seconds=5)
    batch_size = 10
    try:
        print ('Processing batch')
        batch_xs, batch_ys = train_loadbatch_from_lists(batch_size, timeout_sec)
        print ('Completed successfully')
        print (batch_xs, batch_ys)
    except (TimeoutException, e):
        print ('Timeout after processing N records')

if __name__ == '__main__':
    main()


# In[ ]:


import multiprocessing.pool
import functools

def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator


# In[ ]:


# if execution takes longer than 5 seconds, raise a TimeoutError
@timeout(5.0)
def sss():
    x = []
    for i in range(100000000):
        x.append(i)
    return x


# In[ ]:


sss()


# In[ ]:


my = ['hellloworld@gmail.com']

my[0].replace("'","")
my


# In[ ]:


a = [1, 2, 2]
b = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]
c = a + b
list(set(c))
# new = []
# for i in c:
#     if i not in new:
#         new.append(i)

# print(new)


# In[ ]:


x = pd.dataframe([1,2,3],[4,5,6])
x

