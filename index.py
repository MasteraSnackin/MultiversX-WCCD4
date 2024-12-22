# Import necessary modules
import json  # Module for working with JSON data
from multiversx_sdk_core import Address  # Import Address class for handling blockchain addresses
from multiversx_sdk_network_providers import ProxyNetworkProvider  # Import network provider class for interacting with the blockchain

# Define the network provider (devnet in this case)
# ProxyNetworkProvider is used to interact with the MultiversX blockchain through a specific API endpoint.
# Here, we are connecting to the devnet API, which is a test network.
provider = ProxyNetworkProvider("https://devnet-api.multiversx.com")

# List of account addresses to query
# These are the blockchain addresses you want to query for transactions.
# You need to replace the placeholder values ("erd1...") with actual addresses.
accounts = [
    "erd1...",
    "erd1...",
    # Add more accounts as needed
]

# Function to retrieve transactions for a given account
def get_transactions_for_account(account_address):
    try:
        # Convert the string address to an Address object
        address = Address.from_bech32(account_address)
        
        # Fetch transactions for the given address
        # The 'with_results=True' parameter indicates that you want detailed results.
        transactions = provider.get_account_transactions(address, with_results=True)
        
        # Return the list of transactions
        return transactions
    except Exception as e:
        # Handle exceptions by printing an error message
        print(f"Error fetching transactions for account {account_address}: {e}")
        
        # Return an empty list if there was an error
        return []

# Main function to execute the script
def main():
    # Dictionary to store all transactions for each account
    all_transactions = {}
    
    # Iterate over each account address
    for account in accounts:
        # Retrieve transactions for the current account
        transactions = get_transactions_for_account(account)
        
        # Store the transactions in the dictionary
        all_transactions[account] = transactions

    # Save the transactions to a JSON file
    with open("transactions.json", "w") as outfile:
        # Serialize the dictionary to a JSON formatted stream and write to the file
        json.dump(all_transactions, outfile, indent=4)

    # Print confirmation message
    print("Transactions have been saved to transactions.json")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()