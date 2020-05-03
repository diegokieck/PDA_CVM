# PDA_CVM
This project aims to continually mine CVM data from Brazil's Open Data Platform.

## Dependencies
This projects uses the following Python Packages:
Requests
BeautifulSoup4
Psycopg2

## Usage

When run retrieves data from REPOSITORY url. 
For csv file in the remote repository, the program checks if the local copy is updated. If it's not, the program downloads the updated version.

The local_files.txt file keeps track of local files and version. 

Local files are stored in Tabelas_locais Folder.
## To-do 

* Create Postgres Database and Schema
* Integrate with Postgres
* Compare remote file and local file and store updates
* Generate setup script with asdf and pipenv
