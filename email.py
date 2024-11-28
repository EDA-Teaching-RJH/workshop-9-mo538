import re



def validate_email(email):

    # Define the regex pattern

    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(ac\.uk|gov\.uk|nhs\.net)$'

    

    # Match the email against the pattern

    match = re.match(pattern, email)

    if not match:

        if "@" not in email:

            return "Invalid email: Missing '@' symbol."

        username, _, domain = email.partition('@')

        if not username.isalnum():

            return "Invalid email: Username contains invalid characters. Only letters and numbers are allowed."

        if "." not in domain:

            return "Invalid email: Missing domain suffix (e.g., '.ac.uk')."

        if not re.match(r'^[a-zA-Z0-9]+\.[a-z]{2,}$', domain):

            return "Invalid email: Domain contains invalid characters or structure."

        if not domain.endswith(('.ac.uk', '.gov.uk', '.nhs.net')):

            return "Invalid email: Unsupported domain suffix."

        return "Invalid email: Unknown issue."

    

    # Determine the domain type

    if email.endswith('.ac.uk'):

        return "Valid Academic Email"

    elif email.endswith('.gov.uk'):

        return "Valid Government Email"

    elif email.endswith('.nhs.net'):

        return "Valid NHS Email"



def main():

    email = input("Enter an email address: ").strip()

    feedback = validate_email(email)

    print(feedback)



if __name__ == "__main__":

    main()