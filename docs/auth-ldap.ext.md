# auth-ldap.ext.conf


```yaml
dovecot_defaults_authentications:
  - ldap:
      passdb:
        driver: ldap
        args: /etc/dovecot/dovecot-ldap.conf.ext
      userdb:
        driver: ldap
        args: /etc/dovecot/dovecot-ldap.conf.ext
        default_fields: home=/home/virtual/%u
```

