# DataAccess
Navigate to this directorty and execute: `python app.py`

 # IAM DB Authentication
```
CREATE USER 'nssp-mb-app-user'@'%' IDENTIFIED WITH AWSAuthenticationPlugin as 'RDS';
GRANT EXECUTE, SELECT, DELETE, INSERT, UPDATE ON sia.* TO 'nssp-mb-app-user'@'%';
FLUSH PRIVILEGES;
```

RDS Access Policy
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "rds-db:connect",
            "Resource": "arn:aws:rds-db:us-east-1:103346953322:dbuser:cluster-NY2H7O547KOFSNIZB5O3ZWAIYM/nssp-mb-app-user",
            "Effect": "Allow"
        }
    ]
}
```