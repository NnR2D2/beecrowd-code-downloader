"""
File dedicated to the extraction and manipulation of the source code.
"""
import os
import re
from selenium.webdriver.common.by import By
from .helpers import create_dir
from .constants import BASE_FOLDER

def scrape_code(driver):
    # Ace editor lines are usually under #code with class 'ace_line'
    return driver.find_elements(By.XPATH, '//*[@id="code"]//div[contains(@class,"ace_line")]')

def get_extension(language: str):
    lang = (language or "").strip()

    if lang == "C":
        return ".c"

    if lang == "C99":
        return ".c"

    if lang == "C#":
        return ".cs"

    if lang == "C++" or lang == "C++17" or lang == "C++20":
        return ".cpp"

    if lang == "Java" or lang == "Java 8" or lang == "Java 14" or lang == "Java 19":
        return ".java"

    if lang == "JavaScript" or lang == "JavaScript 12.18":
        return ".js"

    if lang == "Python" or lang == "Python 3" or lang == "Python 3.8" or lang == "Python 3.9" or lang == "Python 3.9 AI" or lang == "Python 3.11":
        return ".py"

    if lang == "Go" or lang == "Go 1.15" or lang == "Go 1.20":
        return ".go"

    if lang == "Ruby" or lang == "Ruby 2.7":
        return ".rb"

    if lang == "Rust":
        return ".rs"

    if lang == "Swift" or lang == "Swift 5.8":
        return ".swift"

    if lang == "TypeScript 4.1" or lang == "TypeScript 5.1":
        return ".ts"

    if lang == "Kotlin":
        return ".kt"

    if lang == "Lua" or lang == "Lua 5.4":
        return ".lua"

    if lang == "PHP" or lang == "PHP 8.1":
        return ".php"

    if lang == "PostgreSQL":
        return ".sql"

    if lang == "Scala":
        return ".scala"

    if lang == "Julia":
        return ".jl"

    if lang == "Dart" or lang == "Dart 2.17" or lang == "Dart 3.0":
        return ".dart"

    if lang == "Haskell":
        return ".hs"

    if lang == "OCaml":
        return ".ml"

    if lang == "Pascal":
        return ".pas"

    if lang == "Clojure":
        return ".clj"

    if lang == "Elixir":
        return ".ex"

    return ".txt"
def get_language_name_from_extension(ext: str):
    languages = {
        ".cpp": "C++",
        ".py": "Python",
        ".go": "Golang",
        ".js": "JavaScript",
        ".cs": "C#",
        ".c": "C",
        ".java": "Java",
        ".txt": "Other",
    }
    return languages.get(ext, "Other")

def write_to_file(elements, problem_id: str, exec_id: str, language: str):
    ext = get_extension(language)
    lang_folder = get_language_name_from_extension(ext)

    create_dir(BASE_FOLDER)
    lang_dir = os.path.join(BASE_FOLDER, lang_folder)
    create_dir(lang_dir)

    base = str(problem_id).strip()
    base = re.sub(r"\D", "", base) or "unknown"
    # Find all existing files for this problem
    existing = []
    for fname in os.listdir(lang_dir):
        if fname.startswith(base) and fname.endswith(ext):
            existing.append(fname)

    # Case 1: no file exists → save as 1001.cpp
    if not existing:
        filename = f"{base}{ext}"

    # Case 2: first duplicate → rename existing and create numbered files
    elif len(existing) == 1 and existing[0] == f"{base}{ext}":
        os.rename(
            os.path.join(lang_dir, f"{base}{ext}"),
            os.path.join(lang_dir, f"{base}_1{ext}")
        )
        filename = f"{base}_2{ext}"

    # Case 3: already numbered attempts
    else:
        numbers = []
        for f in existing:
            m = re.match(rf"{base}_(\d+){re.escape(ext)}", f)
            if m:
                numbers.append(int(m.group(1)))

        next_n = max(numbers) + 1 if numbers else 1
        filename = f"{base}_{next_n}{ext}"

    path = os.path.join(lang_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        for line in elements:
            f.write(line.text + "\n")