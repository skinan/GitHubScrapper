import requests


class GitHubStatsScrapper:
    def __init__(self, api_url="https://api.github.com"):
        self.github_api_url = api_url

    def search_repos_tag(self, tag, sort_by, per_page=10, page=1):
        request_url = f'{self.github_api_url}/search/repositories?q={tag}&sort={sort_by}&per_page={per_page}&page={page}'
        response = requests.get(request_url)
        if response.status_code == 200:
            response_dict = response.json()
            return response_dict
        else:
            print("Status code: ", response.status_code)


if __name__ == "__main__":
    print("Hello World")
