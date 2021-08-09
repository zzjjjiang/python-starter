# DataAccess
Navigate to this directorty and execute: `python app.py`

 # Create DB User
```
CREATE USER 'nssp-mb-app-user'@'%' IDENTIFIED WITH AWSAuthenticationPlugin as 'RDS';
GRANT EXECUTE, SELECT, DELETE, INSERT, UPDATE ON sia.* TO 'nssp-mb-app-user'@'%';
FLUSH PRIVILEGES;
```