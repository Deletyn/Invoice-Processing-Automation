# Invoice Processing Automation

## Project Overview

This project is a Python-based invoice processing and validation system developed to demonstrate how repetitive administrative tasks can be automated using Python.

The program reads invoice records from a CSV file, checks for common data errors and identifies invoices that require further review. It then generates a report containing the processing results.

## Features

- Reads invoice records from CSV files using Pandas.
- Checks for missing invoice IDs and supplier information.
- Identifies invalid invoice amounts.
- Detects unusually large invoice transactions.
- Identifies duplicate invoice IDs.
- Categorises invoices as either Passed or Requires Review.
- Generates a CSV report containing the processing results.
- Displays a summary of the invoices processed.

## Technologies Used

- Python 3.11
- Pandas
- CSV
- VS Code

## Project Structure

```text
invoice-processing-automation/
│
├── main.py
├── sample_invoices.csv
├── requirements.txt
│
└── reports/
    └── invoice_review_report.csv
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Deletyn/invoice-processing-automation.git
```

2. Navigate into the project directory:

```bash
cd invoice-processing-automation
```

3. Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Program

Execute the following command in your terminal:

```bash
python main.py
```

The program will process the sample invoice records and generate a report inside the `reports` directory.

## Output

The generated report contains:

- Invoice ID
- Supplier name
- Invoice date
- Invoice amount
- Review status
- Identified issues

Invoices are categorised into two groups:

- **Passed:** No validation issues detected.
- **Requires Review:** One or more validation issues detected.

## Future Improvements

Potential improvements include:

- Extracting invoice information automatically from PDF documents.
- Integrating machine learning for anomaly detection.
- Using OCR to extract information from scanned invoices.
- Connecting the system to accounting software.
- Developing a graphical user interface.

## Project Classification

This project currently uses rule-based automation rather than machine learning or generative AI. It applies predefined validation rules to invoice records and produces structured processing reports.

## Author

Tinotenda Bvirakare

BSc Information Technology (Data Science)
