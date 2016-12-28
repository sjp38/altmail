altmail
=======

Find alternative mail address(es) for a user or members of a mailing list
group.

In case of mail server crash, finding alternative mail addresses of members in
manual is exhausting.  `altmail` automatically finds out such alternative mail
addresses.  It uses `/etc/aliases` and `.forward` file under home directories
to find out the addresses.


Usage
=====

```
$ altmail.py <user name or mailing list name>
```

For example,

```
$ altmail.py alice
alice@gmail.com
$
$ altmail.py members
alice@gmail.com
chatshire@gmail.com
david@yahoo.com
$
```


License
=======

GPL v3


Author
======

SeongJae Park (sj38.park@gmail.com)
