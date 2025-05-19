# 🚀 Simple Python Web App with Azure CI/CD

This project demonstrates how to deploy a simple Python web application to **Azure App Service** using **GitHub Actions** for CI/CD.

---

## 🌐 Live Application

🔗 [https://simple-web-app-azure-fufbegaac6gyekag.centralindia-01.azurewebsites.net](https://simple-web-app-azure-fufbegaac6gyekag.centralindia-01.azurewebsites.net)

---

## 📦 Tech Stack

- **Language**: Python 3.13  
- **Runtime**: Azure Linux App Service  
- **CI/CD**: GitHub Actions  
- **Deployment**: Azure App Service (Free Tier)

---

## ⚙️ CI/CD Pipeline Setup

### 1️⃣ Create Azure Service Principal

Run the following command in the [Azure Cloud Shell](https://shell.azure.com) or your terminal:

```bash
az ad sp create-for-rbac --name "github-deploy" --role contributor \
  --scopes /subscriptions/<your-subscription-id> \
  --sdk-auth
## 📄 GitHub Actions Workflow File

The following is the CI/CD pipeline configuration defined in `.github/workflows/deploy.yml`:

```yaml
.github/workflows/deploy.yml

name: Deploy to Azure Web App

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'

    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Login to Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}

    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'simple-web-app-azure'
        slot-name: 'production'
        package: .
