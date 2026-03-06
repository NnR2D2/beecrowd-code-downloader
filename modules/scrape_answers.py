import time
import re
from selenium.webdriver.common.by import By
from .constants import SUBMISSIONS_LIST

def _header_indexes(driver):
    headers = driver.find_elements(By.XPATH, "//table//thead//th")
    idx = {}
    for i, th in enumerate(headers):
        key = (th.text or "").strip().lower()
        if key:
            idx[key] = i
    return idx

def _pick_index(header_idx, candidates):
    for c in candidates:
        if c in header_idx:
            return header_idx[c]
    return None

def scrape_answers(driver, page_num: int):
    url = f"{SUBMISSIONS_LIST}{page_num}"
    print(f"Navigating to: {url}")
    driver.get(url)
    time.sleep(3)

    header_idx = _header_indexes(driver)

    # Pick columns by header text (beecrowd varies)
    lang_i = _pick_index(header_idx, ["language", "compiler", "lang"])
    # (Problem ID we already pull from /problems/view/<id>, so no need for td index)

    rows = driver.find_elements(By.XPATH, "//table//tbody/tr")
    results = []

    for row in rows:
        # ---- numeric problem id from link ----
        problem_id = ""
        try:
            prob_a = row.find_element(By.XPATH, './/a[contains(@href, "/problems/view/")]')
            href = prob_a.get_attribute("href") or ""
            m = re.search(r"/problems/view/(\d+)", href)
            if m:
                problem_id = m.group(1)
        except Exception:
            pass

        # ---- exec id from /runs/code/<id> ----
        exec_id = ""
        try:
            a = row.find_element(By.XPATH, './/a[contains(@href, "/runs/code/")]')
            href = (a.get_attribute("href") or "").rstrip("/")
            exec_id = href.split("/")[-1]
        except Exception:
            pass

        # ---- language from the correct column ----
        language = ""
        try:
            tds = row.find_elements(By.XPATH, "./td")
            if lang_i is not None and lang_i < len(tds):
                language = (tds[lang_i].text or "").strip()
        except Exception:
            pass

        # Fallback: try to find any td that looks like a language string
        if not language:
            try:
                for td in row.find_elements(By.XPATH, "./td"):
                    txt = (td.text or "").strip()
                    low = txt.lower()
                    if any(k in low for k in ["c++", "python", "java", "javascript", "c#", "golang", " go", "rust", "kotlin", "c99", "c11"]):
                        language = txt
                        break
            except Exception:
                pass

        if exec_id:
            results.append({"problem_id": problem_id, "exec_id": exec_id, "language": language})

    if results:
        print("Sample scraped problem_ids:", [r["problem_id"] for r in results[:5]])
        print("Sample scraped language values:", [r["language"] for r in results[:5]])

    return results