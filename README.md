## Telegram Scrapping Server

This project implements a server-side application that scrapes messages from the "Bitcoin Industry" Telegram group chat. It leverages different technologies to provide several functionalities:

**Features:**

* **Periodic Data Scraping:** The server periodically fetches messages from the Telegram group chat and stores them in a PostgreSQL database.
* **Image Storage:** Images embedded within messages are saved to local storage for future reference.
* **Email Notifications:** When the chatroom owner posts a new message, an email notification is sent to a designated recipient.
* **REST API:** A REST API allows you to retrieve saved messages with pagination for efficient browsing.
* **Swagger Documentation:** Online API documentation using Swagger is provided for easy exploration and testing of the endpoints.

**Technology Stack:**

* **Scraper Language:** Python
* **Backend Language:** Node.js is the preferred backend language for this project (Python).
* **Database:** PostgreSQL is used for reliable data storage.



### Setting Up Postgresql

1. Open the PostgreSQL command-line interface by running the following command in your terminal:

```
sudo -u postgres psql
```

This will open the PostgreSQL interactive terminal client.

2. Connect to your database by running the following command, replacing `your_database_name` with the name of your database:

```
\c your_database_name
```

3. Once you're connected to your database, you can check if the table exists by running the following command:

```
\dt
```


* **API:** RESTful API provides structured access to scraped messages.
* **Documentation:** Swagger facilitates interactive API exploration.

**Project Structure:**

* **backend/**: Contains Node.js server-side code (Python).
* **config/**: Stores configuration files (e.g., database connection details, email settings).
* **db/**: Houses database-related logic and migrations (if applicable).
* **docs/**: Optional directory for API documentation files.
* **scraper/**: Contains the Python script (`telegram_scraper.py`) for scraping messages if using Python.
* **utils/**: Optional directory for utility functions shared across the project.

**Installation**


**Node.js:**

**Prerequisites:** Install Node.js and npm (Node Package Manager).

**Dependencies:** Install project dependencies from `package.json`:

```bash
cd backend
npm install
```

**Python Example:**

**Prerequisites:** Install Python and virtual environment tools (e.g., `venv` or `virtualenv`).

**Virtual Environment:** Create and activate a virtual environment (recommended for Python projects):

```bash
python -m venv venv  # Create virtual environment (adjust command if using virtualenv)
source venv/bin/activate  # Activate virtual environment (adjust command if using virtualenv)
```

**Running the Server:**

**Node.js:**

```bash
cd backend
node server.js
```

**Python:**

```bash
cd backend
python telegram_scraper.py  # Assuming `telegram_scraper.py` is the scraper script
```

**API Usage:**

Refer to the provided Swagger documentation for detailed API endpoint descriptions, usage examples, and request/response formats.

when the server is running, find the documentation at 

``http://localhost:3000/api-docs/#/default/get_messages``

**Customization:**

* Update configuration files in the `config` directory to tailor the project to your specific needs (database connection details, email settings, etc.).
* Modify the scraper script (`telegram_scraper.py`) to adjust scraping behavior if using Python.
* Implement additional features or modify existing ones to suit your project requirements.

Using a `.env` File for Secret Keys:

Create a file named `.env` in the config directory.

Add environment variables for sensitive information like your Telegram bot token, database connection details, and email credentials:

```bash
POSTGRES_USER=<POSTGRES_DB_USERNAME>
POSTGRES_PASSWORD=<PASSWORD>
POSTGRES_DB=<DB>
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
EMAIL_USER=<USERNAME>
EMAIL_PASS=<PASSWORD>
TELEGRAM_BOT_TOKEN =<Bot Token>
TARGET_CHAT_ID=<chatID>
```