# Workstation

Workstation is a personal productivity web application designed to organize tasks through a Dashboard and Workspace interface.

## Features

-   **Personalized Landing Page**: Welcomes the user by name.
-   **Theme Support**: Automatic Light and Dark mode based on system preferences.
-   **Data Privacy**: All data is stored locally in JSON files within the `data/` directory.
-   **FastAPI Backend**: High-performance Python framework.

## Setup

1.  **Clone the repository** (or download the source code).
2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```
3.  **Install Dependencies**:
    ```bash
    ./venv/Scripts/pip install -r requirements.txt
    ```

## Running the Application

1.  **Start the Server**:
    ```bash
    ./venv/Scripts/python -m uvicorn main:app.py --reload
    ```
2.  **Access the App**:
    Open [http://localhost:8000](http://localhost:8000) in your browser.
3.  **First Run**:
    You will be prompted to enter your name. This creates a `data/config.json` file.

## Project Structure

-   `main.py`: Application entry point.
-   `database.py`: Handles file-based database operations.
-   `templates/`: HTML templates.
-   `static/`: CSS and JavaScript files.
-   `data/`: Stores user configuration and database files (ignored by Git).
