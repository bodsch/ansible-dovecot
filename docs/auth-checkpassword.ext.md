# auth-checkpassword.ext.conf


```yaml
dovecot_defaults_authentications:
  - checkpassword:
      passdb:
        driver: checkpassword
        args: /usr/bin/checkpassword
      userdb:
        driver: prefetch
```

