from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from sys import platform

def scrape_with_selenium(url: str, selenium_headless: bool = True, return_format: str = "TEXT") -> tuple[WebDriver, str]:
    """Scrape text from a website using selenium
    Modified from: https://github.com/Significant-Gravitas/Auto-GPT/blob/86d3444fb8f9c46419dee88dd5c1fd1ff2be2ffa/autogpt/commands/web_selenium.py

    Args:
        url (str): The url of the website to scrape

    Returns:
        Tuple[WebDriver, str]: The webdriver and the text scraped from the website
    """
    options = ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36"
    )


    if platform == "linux" or platform == "linux2":
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")

    options.add_argument("--no-sandbox")
    if selenium_headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)

    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Get the HTML content directly from the browser's DOM
    page_source = driver.execute_script("return document.body.outerHTML;")
    soup = BeautifulSoup(page_source, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    
    if return_format=="TEXT":
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = "\n".join(chunk for chunk in chunks if chunk)
    elif return_format=="HTML":
        text = soup.prettify()
    driver.quit()
    return text

