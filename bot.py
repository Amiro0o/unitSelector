# -*- coding: utf-8 -*-

import time
from selenium import webdriver

flag = False
driver = webdriver.Chrome()
driver.get("http://pooya.khayyam.ac.ir/gateway/PuyaAuthenticate.php")
while (not flag):
    


    

    driver.find_element_by_xpath("//*[@type='submit']").click()
    driver.get("https://pooya.khayyam.ac.ir/educ/stu_portal/ShowPreCSelsFormVorud.php")
    driver.find_element_by_xpath("//*[@type='submit']").click()
    driver.find_element_by_xpath("//*[@type='submit']").click()
    html_source = driver.page_source
    
    if ("زمان انتخاب واحد شما فرا نرسیده است" in html_source) or ("عدم قبول درخواست" in html_source):
        print (time.ctime()," : Your unit selection time has not arrived")
        time.sleep (5)
        driver.get("http://pooya.khayyam.ac.ir/gateway/SignOut.php")
    else:
        i = 0
        #Amiro0o   Andish     Az Fizi    Az Riz       Narm     Az Shab    Inter      Zaban B
        course = ["5410324", "5410334", "5410335", "5410414", "5410415", "5410905", "5414208"]
        code =   [   3     ,     2    ,     3    ,     2    ,     1    ,     1    ,     1    ]
        #vahd =  [   1     ,     3    ,     1    ,     3    ,     3    ,     1    ,     3    ]

        
        tables = driver.find_elements_by_tag_name("table")
        for i in range(len(course)):
            for col in driver.find_elements_by_tag_name("tr"):
                if len(col.find_elements_by_tag_name("td")) == 6 :
                    if col.find_elements_by_tag_name("td")[1].text == course[i] :
                        cell = col.find_element_by_id("LsnGrp[]")
                        cell.send_keys(code[i])
        driver.find_element_by_xpath("//*[@type='submit']").click()
        flag = True
#driver.quit()
