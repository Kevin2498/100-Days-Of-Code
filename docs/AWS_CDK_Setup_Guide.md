
# Setting Up AWS CDK

This guide provides step-by-step instructions to set up AWS CDK (Cloud Development Kit) with Python.

---

## Prerequisites

Ensure the following are installed before proceeding:

1. **Python**
2. **Node.js**
3. **AWS CDK CLI**
4. **AWS CLI**

---

## Steps to Set Up AWS CDK

### 1. Create a Folder
- Create a folder and navigate into it:

  ```bash
  mkdir my-cdk-project
  cd my-cdk-project
  ```

### 2. Create a GitHub Repository
- Create a GitHub repository with the same name as your folder.

### 3. Initialize CDK
- Initialize the CDK app with Python as the language:

  ```bash
  cdk init app --language python
  ```

### 4. Configure AWS Credentials
- Use AWS SSO to configure your credentials:

  ```bash
  aws configure sso
  ```

### 5. Bootstrap Your Environment
- Bootstrap your AWS environment:

  ```bash
  cdk bootstrap
  ```

#### Note:
- If updates or customizations are needed for the bootstrap template, run:

  ```bash
  cdk bootstrap --show-template > bootstrap-template.yml
  ```
- To enforce permissions boundaries, add the following to your `cdk.json`:

  ```json
  {
      "context": {
          "@aws-cdk/core:permissionsBoundary": {
              "name": "LZ-IAM-Boundary"
          }
      }
  }
  ```

#### Custom Bootstrap:
- Deploy a custom bootstrap template:

  ```bash
  export AWS_PROFILE="my-aws-profile"
  cdk bootstrap       
    --template templates/cdk-bootstrap-templte.yaml       
    --role-arn "arn:aws:iam::$( aws sts get-caller-identity --query Account | tr -d '"' ):role/LillyCloudFormationExecutionRole"
  ```

### 6. List CDK Stacks
- List the available CDK stacks in your app:

  ```bash
  cdk list
  ```

### 7. Deploy Your CDK Stack
- Deploy the stack (if you are not setting up a pipeline):

  ```bash
  cdk deploy
  ```

---

## Deploy CDK Stack Using GitHub Actions

Here’s a sample GitHub Actions workflow to deploy your CDK stack:

```yaml
name: Deploy CDK Changes

on:
  push:
    branches:
      - main  # Trigger on changes to the main branch

env:
  AWS_REGION: us-east-2

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read

    steps:
      # Step 1: Checkout the repository
      - name: Checkout Repository
        uses: actions/checkout@v4

      # Step 2: Set up Node.js
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'  # Compatible Node.js version for AWS CDK

      # Step 3: Set up Python and install dependencies
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'  # Match your local Python version

      - name: Install Python Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # Step 4: Install AWS CDK CLI
      - name: Install AWS CDK
        run: npm install -g aws-cdk

      # Step 5: Configure AWS credentials
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::${{ secrets.AWS_ACCOUNT_ID }}:role/${{ secrets.AWS_ROLE }}
          aws-region: ${{ env.AWS_REGION }}

      # Step 6: Synthesize and deploy the CDK stack
      - name: Deploy CDK Stack
        run: |
          cdk deploy --require-approval never
```

---

## Additional Notes

- Always ensure your AWS CLI is configured properly to avoid authentication issues.
- Regularly update your dependencies (`pip` and `npm`) to use the latest features and fixes.
