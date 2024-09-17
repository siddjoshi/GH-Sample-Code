import { Octokit } from "@octokit/rest";
import dotenv from "dotenv";

// Load environment variables from .env file
dotenv.config();

const owner = process.env.GITHUB_OWNER;
const repo = process.env.GITHUB_REPO;
const token = process.env.GITHUB_TOKEN;

// Initialize Octokit with authentication
const octokit = new Octokit({
  auth: token,
});

async function getCodeScanningAlerts(owner, repo, state, ref) {
  let alerts = [];
  let page = 1;

  while (true) {
    const response = await octokit.rest.codeScanning.listAlertsForRepo({
      owner,
      repo,
      //state,
      ref,
      page,
      per_page: 100,
    });

    alerts = alerts.concat(response.data);

    if (response.data.length < 100) {
      break;
    }

    page++;
  }

  return alerts;
}

// Fetch the alerts with desired state and reference
const stateFilter = 'fixed';  // Example state filter
//const refFilter = 'refs/heads/master';  // Example reference filter
// const refFilter = 'refs/heads/feature1';
const refFilter = 'refs/pull/1/merge';
// const refFilter = 'refs/heads/main';

getCodeScanningAlerts(owner, repo, stateFilter, refFilter)
  .then(alerts => {
    alerts.forEach(alert => {
      console.log(`Alert ID: ${alert.number}, State: ${alert.state}, Rule: ${alert.rule.id}, Ref: ${alert.most_recent_instance.ref}`);
    });
  })
  .catch(error => {
    console.error(error);
  });