# auth-static.ext.conf


```yaml
dovecot_defaults_authentications:
  - static:
      passdb: {}
      #   driver: static
      #   # args: proxy=y host=%1Mu.example.com nopassword=y
      userdb: {}
      #   driver: static
      #   # args: uid=vmail gid=vmail home=/home/%u
```

