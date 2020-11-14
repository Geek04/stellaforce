# stellaforce
Basic protection for freelance projects.

# Usage (as a cmd-line program)
```
stellaforce [--help, -h] --key KEY [--etype ETYPE] --ftype [--ftype FTYPE] --verbose P
positional arguments:
  P              Path to JSON file to be encrypted.

keyword arguments:
  -h, --help     show this help message and exit
  --key KEY      Private key for data to be encrypted.
  --etype ETYPE  Type of encryption to be used. Supported types: Fernet.
                 Default: Fernet
  --ftype FTYPE  Type of file type. Supported types: JSON. Default: JSON
  --verbose      If added, prints out encrypted data```
