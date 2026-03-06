import os
from github import Github, UnknownObjectException
from github.GithubException import GithubException
from .constants import BASE_FOLDER

REPO_NAME = "URI-Source-Codes"

def auth():
    token = input("Enter your GitHub Personal Access Token: ").strip()
    g = Github(token)
    return g.get_user()

def get_or_create_repo(user):
    try:
        return user.get_repo(REPO_NAME)
    except UnknownObjectException:
        print(f"Repository '{REPO_NAME}' not found. Creating it...")
        return user.create_repo(REPO_NAME, private=False)

def upload_file(repo, repo_path, local_path):
    with open(local_path, "r", encoding="utf-8") as f:
        content = f.read()

    try:
        existing = repo.get_contents(repo_path)
        repo.update_file(
            path=repo_path,
            message=f"Update {repo_path}",
            content=content,
            sha=existing.sha,
        )
        print(f"Updated: {repo_path}")
    except UnknownObjectException:
        repo.create_file(
            path=repo_path,
            message=f"Add {repo_path}",
            content=content,
        )
        print(f"Uploaded: {repo_path}")
    except GithubException as e:
        print(f"Failed to upload {repo_path}: {e}")

def github():
    user = auth()
    repo = get_or_create_repo(user)

    if not os.path.isdir(BASE_FOLDER):
        print(f"Folder not found: {BASE_FOLDER}")
        return

    for root, _, files in os.walk(BASE_FOLDER):
        for file_name in files:
            local_path = os.path.join(root, file_name)

            # repo path like C++/1000.cpp or Python/2987_2.py
            repo_path = os.path.relpath(local_path, BASE_FOLDER).replace("\\", "/")

            upload_file(repo, repo_path, local_path)

    print(f"All files uploaded to GitHub repo '{REPO_NAME}'.")