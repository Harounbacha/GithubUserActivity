# GitHub User Activity Tracker

A command-line tool that fetches and displays recent GitHub activities for any user.

## Features

- Fetch latest GitHub activities for any user
- Display event type, timestamp, and repository name
- Simple and easy-to-use command-line interface
- Shows the 5 most recent activities

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Harounbacha/GithubUserActivity.git
cd GithubUserActivity
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with a GitHub username as an argument:
```bash
python main.py <username>
```

Example:
```bash
python main.py Harounbacha
```

## Sample Output
```
Recent GitHub activity for Harounbacha:

🔹 PushEvent on 2025-05-07 10:30:15
   Repository: Harounbacha/GithubUserActivity
```

## Dependencies

- click: Command-line interface creation kit
- requests: HTTP library for API requests

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.