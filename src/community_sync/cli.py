import os
import click
import requests

API = "https://api.github.com"


def _get(url, token=None, params=None):
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    r = requests.get(url, headers=headers, params=params, timeout=15)
    r.raise_for_status()
    return r.json()


@click.group()
def cli():
    """Community Sync: generate GitHub community health reports."""
    pass


@cli.command()
@click.option("--org", required=True, help="GitHub org name")
def report(org):
    """Report key numbers across all org repos."""
    token = os.getenv("GITHUB_TOKEN")
    repos = _get(f"{API}/orgs/{org}/repos", token=token, params={"per_page": 100})

    total_repos = len(repos)
    open_issues = sum(repo.get("open_issues_count", 0) for repo in repos)

    click.echo(f"Org: {org}")
    click.echo(f"Repos: {total_repos}")
    click.echo(f"Open issues (total): {open_issues}")


@cli.command()
@click.option("--repo", required=True, help="Repository slug owner/repo")
def summary(repo):
    """Output simple repo community summary."""
    token = os.getenv("GITHUB_TOKEN")
    owner, name = repo.split("/", 1)
    r = _get(f"{API}/repos/{owner}/{name}", token=token)

    click.echo(f"Repo: {repo}")
    click.echo(f"Stars: {r.get('stargazers_count', 0)}")
    click.echo(f"Watchers: {r.get('watchers_count', 0)}")
    click.echo(f"Open issues: {r.get('open_issues_count', 0)}")


def main():
    cli()


if __name__ == "__main__":
    main()