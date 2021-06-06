# VideoTranslate
 
 This code consists of two microservices
 
 1. Pull YouTube video cuptions,translate them and put into Postgres DB in JSON format
 Request got to contain video id in url
 
 2. Get translated cuptions with pagination
 request got to contain video id with start and limit (page size) in url
 Response will contain the page and next, previous urls

Code is working with locally run PostgresSQL server, put in your credentials in
both model.py files