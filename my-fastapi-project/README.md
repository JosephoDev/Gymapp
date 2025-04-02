# My FastAPI Linear Regression Project

This project is a web application built using FastAPI that implements a linear regression model. It includes a simulated dataset with noise for testing the model's performance.

## Project Structure

```
my-fastapi-project
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   └── linear_regression.py
│   ├── static
│   │   └── (static files)
│   ├── templates
│   │   └── (template files)
│   └── utils
│       └── data_simulation.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-fastapi-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:
```
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000` in your web browser to access the application.

## Features

- Simulated dataset generation with noise for testing the linear regression model.
- Implementation of a linear regression model.
- FastAPI framework for building the web application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.