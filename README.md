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
