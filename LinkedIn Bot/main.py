from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to the ChromeDriver executable
chrome_driver_path = "E:/Applications/chromedriver-win64/chromedriver.exe"

# Create a Service object
service = Service(executable_path=chrome_driver_path)

# Optional: Set Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

# Initialize the ChromeDriver with Service and Options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open LinkedIn
driver.get("https://www.linkedin.com")


