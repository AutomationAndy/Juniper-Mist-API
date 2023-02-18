# Export Inventory to CSV #

## What does it do? ##

Exports the inventory of an Org to a CSV file.

## Why did we need it? ##

Orignially built to grab the 'magic' column of an Organization's AP inventory, rebuilt for a new use-case of bulk editing the notes section of AP's. We need IDs and other details from the inventory of the Organization so that we can use it later in another script. This was written so that it should include firewalls, switches, and whatever else comes out of the API call.

## Instructions ##

1. Create a read-only API token in the Mist dashboard. From the navigation pane navigate to Organization > Settings then there's a section for API Tokens
2. Paste your API token into line 9, variable Token.
3. Paste your Org ID into line 10, variable OrgID. You can find your Org ID from your Mist dashboard in Organizaton > Settings

## Notes ##

This will create a file called 'output.csv' in the same directory as this python script. The 'magic' column is the claim/activation code for the device.

## Credits / Collaborators / Idea Makers ##

Garth H.