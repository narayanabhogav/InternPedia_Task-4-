import requests

# Function to fetch exchange rates
def fetch_exchange_rates(api_key):
    api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('conversion_rates')
    else:
        print("Error fetching exchange rates. Please check your API key and try again.")
        return None

# Function to convert currency
def currency_conversion(amount, source_currency, target_currency, exchange_rates):
    if source_currency == target_currency:
        return amount
    base_amount = amount / exchange_rates[source_currency]
    converted_amount = base_amount * exchange_rates[target_currency]
    return converted_amount

# Function to display currency conversion
def show_conversion(amount, source_currency, target_currency, converted_amount):
    print(f'{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}')

def main():
    api_key = '6908ddbf66540c364ca8dc58'  # Replace with your API key from ExchangeRate-API
    exchange_rates = fetch_exchange_rates(api_key)

    if exchange_rates is None:
        return

    available_currencies = list(exchange_rates.keys())
    while True:
        print("\nAvailable currencies:", ', '.join(available_currencies))
        source_currency = input("Enter the source currency code: ").upper()
        target_currency = input("Enter the target currency code: ").upper()

        if source_currency not in available_currencies or target_currency not in available_currencies:
            print("Invalid currency code. Please try again.")
            continue

        try:
            amount = float(input(f"Enter the amount in {source_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        converted_amount = currency_conversion(amount, source_currency, target_currency, exchange_rates)
        show_conversion(amount, source_currency, target_currency, converted_amount)

        continue_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if continue_conversion != 'yes':
            break

if __name__ == "__main__":
    main()
