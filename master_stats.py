from time import sleep
from selenium import webdriver
import json
# from selenium.webdriver.common.keys import Keys # nur für eintippen lassen

# Bums um weiterzumachen wenn Seite geladen ist
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# driver.get('https://www.mastersportal.com/search/#q=di-24|lv-master|tc-EUR')
# try:
#     numbResultsElem = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "ResultsNum")))
#     numbResults = int(numbResultsElem.text.split()[-1].replace(".", ""))
# except:
#     print("kein guter Start")
#     driver.quit()

BASEURL = 'https://www.mastersportal.com/search/#q=di-24|lv-master|tc-EUR&start='

# for i in range(0, numbResults, 10):
for i in range(10, 20, 10):
    driver.get(BASEURL + str(i))
    sleep(.2)
    try:
        studySearchResults = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "StudySearchResultsStudies")))
    except:
        print(f'Fehler bei Seite {i}')
        continue
    courseElement = studySearchResults.find_elements_by_class_name('Result')

    theseCourses = []
    for course in courseElement:
        title = course.find_element_by_class_name('StudyTitle').text
        uni = course.find_elements_by_class_name('LocationFact')[0].text
        location = course.find_elements_by_class_name('LocationFact')[1].text
        price = course.find_elements_by_class_name('KeyFact')[0].text
        duration = course.find_elements_by_class_name('KeyFact')[1].text
        discription = course.find_element_by_class_name('Description').text
        courseID = i + courseElement.index(course)
        extraFacts = []
        for fact in course.find_elements_by_class_name('ExtraFact'):
            extraFacts.append(fact.text)

        theseCourses.append({
            'id': courseID,
            # url
            'title': title,
            'uni': uni,
            'location': location,
            'price': price,
            'duration': duration,
            'extraFacts': extraFacts,  # hier evlt die Voraussetzung rausfiltern
            'discription': discription
        })

        print(courseID)

        # driver.back()

# print(allCourses)
with open("D:\OneDrive\Dokumente\Learnerino\py\master_stats.json", 'a') as json_file:
    json.dump(allCourses, json_file)
driver.quit()


# checken was passiert wenn man 2x driver get macht
