# Clone WLAN to New Org #

## What it Does ##

Clone a WLAN from one Organization to another using Python.

## Why ##

Original use-case was that a managed service provider wanted to copy a golden WLAN Template from one of their customers to another. As of writing this, you can't clone WLAN's or their templates from one Organization to another, so this will at least copy the WLAN configuration from one to another, then you can manually create a WLAN Template with the new WLAN(s).

## Instructions ##

1. Create a read-only API token on the Org you want to copy the WLAN from
2. Copy the API token into line 10, in the variable Mist_Org1_Token
3. Copy the Org ID for this Org to line 11, in the variable Mist_Org1_ID
4. Copy the Site ID for the WLAN you want to copy into line 12, in the variable Mist_Site1_ID
5. Copy the WLAN ID of the WLAN you want to copy into line 13, in the variable Mist_wlan1_ID 

6. Create a read-write API token on the Org you want to clone the WLAN to
