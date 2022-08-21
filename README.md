This poc is for a change stream watcher to propagate changes from a mongodb collection to a postgreSQL db
``` connection strings were hard coded and left in the project but those configurations are not exposed to the internet and were deleted after project completion ```
# DB Configurations#

The configuration for the test was as follows three a mongodb containers running in a replica set running on docker on a local network.
with the database people and the collection people

A postgreSQL container running in docker on the local network
with the database changePOC and table people with the following fields: 
id serial PRIMARY KEY,
username varchar(20) not null

A user post was created in the postgres environment with the password post 
post was granted login; select, insert, update, and delete on people;
as well as select, usage, and update on people_id_seq

# Application Setup#
Two python scripts run to demonstrate the poc.  
1. The first is a flask application that makes changes to the postgres database from requests made to the api.  
The flask app will need a virtual environment with the dependencies defined in the requirements.txt file.  
Start the flask app with the `python -m app` command from the root directory of the project.
2. The second is a simple script  that watches a change stream and invokes the flask api depending on what is watched.
The change stream script needs both the `Requests` package and the `pymongo` package installed into a virtual environment.
Start the change stream script with the `python -m change_stream` command from the root directory of the project.

# Behavior#
Whenever both applications are running on localhost when a document is inserted into people.people with the key "name" present in the document a row will be added to the people table in postgres with the value of "name" as the username

