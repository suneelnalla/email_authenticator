# # import imaplib
# # import email
# # from email.header import decode_header
# # import os

# # # Email account credentials
# # username = "suneelnalla123@gmail.com"
# # password = "Sunny@79955"

# # # Create an IMAP4 class with SSL 
# # mail = imaplib.IMAP4_SSL("imap.gmail.com")
# # # Authenticate
# # mail.login(username, password)

# # # Select the mailbox you want to use
# # mail.select("inbox")

# # # Search for all emails in the inbox
# # status, messages = mail.search(None, "UNSEEN")
# # # Convert messages to a list of email IDs
# # email_ids = messages[0].split()

# # # Function to extract email body
# # def get_email_body(msg):
# #     if msg.is_multipart():
# #         for part in msg.walk():
# #             content_type = part.get_content_type()
# #             if content_type == "text/plain" and "attachment" not in part.get("Content-Disposition"):
# #                 return part.get_payload(decode=True).decode()
# #     else:
# #         return msg.get_payload(decode=True).decode()

# # # Directory to store emails
# # output_dir = "D:\python_scripts\mail_automation_results"
# # if not os.path.exists(output_dir):
# #     os.makedirs(output_dir)

# # # Process each email
# # for email_id in email_ids:
# #     status, msg_data = mail.fetch(email_id, "(RFC822)")
# #     for response_part in msg_data:
# #         if isinstance(response_part, tuple):
# #             msg = email.message_from_bytes(response_part[1])
# #             subject, encoding = decode_header(msg["Subject"])[0]
# #             if isinstance(subject, bytes):
# #                 subject = subject.decode(encoding if encoding else "utf-8")
# #             from_ = msg.get("From")
# #             body = get_email_body(msg)
            
# #             # Store email in a text file
# #             file_name = f"{output_dir}/{subject[:50]}.txt"
# #             with open(file_name, "w", encoding="utf-8") as f:
# #                 f.write(f"Subject: {subject}\n")
# #                 f.write(f"From: {from_}\n")
# #                 f.write(f"Body:\n{body}")

# # # Logout
# # mail.logout()
# import imaplib
# import email
# from email.header import decode_header
# import os

# try:
#     # Email account credentials
#     username = "venomcyberrrr@gmail.com"
#     password = "znKr7C85jSqLBR43"

#     # Create an IMAP4 class with SSL 
#     mail = imaplib.IMAP4_SSL("imap.gmail.com")
#     print("Connected to the email server.")

#     # Authenticate
#     mail.login(username, password)
#     print("Logged in as", username)

#     # Select the mailbox you want to use
#     mail.select("inbox")
#     print("Inbox selected.")

#     # Search for all emails in the inbox
#     status, messages = mail.search(None, "UNSEEN")
#     if status != "OK":
#         print("Error searching inbox.")
#         exit()

#     # Convert messages to a list of email IDs
#     email_ids = messages[0].split()
#     print(f"Found {len(email_ids)} emails.")

#     # Function to extract email body
#     def get_email_body(msg):
#         if msg.is_multipart():
#             for part in msg.walk():
#                 content_type = part.get_content_type()
#                 if content_type == "text/plain" and "attachment" not in part.get("Content-Disposition"):
#                     return part.get_payload(decode=True).decode()
#         else:
#             return msg.get_payload(decode=True).decode()

#     # Change the directory to store emails
#     output_dir = "emails"  # Change this to your desired path

#     # Create the directory if it doesn't exist
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#         print("Created directory:", output_dir)

#     # Process each email
#     for email_id in email_ids:
#         status, msg_data = mail.fetch(email_id, "(RFC822)")
#         for response_part in msg_data:
#             if isinstance(response_part, tuple):
#                 msg = email.message_from_bytes(response_part[1])
#                 subject, encoding = decode_header(msg["Subject"])[0]
#                 if isinstance(subject, bytes):
#                     subject = subject.decode(encoding if encoding else "utf-8")
#                 from_ = msg.get("From")
#                 body = get_email_body(msg)
                
#                 # Store email in a text file
#                 file_name = f"{output_dir}/{subject[:50].replace('/', '_').replace('\\', '_')}.txt"
#                 with open(file_name, "w", encoding="utf-8") as f:
#                     f.write(f"Subject: {subject}\n")
#                     f.write(f"From: {from_}\n")
#                     f.write(f"Body:\n{body}")
#                 print(f"Saved email: {file_name}")

#     # Logout
#     mail.logout()
#     print("Logged out.")

# except Exception as e:
#     print("An error occurred:", str(e))
import os
import base64
import imaplib
import email
from email.header import decode_header
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Path to your credentials file
credentials_path = 'D:\python_scripts\crdentials'
token_path = 'token.json'

# Scopes required by Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return creds

def generate_oauth2_string(username, creds):
    auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, creds.token)
    return 'user=%s\1auth=Bearer %s\1\1' % (username, creds.token)

def fetch_emails():
    creds = authenticate_gmail()
    username = "suneelnalla123@gmail.com"

    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    # Authenticate using OAuth2
    auth_string = generate_oauth2_string(username, creds)
    mail.authenticate('XOAUTH2', lambda x: auth_string)
    print("Logged in as", username)

    mail.select("inbox")
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    print(f"Found {len(email_ids)} emails.")

    output_dir = "emails"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                from_ = msg.get("From")
                body = get_email_body(msg)
                
                file_name = f"{output_dir}/{subject[:50].replace('/', '_').replace('\\', '_')}.txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(f"Subject: {subject}\n")
                    f.write(f"From: {from_}\n")
                    f.write(f"Body:\n{body}")
                print(f"Saved email: {file_name}")

    mail.logout()
    print("Logged out.")

def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain" and "attachment" not in part.get("Content-Disposition"):
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()

if __name__ == "__main__":
    fetch_emails()

