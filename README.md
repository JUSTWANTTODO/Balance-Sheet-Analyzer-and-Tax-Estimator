# Balance Sheet Analyzer & Tax Estimator

This is a powerful Streamlit-based web application that analyzes uploaded financial data (Excel/CSV), generates Profit & Loss statements, estimates tax liability, summarizes TDS and GST, and provides interactive visualizations and updates on Indian tax laws. It uses Google's Gemini Pro (via LangChain) for financial reasoning and report generation.

## Features

- Upload `.csv`, `.xls`, or `.xlsx` files with financial data (e.g., ledgers, journal, Tally exports).
- Auto-parses and classifies income, expenses, assets, liabilities, and GST components.
- Generates:
  - Profit & Loss statement
  - Estimated tax liability with steps
  - GST and TDS summaries
  - Key insights and action items
- Asks for missing tax details and recalculates estimates
- Allows:
  - Saving and loading reports from a local database
  - Downloading detailed PDF reports
  - Querying financial analysis via an LLM-powered chat
- Suggests and generates meaningful visualizations using Plotly
- Displays the latest Indian tax and finance updates using an LLM agent

## Tech Stack

- **Frontend**: Streamlit
- **Backend/Logic**: Python, LangChain with Gemini Pro
- **Database**: SQLite (via `db_utils`)
- **Visualization**: Plotly
- **PDF Generation**: FPDF
- **Environment Variables**: Managed via `.env` file

## Setup Instructions

1. **Clone the repository**:
   ```bash
  git clone https://github.com/JUSTWANTTODO/Balance-Sheet-Analyzer-and-Tax-Estimator.git
  cd Balance-Sheet-Analyzer-and-Tax-Estimator

   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** with your Gemini API key:
   ```
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

4. **Run the app**:
   ```bash
   streamlit run main_app.py
   ```

## Notes

- Ensure you have the `db_utils.py` module for saving/loading reports.
- Compatible with Indian tax rules and formats.
- Designed to be robust even when input data is incomplete.

## License

MIT License. You are free to use, modify, and distribute this tool with attribution.
