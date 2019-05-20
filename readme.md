```
> python send.py -h
usage: send.py [-h] [-f EFROM] [-p PASSWORD] [-t TO] [-s SERVER] [-m MESSAGE]
               [-ti TITLE] [-n NAME] [-rn RECIPIENT_NAME]

Simple email sender.

optional arguments:
  -h, --help            show this help message and exit
  -f EFROM, --from EFROM
  -p PASSWORD, --password PASSWORD
  -t TO, --to TO
  -s SERVER, --server SERVER
                        smtp server
  -m MESSAGE, --message MESSAGE
  -ti TITLE, --title TITLE
  -n NAME, --name NAME
  -rn RECIPIENT_NAME, --recipient_name RECIPIENT_NAME

```

```
> python recv.py -h
usage: recv.py [-h] [-e EMAIL] [-p PASSWORD] [-s POP3_SERVER]

Simple pop3 receiver.

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
  -p PASSWORD, --password PASSWORD
  -s POP3_SERVER, --pop3_server POP3_SERVER

```
