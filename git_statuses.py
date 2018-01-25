#!/usr/bin/env python

import argparse
import requests
import sys

parser = argparse.ArgumentParser(description='Github statuses api helper.')

parser.add_argument('--owner', type=str, help="a repository owner", required=True)
parser.add_argument('--repo', type=str, help="repository name", required=True)
parser.add_argument('--sha', type=str, help="commit sha", required=True)
parser.add_argument('--access-token', type=str, help="oauth access token", required=True)

parser.add_argument('--state', type=str, help="state: pending|failure|error|success", required=True)
parser.add_argument('--target-url', metavar="URL", type=str, help="The target URL to associate with this status. This URL will be linked from the GitHub UI to allow users to easily see the source of the status. For example, if your continuous integration system is posting build status, you would want to provide the deep link for the build output for this specific SHA: http://ci.example.com/user/repo/build/sha")
parser.add_argument('--description', metavar="DESC", type=str, help="A short description of the status.")
parser.add_argument('--context', type=str, help="A string label to differentiate this status from the status of other systems", default="default")

args = parser.parse_args()

endpoint = "https://api.github.com/repos/{owner}/{repo}/statuses/{sha}?access_token={access_token}"\
    .format(
        owner=args.owner,
        repo=args.repo,
        sha=args.sha,
        access_token=args.access_token
    )

payload = {
    "state": args.state,
    "target_url": args.target_url,
    "description": args.description,
    "context": args.context
}

response = requests.post(endpoint, json=payload)

if response.status_code:
    sys.exit(response.text)
