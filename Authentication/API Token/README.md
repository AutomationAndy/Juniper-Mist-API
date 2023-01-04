# API Token #

## Overall Description ##

<https://api.mist.com/api/v1/docs/Auth#api-token>

Your API token is step 1 of any project. You need a token to do just about anything else in this repo. This is kind of a chicken and the egg scenario though. You need an API token to use any of the API token examples, but you don't have an API token yet because you can't run the script to generate a new one without a token. The easiest way around this is to just generate an API token from the Mist dashboard (Org > Settings > API Token), or use the Django example since it uses your currently logged in account to authenticate you. 
  
Tokens can also be setup on the Mist dashboard under Organization > Settings then the "API Token" box. You can setup tokens that only have access to specific things, like sites, site groups, or user roles like observer (read-only) or super user (read/write).  
  
I suggest you create a token per project/integration with only the access required for your project. This way if something breaks or someone gets your token you can just delete the token and it wont affect any other automation projects you have.

## File Descriptions ##

<b>Create-API-Token_Django.md</b> - Placeholder File        <i>-- Not Complete --</i>  
<b>Create-API-Token_Python.py</b> - Placeholder File        <i>-- Not Complete --</i>  
<b>Create-API-Token_Ansible.yml</b> - Placeholder File      <i>-- Not Complete --</i>  

<b>Delete-API-Token_Django.md</b> - Placeholder File        <i>-- Not Complete --</i>  
<b>Delete-API-Token_Python.py.py</b> - Placeholder File     <i>-- Not Complete --</i>  
<b>Delete-API-Token_Ansible.yml.yml</b> - Placeholder File  <i>-- Not Complete --</i>  

<b>List-API-Token_Django.md</b> - Placeholder File          <i>-- Not Complete --</i>  
<b>List-API-Token_Python.py.py</b> - Placeholder File       <i>-- Not Complete --</i>  
<b>List-API-Token_Ansible.yml.yml</b> - Placeholder File    <i>-- Not Complete --</i>  

<b>Use-API-Token_Django.md</b> - Placeholder File           <i>-- Not Complete --</i>  
<b>Use-API-Token_Python.py.py</b> - Placeholder File        <i>-- Not Complete --</i>  
<b>Use-API-Token_Ansible.yml.yml</b> - Placeholder File     <i>-- Not Complete --</i>  

| File Name | Description |
| ---       | ---         |
| test1     | test-a      |
| test2     | test-b      |