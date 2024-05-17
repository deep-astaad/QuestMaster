
# QuestMaster

  

QuestMaster is a powerful application that leverages DataStax Cassandra and OpenAI GPT-3.5 Turbo to provide advanced functionalities. This README provides detailed instructions on how to set up and run the application on a Linux system.

  

## Prerequisites

  

Before you begin, ensure you have the following installed on your system:

  

1.  **Python**: Version 3.8 or higher

2.  **pip**: Python package installer

3.  **Git**: Version control system

  

## Installation

  

Follow these steps to set up and run the application:

  

### 1. Clone the Repository

  
  

```bash

git  clone  <https://github.com/deep-astaad/QuestMaster.git>

cd  <QuestMaster>

```

  
  

### 2. Clone the Repository

```bash

python3  -m  venv  venv

source  venv/bin/activate

```

### 3.  Install Required Packages
```bash
pip install -r requirements_linux.txt
```

### 4. Obtain DataStax Cassandra Credentials
You need to get the `token.json` and `secure-connect-bundle.zip` from your DataStax Cassandra database.

 ##### 4.1. Generate Token JSON
			 1. Log in to your DataStax Astra account.
			 2. Navigate to the Generate token.
			 3. Select database administration role and generate a new token.
			 4. Download the `token.json` file.
 ##### 4.2. Download Secure Connect Bundle
			 1. In your DataStax Astra dashboard, create new database database.
			 2. Click on Connect.
			 3. Look for Download SCB or Secure Connect Bundle
			 4. Download the `secure-connect-bundle.zip`.

### 5. Obtain OpenAI API Key
You need to get an API key from OpenAI to use their GPT-3.5 Turbo model.

			 1. Go to the [OpenAI official website](https://platform.openai.com/signup/).
			 2. Sign up for an account or log in if you already have one.
			 3. Navigate to the API Keys section in your account settings.
			 4. Click on Create new secret key.
			 5. Copy the generated API key.

### 6. Set Up Environment Variables
Create a `.env` file in the root directory of your project and add the following lines:
```bash
DATASTRAX_TOKEN_JSON=/path/to/your/token.json
SECURE_BUNDLE_ZIP=/path/to/your/secure-connect-bundle.zip
OPENAI_API_KEY=your_openai_api_key
```
Replace `/path/to/your/token.json` and `/path/to/your/secure-connect-bundle.zip` with the actual paths to your downloaded files. Also, replace `your_openai_api_key` with your actual OpenAI API key.

### 7. Run the Application
```bash
streamlit run app_questmaster.py
```

## Summary of Key Files and Their Roles

 - **app_questmaster.py**: Main application script.
 - **cassandra_connection.py**: Handles the connection to the DataStax Cassandra database.
 - **openai_gpt.py**: Configures the OpenAI GPT-3.5 Turbo model.
 - **requirements_linux.txt**: Lists all the Python dependencies.

#### Directory Structure
```xml
<QuestMaster>/
├── app_questmaster.py
├── cassandra_connection.py
├── openai_gpt.py
├── requirements_linux.txt
├── .env.example
└── .env
└── secure_bundle_connect.zip
└── token.json
```

### Additional Notes

 - Ensure that the `token.json` and `secure-connect-bundle.zip` files are kept secure and not exposed to anyone.
