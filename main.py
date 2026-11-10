
# importing modules to be used
import pandas as pd
import os

#setting the maximum invoice amount before it requires review
Amount_threshold = 10000

#function to read and process the invoice data
def process_invoices(file_path):

    #checking whether the input file exists
    if not os.path.exists(file_path):
        print("Error: Invoice File not Found")
        return

    #reading the invoice data from the csv file
    invoices = pd.read_csv(file_path)

    #checking whether all required columns are available
    required_columns = [
        "invoice_id", "supplier", "invoice_date", "amount", "status"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in invoices.columns
    ]

    if missing_columns:
        print(f"Error: Missing columns {missing_columns}")
        return

    #converting invoice amounts into numeric values
    invoices["amount"] = pd.to_numeric(
        invoices["amount"], errors="coerce"
    )

    #identifying all occurrences of duplicate invoice IDs
    duplicate_ids = invoices["invoice_id"].duplicated(keep=False)

    #creating a list to store the processing results
    issues = []

    #checking each invoice
    for index, invoice in invoices.iterrows():
        invoice_issues = []

        #checking for missing invoice ID
        if pd.isna(invoice["invoice_id"]) or str(
            invoice["invoice_id"]
        ).strip() == "":
            invoice_issues.append("Missing invoice ID")

        #checking for missing supplier information
        if pd.isna(invoice["supplier"]) or str(
            invoice["supplier"]
        ).strip() == "":
            invoice_issues.append("Missing supplier information")

        #checking for invalid invoice amounts
        if pd.isna(invoice["amount"]) or invoice["amount"] <= 0:
            invoice_issues.append("Invalid invoice amount")

        #checking for unusually large amounts
        elif invoice["amount"] > Amount_threshold:
            invoice_issues.append("Invoice amount exceeds threshold")

        #checking for duplicate invoice IDs
        if duplicate_ids.iloc[index]:
            invoice_issues.append("Duplicate invoice ID")

        #determining whether the invoice requires review
        if invoice_issues:
            review_status = "Requires Review"
            issue_description = ", ".join(invoice_issues)
        else:
            review_status = "Passed"
            issue_description = "No issues detected"

        #storing the processing results
        issues.append({
            "invoice_id": invoice["invoice_id"],
            "supplier": invoice["supplier"],
            "invoice_date": invoice["invoice_date"],
            "amount": invoice["amount"],
            "review_status": review_status,
            "issues": issue_description
        })

    #converting processing results into a dataframe
    report = pd.DataFrame(issues)

    #creating reports folder if there is none
    os.makedirs("reports", exist_ok=True)

    #saving the results
    report.to_csv("reports/invoice_review_report.csv", index=False)

    #calculating the processing statistics
    total_invoices = len(report)
    flagged_invoices = (
        report["review_status"] == "Requires Review"
    ).sum()
    passed_invoices = (
        report["review_status"] == "Passed"
    ).sum()

    #displaying the processing summary
    print("\n===== INVOICE PROCESSING SUMMARY =====")
    print(f"Total invoices processed: {total_invoices}")
    print(f"Invoices passed: {passed_invoices}")
    print(f"Invoices requiring review: {flagged_invoices}")
    print("Report saved to reports/invoice_review_report.csv")
    print("======================================")


#running the program
if __name__ == "__main__":
    process_invoices("sample_invoices.csv")
