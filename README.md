# 2FA Extension for ulauncher

Generate pin codes for two factor authentication.

## Settings
There are only a few settings available

*generate pin keyword*
default: 2fa   
This is the keyword to activate this ulauncher. If you type a argument after the keyword it will be used to filter the providers.

*providers*
default:   
This field contains one entry per line. Each line will contain a name and a secret seperated by a equals sign.
Example:
```
gitlab=abcd efgh 1234 fake fake 4321
gitlab=1236 1248 test fail
```

## Requirements
For this extension the onetimepass python library is needed.
```
pip install onetimepass
```

## Disclaimer
This software is delivered free of charge and without warranty.
Make sure you always make backup keys for your accounts.
I am not responsible for any loss of data.

## Licenses
All rights off third party libraries or images remain to the original authors.

Big thanks to the following authors
* ulauncher
* onetimepass (totp library)
* zimbra (logo)
* python
