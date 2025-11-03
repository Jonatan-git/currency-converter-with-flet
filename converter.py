import requests
from babel.numbers import format_currency
from locales import locales

def convert_currency(base_currency, target_currency, amount):
    url = f"your API{base_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        return "❌ Cannot Get API data."

    data = response.json()
    if "conversion_rates" not in data:
        return "❌ API Format did not match."

    rates = data["conversion_rates"]
    if target_currency not in rates:
        return "❌ Currency to convert cannot be found in API."

    rate = rates[target_currency]
    result = amount * rate

    base_locale = locales.get(base_currency, "en_US")
    target_locale = locales.get(target_currency, "en_US")

    formatted_input = format_currency(amount, base_currency, locale=base_locale)
    formatted_result = format_currency(result, target_currency, locale=target_locale)

    return f"{formatted_input} = {formatted_result}"