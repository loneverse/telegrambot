Absolutely, here's the formatted README in markdown:

## Telegram Scrapping Server

This project implements a server-side application that scrapes messages from the "Bitcoin Industry" Telegram group chat. It leverages different technologies to provide several functionalities:

**Features:**

* **Periodic Data Scraping:** The server periodically fetches messages from the Telegram group chat and stores them in a PostgreSQL database.
* **Image Storage:** Images embedded within messages are saved to local storage for future reference.
* **Email Notifications:** When the chatroom owner posts a new message, an email notification is sent to a designated recipient.
* **REST API:** A REST API allows you to retrieve saved messages with pagination for efficient browsing.
* **Swagger Documentation:** Online API documentation using Swagger is provided for easy exploration and testing of the endpoints.

**Technology Stack:**

* **Scraper Language:** Choose either Golang or Python based on your preference (both are supported).
* **Backend Language:** Node.js is the preferred backend language for this project (alternatives are Golang or Python).
* **Database:** PostgreSQL is used for reliable data storage.
* **API:** RESTful API provides structured access to scraped messages.
* **Documentation:** Swagger facilitates interactive API exploration.

**Project Structure:**

* **backend/**: Contains Node.js server-side code (adjust for Golang or Python).
* **config/**: Stores configuration files (e.g., database connection details, email settings).
* **db/**: Houses database-related logic and migrations (if applicable).
* **docs/**: Optional directory for API documentation files.
* **scraper/**: Contains the Python script (`telegram_scraper.py`) for scraping messages if using Python (adjust if using Golang).
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

**Dependencies:** Install Python dependencies from `requirements.txt` within the activated virtual environment:

```bash
pip install -r requirements.txt
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

**Customization:**

* Update configuration files in the `config` directory to tailor the project to your specific needs (database connection details, email settings, etc.).
* Modify the scraper script (`telegram_scraper.py`) to adjust scraping behavior if using Python.
* Implement additional features or modify existing ones to suit your project requirements.
