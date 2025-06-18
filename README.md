# CST8919 Lab 2 – Flask Web App with Threat Detection using Azure Monitor and KQL
## Overview
This lab demonstrates how to build a simple Python Flask application with a /login route, deploy it to Azure App Service, monitor suspicious activity (like brute-force login attempts) using Azure Monitor, and create alerts using KQL (Kusto Query Language).

## Features
Flask app with /login endpoint
Logs successful and failed login attempts
Diagnostic logging to Azure Monitor
KQL queries to detect brute-force attempts
Alerting when suspicious behavior is detected

## Deployment Steps
🔹 1. Flask App Code
🔹 2. Azure Deployment Commands
🔹 3. Push Code to Azure Web App
🔹 4. Diagnostic Logging (Azure Portal)
In the Web App > Monitoring > Diagnostic Settings:
Enable AppServiceConsoleLogs
Send to a Log Analytics Workspace

## Testing the App
test-app.http Sample (for VS Code REST Client):
```sh
### Successful login
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=ajay

#### Failed login attempt 1
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong1

### Failed login attempt 2
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong2

### Failed login attempt 3
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong3

### Failed login attempt 4
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong4

### Failed login attempt 5
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong5

### Failed login attempt 6
POST https://ajay-lab2-linux-webapp.azurewebsites.net/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong6

```

# KQL Query to Detect Failed Logins:
```sh
AppServiceConsoleLogs
| where TimeGenerated > ago(30m)
| where Level == "Warning"
| where Message has "Login failed"
| summarize FailedAttempts = count() by bin(TimeGenerated, 5m)
```
**Explanation:**

Level == "Warning" filters failed logins
Message has "Login failed" targets failed auth logs
summarize counts number of failed attempts in 5-minute buckets

## Alert Rule
Scope: Log Analytics Workspace
Condition: KQL query above
Threshold: More than 5 failed attempts
Evaluation Period: Every 1 minute
Action Group: Email notification
Severity: 3

# YouTube Demo
🔗 Demo Video Link

**The video demonstrates:**
App deployment in Azure
Simulating login attempts
KQL log inspection
Alert being triggered and email notification


## 💬 What I Learned
How to deploy Flask apps to Azure App Service (Linux)
Enabling and querying diagnostic logs in Azure Monitor
Writing and testing KQL queries
Creating alert rules based on app logs
How failed logins can indicate brute-force attacks

## How I Would Improve This in a Real-World Scenario
Use real identity providers (e.g., Azure AD or OAuth)
Rate-limiting to slow down brute-force attempts
Save logs to blob or database for long-term retention
Alert integration with Teams/Slack or incident tools
Obfuscate sensitive data in logs.
