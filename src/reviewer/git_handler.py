import requests

# Returns the code changes of the provided git url (pull request or commit)
# it must be a public repo
def get_code_changes(git_url):
    url = f"{git_url}.diff"
    response = requests.get(url)
    return response.text
    