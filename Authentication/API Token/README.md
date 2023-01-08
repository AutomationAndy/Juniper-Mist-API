# API Token #

## Overall Description ##

<https://api.mist.com/api/v1/docs/Auth#api-token>

Your API token is step 1 of any project. You need a token to do just about anything else in this repo. This is kind of a chicken and the egg scenario though. You need an API token to use any of the API token examples, but you don't have an API token yet because you can't run the script to generate a new one without a token. The easiest way around this is to just generate an API token from the Mist dashboard (Org > Settings > API Token), or use the Django example since it uses your currently logged in account to authenticate you. 
  
Tokens can also be setup on the Mist dashboard under Organization > Settings then the "API Token" box. You can setup tokens that only have access to specific things, like sites, site groups, or user roles like observer (read-only) or super user (read/write).  
  
I suggest you create a token per project/integration with only the access required for your project. This way if something breaks or someone gets your token you can just delete the token and it wont affect any other automation projects you have.

## File Descriptions ##

| File Name                                                                 | Description                       |
| ---                                                                       | ---                               |
| [Create-API-Token_Django.md](Create-API-Token_Django.md)                  |        <i>-- Not Complete --</i>  |
| [Create-API-Token_Python.py](Create-API-Token_Python.py)                  |        <i>Done</i>  |
| [Create-API-Token_Ansible.yml](Create-API-Token_Ansible.yml)              |        <i>-- Not Complete --</i>  |
|                                                                                                               |
|                                                                                                               |
| [Delete-API-Token_Django.md](Delete-API-Token_Django.md)                  |        <i>-- Not Complete --</i>  |
| [Delete-API-Token_Python.py](Delete-API-Token_Python.py)                  |        <i>Done</i>  |
| [Delete-API-Token_Ansible.yml](Delete-API-Token_Ansible.yml)              |        <i>-- Not Complete --</i>  |
|                                                                                                               |
|                                                                                                               |
| [List-API-Token_Django.md](List-API-Token_Django.md)                      |        <i>-- Not Complete --</i>  |
| [List-API-Token_Python.py](List-API-Token_Python.py)                      |        <i>Done</i>  |
| [List-API-Token_Ansible.yml](List-API-Token_Ansible.yml)                  |        <i>-- Not Complete --</i>  |
|                                                                                                               |
|                                                                                                               |
| [Use-API-Token_Django.md](Use-API-Token_Django.md)                        |        <i>-- Not Complete --</i>  |
| [Use-API-Token_Python.py](Use-API-Token_Python.py)                        |        <i>-- Not Complete --</i>  |
| [Use-API-Token_Ansible.yml](Use-API-Token_Ansible.yml)                    |        <i>-- Not Complete --</i>  |