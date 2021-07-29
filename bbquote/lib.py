import requests


# def get_quote():
#     # url = 'https://movie-quote-api.herokuapp.com/v1/quote/'  # alternative API
#     url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
#     response = requests.get(url).json()[0]

#     return f"'{response['quote']}' \n> {response['author']}"


def get_quote():
    url = 'https://movie-quote-api.herokuapp.com/v1/quote/'  # alternative API
    response = requests.get(url).json()

    return f"'{response['quote']}' \n> {response['show']}"


if __name__ == "__main__":
    print(get_quote())
