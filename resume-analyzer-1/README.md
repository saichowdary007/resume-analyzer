# README.md

# Resume Analyzer

## Overview
The Resume Analyzer is a web application built using Streamlit that allows users to upload their resumes and paste job descriptions to analyze the match score and identify missing skills.

## Features
- Upload a resume in PDF format.
- Paste a job description to get a match score.
- View insights on missing skills.
- Preview the text of the uploaded resume.

## Project Structure
```
resume-analyzer
├── src
│   ├── streamlit_app.py        # Main application file
│   ├── utils
│   │   └── __init__.py         # Utility functions
│   └── tests
│       └── __init__.py         # Test cases
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd resume-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To run the application, execute the following command:
```
streamlit run src/streamlit_app.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.