import gitlab
from datetime import datetime

GITLAB_URL = 'https://git.internal.ir' 
PRIVATE_TOKEN = 'xxxx'
YOUR_USERNAME = 'YOUR_USERNAME'

try:
    gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)
    gl.auth()
except Exception as e:
    print(f"Failed to connect to GitLab: {str(e)}")
    exit(1)

try:
    user = gl.user
    if user is None:
        raise ValueError("Failed to fetch user information. Check your access token.")
    print(f"Fetching contributions for user: {user.username} (ID: {user.id})")
except Exception as e:
    print(f"Error fetching user info: {str(e)}")
    exit(1)

try:
    projects = gl.projects.list(membership=True, get_all=True)
except Exception as e:
    print(f"Error fetching projects: {str(e)}")
    exit(1)

total_commits = 0
total_releases = 0
total_tags = 0
total_merge_requests = 0
total_issues = 0


for project in projects:
    print(f"\nChecking project: {project.name}")

    try:
        commits = project.commits.list(all=True, author_id=user.id, get_all=True)
        your_commits = [commit for commit in commits if commit.author_name == YOUR_USERNAME]
        total_commits += len(your_commits)
        print(f" - Your commits: {len(your_commits)}")
        for commit in your_commits:
            print(f"   - Commit: {commit.id} by {commit.author_name} on {commit.created_at}")
    except Exception as e:
        print(f" - Error fetching commits: {str(e)}")

    try:
        releases = project.releases.list(get_all=True)
        your_releases = [release for release in releases if release.author['name'] == YOUR_USERNAME]
        total_releases += len(your_releases)
        print(f" - Your releases: {len(your_releases)}")
        for release in your_releases:
            print(f"   - Release: {release.name} on {release.released_at}")
    except Exception as e:
        print(f" - Error fetching releases: {str(e)}")

    try:
        tags = project.tags.list(get_all=True)
        your_tags = [tag for tag in tags if tag.commit['author_name'] == YOUR_USERNAME]
        total_tags += len(your_tags)
        print(f" - Your tags: {len(your_tags)}")
        for tag in your_tags:
            print(f"   - Tag: {tag.name} by {tag.commit['author_name']} on {tag.commit['created_at']}")
    except Exception as e:
        print(f" - Error fetching tags: {str(e)}")

    try:
        merge_requests = project.mergerequests.list(author_id=user.id, state='all', get_all=True)
        total_merge_requests += len(merge_requests)
        print(f" - Your merge requests: {len(merge_requests)}")
        for mr in merge_requests:
            print(f"   - MR: {mr.title} (State: {mr.state}) on {mr.created_at}")
    except Exception as e:
        print(f" - Error fetching merge requests: {str(e)}")

    try:
        issues = project.issues.list(author_id=user.id, state='all', get_all=True)
        total_issues += len(issues)
        print(f" - Your issues: {len(issues)}")
        for issue in issues:
            print(f"   - Issue: {issue.title} (State: {issue.state}) on {issue.created_at}")
    except Exception as e:
        print(f" - Error fetching issues: {str(e)}")

print("\n--- Summary of Your Contributions ---")
print(f"Total Commits: {total_commits}")
print(f"Total Releases: {total_releases}")
print(f"Total Tags: {total_tags}")
print(f"Total Merge Requests: {total_merge_requests}")
print(f"Total Issues: {total_issues}")
