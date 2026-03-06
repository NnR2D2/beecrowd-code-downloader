import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    login_url = 'https://judge.beecrowd.com/en/login' # Updated URL
    driver.get(login_url)

    # 1. HARDCODED PAUSE for Cloudflare
    print("If you see a 'Verify you are human' box, click it now!")
    time.sleep(7) # Gives you time to manually solve any captcha

    wait = WebDriverWait(driver, 20)
    
    # 2. Modern Selectors
    # Beecrowd uses ID or NAME for these fields
    email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_field.send_keys("nnroy94@gmail.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("Beecrowd@01")

     # ... after entering email and password ...

    # 1. First, find the button (using the CSS selector for Beecrowd's current site)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")

    # 2. Now use JavaScript to click it (arguments[0] refers to submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    
    print("Login button clicked! Waiting for dashboard...")


