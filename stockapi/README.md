# Description

Wall Street microservice is the rest API which provides various endpoints.
Application requires SSL certificate.

# Requirement
| Software | Version|
|-|-|
|Python | 3.8|
|PSQL| ??|

# Endpoints
All of below API endpoint requires JWT token for authentication purpose except /ping
| Method | endpoint | Description|
|-|-|-|
|Get | /ping| Check connectivity
|Get| /ping-auth| Check validity of token|
|Post| /user| Create new user|
|GET| /login | Custom Login|
|GET| /google-login| Login using google SSO
|GET| /current-user| Get details of current user|

# Steps to run locally
   
  - setup virtual environment - [Refer this link](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
       - python3 -m venv venv 
       - For Linux
          ```
               source venv/bin/activate
          ```
       - For Windows
          ```
               .\venv\Scripts\activate
			   
				
          ```  
  - Edit [config.py](config.py)		  
  - Execute following commands
		```
			pip install -r requirements.txt
			pyhton3 main.py
		```
		or
		```
			./startup_script.sh
		```
     - Endpoints collection   

          <img height="250" src="../../../../var/folders/sy/5qpcn7195g106ffzf67csmj00000gn/T/TemporaryItems/NSIRD_screencaptureui_SAglul/Screen Shot 2021-11-10 at 1.06.22 PM.png" width="250"/>
    

# How to test API:
-	Postman collection : https://www.getpostman.com/collections/d8f8d57058c7fb9cf592
- Postman Workspace is [here](https://red-water-456173.postman.co/workspace/Masters~2bab25bd-2e03-4f98-a016-be9b91b3d7b5/collection/2280968-1662f3d0-65eb-4d7a-beb9-3c01a2dbff67?ctx=documentation)
			

