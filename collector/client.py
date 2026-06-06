import requests


BASE_URL = "https://fapi.binance.com"


def get_data(
    endpoint,
    params=None,
    timeout=10
):
    """
    Generic GET request
    Binance Futures API
    """

    try:

        response = requests.get(
            BASE_URL + endpoint,
            params=params,
            timeout=timeout
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print(
            f"[API ERROR] {e}"
        )

        return None