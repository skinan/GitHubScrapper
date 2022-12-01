from githubscrapper import *
import csv


def main():
    g = GitHubStatsScrapper()
    response_dict = g.search_repos_tag("deep-learning", "stars", per_page= 100, page=100)
    if response_dict:
        scrapped_list = [["name", "stargazers_count", "watchers_count", "language", "open_issues", "forks",
                          "open_issues", "size", "html_url"]]
        for repository in response_dict['items']:
            scrapped_list.append([repository["name"],
                                  repository["stargazers_count"],
                                  repository["watchers_count"],
                                  repository["language"],
                                  repository["open_issues"],
                                  repository["forks"],
                                  repository["open_issues"],
                                  repository["size"],
                                  repository["html_url"]
                                  ])
        with open('GitHubScrapper.csv', 'w') as csv_file:
            # using csv.writer method from CSV package
            write = csv.writer(csv_file)
            write.writerows(scrapped_list)


if __name__ == '__main__':
    main()
