# PDA_CVM
This project aims to continually mine CVM data from Brazil's Open Data Platform.

## Dependencies
This projects uses the following Python Packages:
Requests
BeautifulSoup4
Psycopg2

## Usage

When run retrieves data from REPOSITORY url. 
For csv file in the remote repository, the program checks if there is a local copy and if the local copy is up to date. 
The local_files.txt file keeps track of local files and version.

## To-do 

* Create Postgres Database and Schema
* Integrate with Postgres
* Compare remote file and local file and store updates
* Generate setup script with asdf and pipenv
