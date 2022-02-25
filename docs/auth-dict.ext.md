# auth-dict.ext.conf


```yaml
dovecot_defaults_authentications:
  - dict:
      passdb:
        driver: dict
        args: /etc/dovecot/dovecot-dict-auth.conf.ext
      userdb:
        driver: dict
        args: /etc/dovecot/dovecot-dict-auth.conf.ext
```

