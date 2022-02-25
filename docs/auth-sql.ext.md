# auth-sql.ext.conf


```yaml
dovecot_defaults_authentications:
  - sql:
      passdb:
        driver: sql
        args: /etc/dovecot/dovecot-sql.conf.ext
      userdb:
        driver: sql
        args: /etc/dovecot/dovecot-sql.conf.ext
```

