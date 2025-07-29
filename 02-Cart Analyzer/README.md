# Cart Analyzer

Cart Analyzer is a Python application designed to analyze shopping carts using LLM (Large Language Model) processing and Selenium automation. The tool provides a UI for interacting with the analysis and can capture screenshots of the process.

## Features

- Analyze shopping cart data using LLMs.
- Automate browser interactions with Selenium.
- User interface for easy operation.
- Screenshot capture for documentation and debugging.

## Project Structure

- `LLMProcessor.py`: Handles LLM-based processing and analysis.
- `selenium_handler.py`: Manages Selenium browser automation.
- `ui.py`: Provides the user interface for the application.
- `requirements.txt`: Lists Python dependencies.
- `screenshots/`: Contains example screenshots from the application.

## Installation

1. Clone the repository:
   ```zsh
   git clone <repo-url>
   cd llm-apps/02-Cart\ Analyzer
   ```

2. Create a virtual environment (optional but recommended):
   ```zsh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```zsh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```zsh
   python ui.py
   ```

2. Follow the on-screen instructions to analyze a cart and view results.

## Dependencies

- Python 3.8+
- Selenium
- Any other packages listed in `requirements.txt`

## Screenshots

Screenshots of the application in action can be found in the `screenshots/` directory.

## License

[MIT License](../LICENSE) (if applicable)

## Authors

- [Your Name]

---

Feel free to update this README with more specific details about usage, configuration,