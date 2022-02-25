# auth-vpopmail.ext.conf


```yaml
dovecot_defaults_authentications:
  - vpopmail:
      passdb:
        driver: vpopmail
      userdb:
        driver: vpopmail
        args: quota_template=quota_rule=*:backend=%q
```

