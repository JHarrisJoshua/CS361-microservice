# CS361-microservice

## Table of Contents
* [Overview](#Overview)
* [UML Sequence Diagram](#UML)
* [Video Demo](#Video-Demo)

## Overview
### Description
A microservice for web-scraping html data from video game wiki pages for group partner's individual project.

### Files
**main.py**

A contrived example of a program that could call a function that sends a request to the communication pipe. The function returns a list with the data, which the main program then prints out.

**get_stats.py**

A function called by the main program. The function sends the request to the microservice communication pipe and retrieves the name of the JSON file with the data from the pipe.  

##### Requesting Data

To request data from the microservice, get_stats writes "Get Weapon Stats" to the communication file. This will tell the microservice to scrape data from a video game wiki page that contains information about in-game weapons.  

##### Receiving Data

Once a request is sent and received by the microservice, to receive data from the microservice, get_stats reads the name of the JSON file from the communication pipe. 

**pipe.txt**

The communication pipe. Receives messages from the main program's function, as well as from the microservice program.

**dndscraper**

The microservice - upon receipt of the request, uses beautiful soup to retrieve the html associated with a table of in-game items and their attributes from a community wiki page. 



**weapon_stats.json**

In the example above, the raw html information related to in-game weapons and their attributes is stored in a JSON file. The name of the file is returned to the communication pipe, which the main program can use to open the file and retrieve the scraped html. 





## UML Sequence Diagram


## Video Demo
Here's a Demo of the Microservice:
<https://www.youtube.com/watch?v=UUVHhgp3N5Q>
