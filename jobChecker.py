#Job checker checks if any new jobs are available at https://nursery.aerobotics.com/annotation-products

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

POLL_RATE = 10
browser = webdriver.Firefox()
notLogin = True
bellHasRung = False

#initialise vars
highFruit = 0
medFruit = 0
lowFruit = 0

highTree = 0
medTree = 0
lowTree = 0
while(1):
    
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
   
    #get the page
    browser.get('https://nursery.aerobotics.com/annotation-products')
    if notLogin:
        #Login
        email = browser.find_element_by_id("mat-input-0")
        email.send_keys("REDACTED")

        passwrd = browser.find_element_by_id("mat-input-1")
        passwrd.send_keys("REDACTED")

        submit = browser.find_element_by_class_name("mat-button-wrapper")
        submit.click()
        notLogin = False
        time.sleep(5)


    #wait for new page to load
    time.sleep(5)

    #check for fruit jobs
    #check High Priority Job for fruit finding
    try:
        highFruit = browser.find_element_by_xpath('/html/body/nur-root/nur-annotation-products/div/div/div[1]/div[3]/label')
        print "high fruit: "+highFruit.text
        #check Medium Priority Job for fruit finding
        medFruit = browser.find_element_by_xpath('/html/body/nur-root/nur-annotation-products/div/div/div[1]/div[2]/label')
        print "med fruit: "+medFruit.text
        #check High Priority Job for fruit finding
        lowFruit = browser.find_element_by_xpath('/html/body/nur-root/nur-annotation-products/div/div/div[1]/div[1]/label')
        print "low fruit: "+lowFruit.text
    except (NoSuchElementException, StaleElementReferenceException) as e:
        print "failed during fruit element searching"

    try:
        totalFruit = int(highFruit.text) + int(medFruit.text) + int(lowFruit.text)
    except ValueError:
        print "fruit values are null"

    try:
        #check for tree jobs
        #check High Priority Job for fruit finding
        highTree = browser.find_element_by_xpath('/html/body/nur-root/nur-annotation-products/div/div/div[2]/div[3]/label')
        print "high tree: "+highTree.text
        #check Medium Priority Job for fruit finding
        medTree = browser.find_element_by_xpath('/html/body/nur-root/nur-annotation-products/div/div/div[2]/div[2]/label')
        print "med tree: "+medTree.text
        #check High Priority Job for fruit finding
        lowTree = browser.find_element_by_xpath('/html/body/nur-root/nur-annotation-products/div/div/div[2]/div[1]/label')
        print "low tree: "+lowTree.text
    except (NoSuchElementException, StaleElementReferenceException)as e:
        print "failed during tree element searching"

    try:
        totalTree = int(highTree.text) + int(medTree.text) + int(lowTree.text)
    except ValueError:
        print "Tree values are null"
    print "total fruit: "+str(totalFruit)
    print "total tree: "+str(totalTree)

        #total all the jobs
    total = totalFruit+totalTree
    if total==0:
        bellHasRung = False

    if total>0:
        print str(total)+" jobs available"
        #ring bell 3 times
        i = 0
        if(not bellHasRung):
            bellHasRung = True
            while i != 3:
                print "\a"
                time.sleep(0.2)
                i = i+1


    #close tab
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 'w')
    
    #print a time stamp
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print current_time

    #make a new line
    print ""
    #wait for polling rate
    time.sleep(POLL_RATE)

