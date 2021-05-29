from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import parameters

driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://linkedin.com')

time.sleep(2)

username=driver.find_element_by_xpath("//input[@name='session_key']")
password=driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys(parameters.linkedin_username)
password.send_keys(parameters.linkedin_password)
time.sleep(2)

submit=driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

import random
n_pages=3
for n in range(1,n_pages):
    driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=lTC&page='+str(n))
    time.sleep(2)

    all_buttons = driver.find_elements_by_tag_name('button')
    message_button = [btn for btn in all_buttons if btn.text == 'Message']

    for i in range(0, len(message_button)):
        driver.execute_script('arguments[0].click();', message_button[i])
        time.sleep(2)
        main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
        driver.execute_script('arguments[0].click();', main_div)
        paragraph = driver.find_elements_by_tag_name("p")
        all_span = driver.find_elements_by_tag_name("span")
        all_span = [s for s in all_span if s.get_attribute("aria-hidden") == "true"]

        idx = [*range(3, 18, 2)]
        greetings = ["Hello", "Hi", "Hey", "Ahoy", "Yo yo", "Sup"]
        all_names=[]
        for j in idx:
            name = all_span[j].text.split(" ")[0]
            all_names.append(name)

        greetings_idx = random.randint(0, len(greetings) - 1)
        message=greetings[greetings_idx] + " " + all_names[i] + ", Sorry, I didnt mean to bother you. This is a Automated message. Thanks!"
        paragraph[-5].send_keys(message)
        time.sleep(2)
        submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script('arguments[0].click();', close_button)
        time.sleep(2)



