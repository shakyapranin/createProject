import sys
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("REPO_PATH")

browser = webdriver.Chrome()
browser.get('https://github.com/login')

username = os.getenv("GITHUB_USERNAME")
password = os.getenv("GITHUB_PASSWORD")

def create():
    project_name = sys.argv[1]
    os.makedirs(path + str(project_name))

    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username) 
    python_button = browser.find_elements_by_xpath("//input[@name='password']")[0] 
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath("//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new') 
    python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0] 
    python_button.send_keys(project_name)
    python_button = browser.find_element_by_css_selector('button.first-in-line')
    python_button.submit()


if __name__ == '__main__':
    create()