# fload
fload is a data processing toolkit.
It uses:

    * Json 
    * linux pipe

# Concepts
## Source

Each source outputs a series of json lines

## Pipeline

Each pipeline consumes lines of json, and output new lines of json.

# Modules

## csv

```bash
fload csv xx.csv
```


## imap

### combine doc id:

```bash
fload imap --imap-server=xxx --imap-port=xxx --imap-user=user --imap-pass=PassW0Rd --start-uid-file=mailbox_uid.txt \
| jq -ca '. + {id: (.mailbox + "/" + (.uid|tostring))}' \
```

### incremental scan:

```bash
fload imap --imap-server=xxx --imap-port=xxx --imap-user=user --imap-pass=PassW0Rd --start-uid-file=mailbox_uid.txt \
| jq -ca '. + {id: (.mailbox + "/" + (.uid|tostring))}' \
| fload last_field_to_field --field=uid --dest-file=mailbox_uid.txt
```
