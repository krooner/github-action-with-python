from github import Github

def get_github_repo(access_token, repo):
    """
        :param access_token: Github access token
        :param repo: Repository name
        :return: repository object
    """

    g = Github(access_token)
    return g.get_user().get_repo(repo)

def upload_github_issue(repo, title, body):
    """
        :param repo: Repository name
        :param title: issue title
        :param body: issue body
        :return: None
    """
    repo.create_issue(title=title, body=body)