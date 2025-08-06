def fetch_case_details(case_type, case_number, year):
    return {
        "case": f"{case_type} {case_number} / {year}",
        "parties": "Alice vs Bob",
        "filing_date": "2022-03-10",
        "next_hearing": "2025-09-15",
        "order_pdf": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    }
