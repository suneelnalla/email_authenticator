
# email_authenticator
1. OAuth2 Authentication:
The script uses the google-auth-oauthlib and google-auth libraries to handle OAuth2 authentication, which is more secure than using plain text passwords.
The authenticate_gmail function handles the authentication process, including refreshing the token if necessary.
2. IMAP Authentication with OAuth2:
The generate_oauth2_string function creates the OAuth2 string needed for authentication with Gmail’s IMAP server.
This approach is more secure and in line with Google's requirements for accessing Gmail via IMAP.
3. Fetching and Saving Emails:
The script fetches all emails from the inbox and saves them as text files in a specified directory.
