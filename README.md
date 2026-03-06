# 🚀 Beecrowd Code Downloader
A Python tool that automatically downloads and organizes your Beecrowd accepted submissions.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Status](https://img.shields.io/badge/Status-Active-success)


Automatically download all your **Beecrowd (URI Online Judge)** accepted submissions, organize them by **programming language**, and optionally upload them to **GitHub**.

This tool logs into your Beecrowd account, scrapes your submission pages, downloads the source code for each submission, and stores them locally in a structured folder format.

---
## 📚 Table of Contents

- [Purpose](#-purpose)
- [Features](#-features)
- [Folder Structure](#-folder-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Running the Script](#-running-the-script)
- [Setup Credentials](#-setup-credentials)
- [Supported Languages](#-supported-languages)
- [Upload to GitHub](#-optional-upload-to-github)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---
## 🎯 Purpose

Competitive programmers often lose track of their past solutions.  
This tool automatically downloads and organizes all accepted submissions from Beecrowd so they can be stored locally or uploaded to GitHub.

---

## 🎬 Demo

Example of the downloader in action:

![Demo](demo.gif)

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

```
URI-Source-Codes/
│
├── C++
│   ├── 1000.cpp
│   ├── 1029_1.cpp
│   └── 1029_2.cpp
│
├── Python
│   └── 1001.py
│
└── Java
    └── 1002.java
```

Files are grouped by **language** and named by **problem ID**.

---

## 🛠 Requirements

- Python **3.8+**
- Google Chrome
- ChromeDriver (matching your Chrome version)

Download ChromeDriver:

https://chromedriver.chromium.org/downloads

Place it:

- **Windows:** inside the project folder  
- **Linux / Mac:** inside your `PATH` or project folder

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/NnR2D2/beecrowd-code-downloader.git
cd beecrowd-code-downloader
```

Install dependencies:
```bash
pip install -r requirements.txt
```
## ▶ Running the Script

Run the script:
```bash
python main.py
```
Steps:

1. The script opens Chrome

2. Log in to Beecrowd

3. Complete the "Verify you are human" check if it appears.

4. The script navigates through all submission pages

5. Your source files are saved into URI-Source-Codes

## 🔐 Setup Credentials

Before running the script, open login.py and add your Beecrowd credentials:
```python
email_field.send_keys("your_email_here")
password_field.send_keys("your_password_here")
```
Then run:
```bash
python main.py
```
## 🌍 Supported Languages

The downloader currently supports:

* C

* C99

* C++

* C++17

* C++20

* C#

* Java

* JavaScript

* Python

* Go

* Ruby

* Rust

* Swift

* TypeScript

* Kotlin

* Lua

* PHP

* Scala

* Julia

* Dart

* Haskell

* OCaml

* Pascal

* PostgreSQL

* R

* Elixir

* Clojure

Adding support for new languages only requires updating the **language-extension mapping**.

## ☁ Optional: Upload to GitHub

After downloading all files, the script can automatically upload them to a GitHub repository.

You will be prompted to provide a **GitHub Personal Access Token**.

## 🧠 Future Improvements

Faster **hybrid scraper (Selenium + Requests)**

Parallel downloads

Support for **Codeforces / AtCoder / UVA**

CLI options (--upload, --judge)

Docker support

## 👨‍💻 Author

**NnR2D2**

GitHub:  
https://github.com/NnR2D2