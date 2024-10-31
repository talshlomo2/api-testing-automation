# API Testing Automation

## Overview

This project implements a RESTful API using Flask to manage bot entities. It also includes automated tests designed to ensure the API functions correctly and reliably. The tests verify various operations related to bot management and generate clear reports for easy analysis.

## Technologies and Libraries Used

* **Flask**: A framework for building the RESTful API.
* **Requests**: A simple HTTP library for making requests in the test suite.
* **Pytest**: The testing framework used to create and run comprehensive test cases.
* **Allure**: Utilized for generating clear and visually appealing test reports, making it easier to analyze results.

## Installation

1. **Install Allure Command Line Interface (CLI):**  
   Follow the installation guide: [Allure CLI Installation](https://docs.qameta.io/allure/#_installing_a_commandline)

2. **Install Project Dependencies:**  
   Make sure you have Python and pip installed, then run:

   ```bash
   pip install -r requirements.txt
   ```
   
## Running the Application

### Run the Server

To start the Flask server, run:

```bash
python api/app.py
```

### Run Tests

To execute the automated tests, run:

```bash
python tests/run_tests.py
```

### View Test Reports

After running the tests, the test reports are generated and available at: `tests/allure-reports`.
