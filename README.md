# GitLab Contribution Tracker

This script is designed to help you track and analyze your contributions across different GitLab projects. It retrieves information on the following contribution types:

- **Commits**
- **Releases**
- **Tags**
- **Merge Requests**
- **Issues**

## Requirements

- Python 3.x
- [GitLab Python API](https://python-gitlab.readthedocs.io/) (`pip install python-gitlab`)
- A GitLab personal access token

## Setup

1. Clone this repository or download the script.
2. Install the required dependencies by running the following command:
    ```bash
    pip install python-gitlab
    ```
3. Update the script with your GitLab URL, personal access token, and username. Modify the following variables in the script:
   - `GITLAB_URL`: Your GitLab server URL (e.g., `'https://gitlab.com'` or `'https://git.internal.ir'`).
   - `PRIVATE_TOKEN`: Your GitLab personal access token.
   - `YOUR_USERNAME`: Your GitLab username.

## Usage

After updating the script, you can run it with the following command:

```bash
python gitlab_contribution_tracker.py
```

### Output

The script will output a summary of your contributions, including the total number of commits, releases, tags, merge requests, and issues that you have contributed to across all the projects you are a member of.

Example output:

```
--- Summary of Your Contributions ---
Total Commits: 42
Total Releases: 3
Total Tags: 5
Total Merge Requests: 8
Total Issues: 10
```

## Notes

- The script assumes that you have access to the GitLab API and the necessary permissions to read data from the repositories you are a member of.
- If the script fails to fetch any information (due to connectivity issues, incorrect credentials, or insufficient permissions), it will display an error message and continue running.

## License

This script is provided as-is for personal use and educational purposes. Feel free to modify or extend it as needed.
