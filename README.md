# Flask Price Alert

Flask application for tracking price alerts and sending email notifications when thresholds are met.

## About

The code is structured as a small Flask site with a user blueprint, a MongoDB-backed data layer, and an alert updater script that scans pending alerts and triggers price checks. It reads like a lightweight notification workflow for watched items.

## Key Features

- Flask app with modular user routes
- MongoDB-backed storage helper
- Scheduled alert update script
- Email notification flow for alert thresholds

## Architecture

- `app.py` creates the Flask application and registers the user blueprint
- `common/database.py` wraps MongoDB access
- `alert_updater.py` iterates over alerts that need refreshing
- `run.py` is the local launcher

## Tech Stack

- Python
- Flask
- PyMongo
- MongoDB

## Prerequisites

- Python 3.x
- MongoDB running locally

## Installation

```bash
pip install flask pymongo passlib
```

## Configuration

- `config.py` currently hardcodes `DEBUG`, `ADMINs`, and `SECRET_KEY`
- `common/database.py` currently connects to `mongodb://127.0.0.1:27017`

## How to Run

```bash
python run.py
python alert_updater.py
```

## Example Usage

- Open `/` to confirm the Flask app is running
- Use the user blueprint under `/users`

## Project Structure

- `app.py` - Flask app setup and route registration
- `common/` - database and utility helpers
- `alert_updater.py` - background price check workflow
- `templates/` - login template and related UI assets

## Current Status

Prototype-level application. The code is functional in concept, but several values are still hardcoded and there is no published deployment configuration.

## Limitations

- Hardcoded secret key in `config.py`
- No env example
- No test suite

## License

No explicit license file was found.
