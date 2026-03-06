import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def create_dir(directory):
    """Creates a directory if it doesn't already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_web_element(element):
    """Extracts text from a Selenium WebElement."""
    return element.text.strip() if element else ""

def read_file(path):
    """Reads content from a file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    """Writes content to a file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def get_max_pages_num(driver):
    url = "https://judge.beecrowd.com/en/runs?answer_id=1&page=1"
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    time.sleep(3)

    # Collect all links that contain page=
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"page=")]')))
    except Exception:
        print("Warning: pagination links not found. Using 1 page.")
        return 1

    links = driver.find_elements(By.XPATH, '//a[contains(@href,"page=")]')

    max_page = 1
    for a in links:
        href = a.get_attribute("href") or ""
        m = re.search(r"[?&]page=(\d+)", href)
        if m:
            max_page = max(max_page, int(m.group(1)))

    print(f"Success! Total pages found: {max_page}")
    return max_page

