# Authentication APIs #

## Description ##

This set of APIs handle account based actions like creating account tokens, registering, un-registering and checking status/priviledges of accounts. Tokens created here are more for automating actions with your account, rather than the organization and site tokens that are for specific integrations. An example would be that if you had access to multiple Mist organizations and wanted to run a script against every org you have access to, you'd use this level of token.  

Very rarely should you use this type of token. It has the same priviledges you do so its possible to mess up a lot all at once. You should create an ogranization or site level token instead.
