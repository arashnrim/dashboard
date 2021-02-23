# Dashboard

## Introduction

Welcome to the Dashboard project! This project was created for a coursework. The main intention of the coursework was to design a Python-executable script that works as a solution for the set design goal.

### About the project

The design goal of this project is:
> Enabling easier use of a computer through an accessible, intuitive interface.

With this dashboard-like interface, our main goal is to create an easy-to-use command-line interface for users who are not familiar with using computers. Having essential features in one place, this program should make it much easier to use some commonly-used features in a computer.

For more details on the project, visit the [project report](https://docs.google.com/document/d/1t1rERklzGDVZPoyKrVBXq2GmOywC1a4bcmHmczDhVgk/edit#) (closed to contributors only).

## Installing

### This program requires the following to be installed:

- Python (tested only on versions ≥ 3.6.8)
- Terminal (pre-installed on macOS)

### Running the Program

Due to some limitations on IDLE, the program cannot be run on it. Instead, use the Terminal:

1. At the location of the Python installation (usually at `/Applications/Python <version>/`, where `<version>` is the Python version number), open and execute the "Install Certificates.command" file.
2. Navigate to the project directory by running `cd /path/to/dashboard` (where `/path/to/dashboard` is replaced with the path to the folder).
3. Install required modules by running `pip3 install -r requirements.txt`.

<details><summary>Additional steps to use the weather feature</summary>

- Create an account at the [OpenWeatherMap website](https://home.openweathermap.org).
- Generate an API key.
- Copy the API key and paste it into `api_key` located in `weather/request.py`.

> **Warning!**
> An API key should be treated as something confidential; exposure of it can result in misuse by other unwanted developers and resulting in your account to potentially be terminated. Exercise caution when handling your API key, especially with a Git repository!
</details>

<details><summary>Additional steps to use the radio feature</summary>

- Install [Google Chrome](https://chrome.google.com).
- Install the [Chrome driver](https://chromedriver.chromium.org/) at `/usr/local/bin/`.
</details>

## Contributing

This project is not accepting feature contributions since it is meant for this specific coursework which has since concluded. If you would like to contribute in other ways except for adding features — such as reporting bugs, cleaning up code, and improving documentation — you may create a fork and a pull request once you're done, if you are interested.
