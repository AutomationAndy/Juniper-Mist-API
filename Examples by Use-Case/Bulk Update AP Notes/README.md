# Export Inventory to CSV #

## What does it do? ##

Updates the Notes section of Access Points inside an Organization.

## Why did we need it? ##

The use-case is that if an organization physically labels access points with asset tags that are then tracked in an Excel spreadsheet, it would be nice to be able to reference that asset tag somehow in the Mist Dashboard.

## Instructions ##

1. Create a read-write API token in the Mist dashboard. From the navigation pane navigate to Organization > Settings then there's a section for API Tokens
2. Paste your API token into line 9, variable Token
3. Run [Export Inventory to CSV example](Export_Inventory_CSV.py) to generate output.csv and copy/paste it into the directory you're running this script in
4. Create a new column in output.csv and name it 'notes'
5. Populate whatever notes you want to add to the device and run the script

## Notes ##

This is designed to be used with the output.csv from the [Export Inventory to CSV example](Export_Inventory_CSV.py) because we need the AP's ID's, and the Site ID they're assigned to so this is an easy way to get them, but really all the script needs to run is a csv file in the same directory named 'output.csv' with a column named 'id' with the AP's you want the notes section modified for, a column named 'site_id' with the site ID info for that AP's ID and a column named 'notes' populated with whatever notes you want add to at AP.

## Credits / Collaborators / Idea Makers ##

Lam T.