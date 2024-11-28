def test_emails():
    test_cases = [
        "qvahxzeueq@nhs.net",
        "rwvqhptft@nhs.net",
        "njvun@nhs.net",
        "omkueltb@gov.uk",
        "qpzyqnlaq@nhs.net",
        "dkf*ggnu@gov.uk", 
        "mtnurpnn@gov.uk",
        "wiq)jadaa@nhs.net", 
        "fph@jp@ac.uk",  
        "euktfrzm@gov.uk"
    ]
    for email in test_cases:
        print(f"Testing '{email}:{validate_email(email)}")

if __name__ == "__name__":
    test_emails

