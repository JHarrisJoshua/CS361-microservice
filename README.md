# CS361-microservice

## Table of Contents
* [Overview](#Overview)
* [UML Sequence Diagram](#UML-Sequence-Diagram)
* [Video Demo](#Video-Demo)

## Overview
### Description
A microservice for web-scraping html tables from video game wiki pages for group partner's individual project.

### Files
**main.py**

A contrived example of a program that could call a function that sends a request to the communication pipe. The function receives the data and returns a dictionary with the item data to the main program.

**get_items.py**

A function called by the main program. The function sends the request to the microservice communication pipe and retrieves the name of the JSON file with the data from the communication pipe.  

##### Requesting Data

To request data from the microservice, get_items writes "Get Weapon Data" to the communication pipe (pipe.txt). This will tell the microservice to scrape data from a video game wiki page that contains information about in-game weapons.  

```python
# Example call 1 - sending a request
def get_items():
    # Send Request
    with open("pipe.txt", "w") as file:
        file.write("Get Weapon Data")

```

##### Receiving Data

Once a request is sent and received by the microservice, the microservice saves the data to a JSON file (which it creates if it doesn't exist). It then returns the name of the file to the communication pipe. To receive the data from the microservice, get_items reads the name of the JSON file from the communication pipe.

```python
    # Example call 2 - receiving the file name
    received = False
    while not received:
        with open("pipe.txt", "r") as file:
            line = file.read()
            time.sleep(.1)
            if line[:3] == "Get":
                print( "waiting...")
                time.sleep(.1)
            else:
                file_name = line
                print("File Received")
                received = True

```

```python
   # Example 3 - opening the file
   with open(file_name, 'r') as infile:
       item_data = json.load(infile)
```

**pipe.txt**

The communication pipe. Receives messages from the main program's function, as well as from the microservice program.

**dndscraper.py**

The microservice - upon receipt of the request, uses beautiful soup to retrieve information about in-game items and their attributes from a community wiki page. 

**weapon_data.json**

In the example above, the information related to in-game weapons and their attributes is stored in a JSON file. The name of the file is returned to the communication pipe, which the main program's function can use to open the file and retrieve the scraped data. 

## UML Sequence Diagram

![UML Sequence Diagram](https://user-images.githubusercontent.com/81477294/178848321-e4e2024f-4c7d-4972-98db-eead32ef9f0f.png)

## Video Demo
Here's a Demo of the Microservice:

https://www.youtube.com/watch?v=-3f5Cr0Ud9w
