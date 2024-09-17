# GitHub Code Scanning Alerts Query

This project provides a script to query code scanning alerts from a GitHub repository using the GitHub REST API and Octokit library. The script can filter alerts based on their state and reference.

## Prerequisites

- Node.js and npm installed on your machine
- A GitHub Personal Access Token (PAT) with `repo` and `security_events` scopes

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository