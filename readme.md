# Blockchain Transactions Query Script

This project provides a script to query the MultiversX blockchain for a list of transactions associated with specific account addresses. The script uses the MultiversX SDK for Python to interact with the devnet API.

## Features

- Query transactions for multiple blockchain accounts.
- Output results in a JSON file for easy analysis and verification.
- Easily configurable to add or remove account addresses.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.6 or higher
- `pip` for managing Python packages
- Internet access to connect to the MultiversX devnet API

## Setup

1. **Clone the Repository**

   Clone the repository to your local machine using:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
Install Required Packages

Install the necessary Python packages using pip:

pip install multiversx_sdk
Configure Account Addresses

Open the script file and replace the placeholder account addresses ("erd1...") with the actual addresses you wish to query:

accounts = [
    "erd1...",
    "erd1...",
    # Add more accounts as needed
]
Usage
To execute the script and retrieve transactions, run the following command:

bash
Copy
python script_name.py
Replace script_name.py with the actual name of your script file.

Output
After running the script, a JSON file named transactions.json will be created in the same directory. This file contains the list of transactions for each queried account address, formatted as follows:

json
Copy
{
    "account1": [...],
    "account2": [...],
    ...
}
Troubleshooting
Network Issues: Ensure you have a stable internet connection to access the devnet API.
Invalid Addresses: Verify that all account addresses are correctly formatted in Bech32.
Additional Resources
For more information on using the MultiversX SDK for Python, refer to the official documentation:

MultiversX SDK for Python Cookbook
MultiversX Devnet Explorer
MultiversX REST API Documentation
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Copy

### Explanation

- **Introduction**: Provides an overview of what the script does and its main features.
- **Prerequisites**: Lists the software and tools needed to run the script.
- **Setup**: Guides the user through cloning the repository and installing necessary packages.
- **Usage**: Explains how to run the script and the expected output.
- **Troubleshooting**: Offers solutions for common issues that might arise.
- **Additional Resources**: Provides links to useful documentation and resources related to the MultiversX SDK.
- **Contributing and License**: Encourages contributions and specifies the licensing of the project.

This template should help users quickly understand how to set up and use your script effectively. Adjust it as needed to fit your specific project details.