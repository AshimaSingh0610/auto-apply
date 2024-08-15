from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to the ChromeDriver executable
chrome_driver_path = "E:\Applications\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object
service = Service(executable_path=chrome_driver_path)


# Initialize the ChromeDriver with Service and Options
driver = webdriver.Chrome(service=service)

# Open LinkedIn
driver.get("https://www.linkedin.com")



driver.close()


