# 0x14. JavaScript - Web scraping

Web scraping in JavaScript involves the extraction of data from websites by programmatically interacting with HTML and CSS web pages. Actually JS languages best suites the process of web-scraping due to its ability to manipulate the Document Object Model(DOM) and asynchronous operations that are very common in web page interactions. 
This folder looks into the practice of web scraping in the following tasks:

## Task 0: Readme

File:

	- 0-readme.js
A script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object



## Task 1: Write me

File:

	- 1-writeme.js
A script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object



## Task 2: Status code

File:

	- 2-statuscode.js
A script that display the status code of a GET request.
* The first argument is the URL to request (GET)
* The status code must be printed like this: code: <status code>
* You must use the module request



## Task 3: Star wars movie title

File:

	- 3-starwars_title.js
A script that prints the title of a Star Wars movie where the episode number matches a given integer.
* The first argument is the movie ID
* You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
* You must use the module request 


## Task 4: Star wars Wedge Antilles

File:

	- 4-starwars_count.js
A script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
* Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
* You must use the module request



## Task 5: Loripsum

File:

	- 5-request_store.js
A script that gets the contents of a webpage and stores it in a file.
* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module request



## Task 6: How many completed?

File:

	- 6-completed_tasks.js
A script that computes the number of tasks completed by user id.
* The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
* Only print users with completed task
* You must use the module request



## Task 7: Who was playing in this movie?

File:

	- 100-starwars_characters.js
A script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line
* You must use the Star wars API
* You must use the module request



## Task 8: Right order

File:

	- 101-starwars_characters.js
Script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: 3 = “Return of the Jedi”
* Display one character name by line in the same order of the list “characters” in the /films/ response
* You must use the Star wars API
* You must use the module request
