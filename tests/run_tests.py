import subprocess
from datetime import datetime


def get_date_for_report():
    current_datetime = datetime.now()
    return current_datetime.strftime("%d-%m-%Y_%H-%M")


def run_tests_and_generate_allure_report():
    # Run pytest tests
    pytest_cmd = "pytest --alluredir=allure-results"
    subprocess.run(pytest_cmd, shell=True)

    # Generate Allure report
    allure_cmd = "allure generate allure-results -o allure-reports\\report_" + get_date_for_report()
    subprocess.run(allure_cmd, shell=True)


if __name__ == "__main__":
    run_tests_and_generate_allure_report()
