# Beecrowd Code Downloader 🚀

Automatically download all your **Beecrowd (URI Online Judge)** accepted submissions, organize them by **programming language**, and optionally upload them to **GitHub**.

This tool logs into your Beecrowd account, scrapes your submission pages, downloads the source code for each submission, and stores them locally in a structured folder format.

---

## ✨ Features

- 🔐 Automatic Beecrowd login
- 📄 Scrapes all submission pages
- 💻 Detects programming language automatically
- 📁 Organizes code by language
- 🏷 Uses **problem ID as filename**
- 🔁 Supports **multiple attempts** (`1001.cpp`, `1001_2.cpp`)
- ⚡ Fast scraping with Selenium
- ☁ Optional **GitHub upload**

---

## 📂 Folder Structure

After downloading, files will look like:

URI-Source-Codes/
│
├── C++
│ ├── 1000.cpp
│ ├── 1029_1.cpp
│ └── 1029_2.cpp
│
├── Python
│ ├── 1001.py
│
└── Java
└── 1002.java


Files are grouped by **language** and named by **problem ID**.

---

## 🛠 Requirements

- Python **3.8+**
- Google Chrome
- ChromeDriver (matching your Chrome version)

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/NnR2D2/beecrowd-code-downloader.git
cd beecrowd-code-downloader

Install dependencies:

pip install -r requirements.txt

Download ChromeDriver:

https://chromedriver.chromium.org/downloads

Place it:

Windows: inside the project folder

Linux/Mac: inside PATH or project folder

▶ Running the Script
python main.py

Steps:

1. Script opens Chrome

2. Log in to Beecrowd

3. Complete "Verify you are human" if shown

4. Script downloads all your submissions

5. Files are saved into URI-Source-Codes

🌍 Supported Languages

The downloader currently supports:

C

C99

C++

C++17

C++20

C#

Java

JavaScript

Python

Go

Ruby

Rust

Swift

TypeScript

Kotlin

Lua

PHP

Scala

Julia

Dart

Haskell

OCaml

Pascal

PostgreSQL

R

Elixir

Clojure

Adding new languages only requires updating the language-extension mapping.

☁ Optional: Upload to GitHub

After downloading all files, the script can automatically upload them to a GitHub repository.

You will be prompted to provide a GitHub Personal Access Token.

🧠 Future Improvements

Faster hybrid scraper (Selenium + Requests)

Parallel downloads

Support for Codeforces / AtCoder / UVA

CLI options (--upload, --judge)

Docker support

👨‍💻 Author

NnR2D2

GitHub:
https://github.com/NnR2D2


---

## After replacing README

Run:

```bash
git add README.md
git commit -m "Fix README merge conflict and add modern README"
git push