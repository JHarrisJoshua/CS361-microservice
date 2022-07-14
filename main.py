"""
Example of main project. Main project calls get_items function, which
will communicate with the microservices pipe to request and receive
information.
"""
from get_items import get_items


def main():
    """Example of individual project."""
    # Get data from microservice
    data = get_items()
    print(data)


if __name__ == "__main__":
    main()
