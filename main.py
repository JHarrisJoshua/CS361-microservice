"""
Example of main project. Main project calls get_stats function, which
will communicate with the microservices pipe to request and receive
information.
"""
from get_stats import get_stats


def main():
    """Example of individual project."""
    # Get data from microservice
    data = get_stats()
    print(data)


if __name__ == "__main__":
    main()
