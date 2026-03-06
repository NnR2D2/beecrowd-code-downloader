import time
from selenium import webdriver
from modules.helpers import get_max_pages_num, create_dir
from modules.login import login
from modules.scrape_answers import scrape_answers
from modules.scrape_source_code import scrape_code, write_to_file
from modules.constants import SUBMISSION_URL
from modules.github_api import github

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        login(driver)
        print("Login successful! Waiting for redirect...")
        time.sleep(5)

        total_pages = get_max_pages_num(driver)
        if total_pages is None:
            print("Could not detect total pages (login failed or page layout changed).")
            return

        create_dir("URI-Source-Codes")

        for cur_page in range(1, total_pages + 1):
            items = scrape_answers(driver, cur_page)

            for item in items:
                problem_id = item.get("problem_id", "").strip()
                exec_id = item.get("exec_id", "").strip()
                language = item.get("language", "").strip()

                if not exec_id:
                    continue

                driver.get(SUBMISSION_URL + exec_id)
                time.sleep(2)

                code_lines = scrape_code(driver)
                write_to_file(code_lines, problem_id, exec_id, language)

        print("All source codes were downloaded.")
        upload_to_github = input("Do you want to upload the source codes to GitHub? (Y/N): ").strip().upper()

        if upload_to_github == "Y":
            github()

    finally:
        driver.quit()

if __name__ == "__main__":
    main()