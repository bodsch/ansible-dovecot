# dovecot-ldap.conf.ext

```yaml
dovecot_defaults_sql: {}
  # # Database driver: mysql, pgsql, sqlite
  # driver: ""
  #
  # #  connect = host=192.168.1.1 dbname=users
  # #  connect = host=sql.example.com dbname=virtual user=virtual password=blarg
  # #  connect = /etc/dovecot/authdb.sqlite
  # connect: ""
  # default_pass_scheme: MD5
  # password_query: >
  #   SELECT username, domain, password
  #   FROM users WHERE username: '%n' AND domain: '%d'
  # user_query: >
  #   SELECT home, uid, gid
  #   FROM users WHERE username: '%n' AND domain: '%d'
  # iterate_query: SELECT username AS user FROM users
```
