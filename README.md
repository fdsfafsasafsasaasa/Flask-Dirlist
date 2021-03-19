# Flask directory list with password auth

* To add a user, edit the `USERS` variable in `main.py`.  
	For example:  
	```
	USERS = {"username": generate_password_hash("password"), "new username here": generate_password_hash("new password here")}
	```  
* Add new files and directories you want in the `content` folder.