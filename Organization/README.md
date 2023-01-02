# Organization APIs #

## Description ##

You'll probably spend most of your time in these and Site APIs. This is where you can mess with all kinds of stuff. Remember to try to use Org and Site level API Tokens one per integration, and create them with appropriate priviledges. Does your script only need to read one site in an org? Make a read-only site token for it. Does it need to create new sites automatically based on some input (like a csv file or something)? It'll need to be an org level read-write (super user) token.  