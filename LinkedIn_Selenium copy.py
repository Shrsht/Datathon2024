import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
import pickle

options = Options()
options.add_experimental_option('detach',True)

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
good = []

### LOG INTO LINKED-IN FUNCTION:
def login_linkedin(driver,p):
    url = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    wait = WebDriverWait(driver,10)
    driver.get(url)

    username = driver.find_element(By.ID,"username")
    username.send_keys("shresht.v24@gmail.com")
    password = driver.find_element(By.ID,'password')
    password.send_keys(p)

    #### CLICK LOG-IN BUTTON:
    driver.find_element(By.CLASS_NAME,"login__form_action_container").click()



### FIND DATA SCIENCE JOBS:
def search(driver):
    time.sleep(5)
    ### LINKEDIN KEYWORD SEARCH FOR "data science" jobs:
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3776673215&keywords=Data%20Scientist&origin=SWITCH_SEARCH_VERTICAL")


# ### FINDS RESULTS OF SEARCH AND GRABS
# def get_n_results(driver):
#     time.sleep(10)

#    ### GETS THE INDIVIDUAL JOB
#     results_div = driver.find_element(By.XPATH,f"/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small")
 
#   ### CONVERTS TO STRING:
#     n_string = results_div.text
#     n = int(n_string.split()[0].replace(',',""))
#     return n 

def get_jobs(driver):
  ul_div = driver.find_element(By.XPATH,f"/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul")
  return ul_div 

#SCROLLS DOWN:
def scroll_down(driver):
  for i in np.linspace(0,1,10):
    time.sleep(2)
    driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight*{i})")

def get_job_urls(jobs,driver,job_urls = {}):
  i = 1
  #Collects job urls,location role cand company 
  #the final result updates the input dictionary and appends a key value pair with the format
  #    url:{'company':company,'location':location,'role':role}
  while True: 
    try:
      WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]')))
      url = jobs.find_element(By.XPATH,f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[1]/a').get_attribute("href")
      role = jobs.find_element(By.XPATH,f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[1]/a').text
      company = jobs.find_element(By.XPATH,f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[2]/span').text
      location = driver.find_element(By.XPATH,f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[3]/ul/li').text
      job_urls.update({url:{'company':company,'location':location,'role':role}})
      i+=1
    except:
      return job_urls

def load_next_page(driver):
  #loads next page for url retrival
  curr= driver.find_element(By.XPATH,f'//*[@aria-current="true"]').text ## TESTED CORRECT
  next = driver.find_element(By.XPATH,f'//*[@aria-label="Page {int(curr)+1}"]') ## TESTED CORRECT
  next.click()

def get_description(driver,job_dict,good):

  fail = []
  #Iterate through the url list to scrape the descriptions
  for url in list(job_dict.keys()):
    if url not in good:
      try:
        driver.get(url)
        time.sleep(3)
        if driver.current_url != url:
          print(f'failed at {url}')
          #remove borken urls
          job_dict.pop(url)
        #scrape
        driver.find_element(By.XPATH,'//*[@aria-label="Click to see more description"]').click() ##TESTED CORRECT
        description = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[2]/article/div/div[1]/span').text #/html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[2]/article/div/div[1]/span
        job_dict.get(url).update({"description":description})
        good.append(url)
        return job_dict
      except:
        #keep going if there is a random error in which a div did not load properly but check where we failed
        print(f"fail {job_dict.get(url)}")
        fail.append(url)

#Run through the entire process of fetch in urls logining in and grabing job descriptions
def main(driver,password):
    login_linkedin(driver,password)
    search(driver)
    #n = get_n_results(driver)
    job_dict ={}
    #iterate through the amount of pages given
    for i in range(40):
        jobs = get_jobs(driver)
        scroll_down(driver)
        get_job_urls(jobs,driver,job_urls = job_dict)
        load_next_page(driver)
    get_description(driver,job_dict,good)

    return get_description(driver,job_dict,good)


# p = open("../../pass.txt", "r").read()
# type(p)

# driver = webdriver.Chrome(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
# f = open("../../pass.txt", "r").read()
# main(driver,f)



def save(final_file):
    with open(f'Desktop/Selenium Project/{final_file}.p', 'wb') as fp:
        pickle.dump(final_file,file=fp,protocol=pickle.HIGHEST_PROTOCOL)
def load():
    with open('Desktop/Selenium Project/job_dict.p', 'rb') as fp:
        job_dict = pickle.load(fp)


### RUNNING AND TESTING:

# login_linkedin(driver,'Nengmyeonchuseyo24')
# search(driver)
# test_jobs = get_jobs(driver)
# scroll_down(driver)
#get_job_urls(test_jobs,driver,job_urls = {})

final_file = main(driver,"Nengmyeonchuseyo24")

save(final_file)



## NEW LINE 57 XML PATH
#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul

## ORIGINAL LINE 57 XML PATH
#/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul"
#/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul

## NEW LINE 74 XML PATH - URL OF JOB POSTING
#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[1]/a

## NEW LINE 76 XML PATH - NAME OF COMPANY
#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[2]/span

## NEW LINE 77 XML PATH - LOCATION
#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{i}]/div/div[1]/div/div[2]/div[3]/ul/li

### LINE 85 TEST:
# Page 1:
#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[6]/ul/li[1]
# Page 2:
#/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/div[6]/ul/li[2]