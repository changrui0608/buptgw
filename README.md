# buptgw

an ultility script for BUPT gateway login, logout ...

easier login in CLI

written in Python, Python2 env is required

## usage

```
python buptgw.py <login|logout|stats> [options]
```
```
Options:
    -u  --user     <username>   specify the gateway account name
    -p  --password <password>   specify the gateway account password
```
example:
```
python bupt.py login
python bupt.py login -u 2016123456
python bupt.py login -u 2016123456 -p 123456
python bupt.py logout
```

## issues

- give success notification when login failed
    - wrong username/password
    - the account already logged in with max number of devices
    - ...
- stats function has not implemented yet
- have not test in case of password containing special characters

