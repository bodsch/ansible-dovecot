# auth-deny.ext.conf


```yaml
dovecot_defaults_authentications:
  - deny:
      passdb:
        driver: passwd-file
        deny: true
        args: /etc/dovecot/deny-users
```

