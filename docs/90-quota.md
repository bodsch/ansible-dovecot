# 90-quota.conf


```yaml
dovecot_defaults_quota:
  plugins: []
  #   - limits:
  #       quota_rule: "*:storage=1G"
  #       quota_rule2: "Trash:storage=+100M"
  #
  #       # LDA/LMTP allows saving the last mail to bring user from under quota to
  #       # over quota, if the quota doesn't grow too high. Default is to allow as
  #       # long as quota will stay under 10% above the limit. Also allowed e.g. 10M.
  #       #quota_grace: 10%%
  #
  #       # Quota plugin can also limit the maximum accepted mail size.
  #       #quota_max_mail_size: 100M
  #   - warnings:
  #       #quota_warning: storage=95%% quota-warning 95 %u
  #       #quota_warning2: storage=80%% quota-warning 80 %u
  #   - backends:
  #       #quota: dirsize:User quota
  #       #quota: maildir:User quota
  #       #quota: dict:User quota::proxy::quota
  #       #quota: fs:User quota
  #service quota-warning {
  #  executable: script /usr/local/bin/quota-warning.sh
  #  user: dovecot
  #  unix_listener quota-warning {
  #    user: vmail
  #  }
  #}
  # services:
  #   - quota-warning:
  #       executable: script /usr/local/bin/quota-warning.sh
  #       user: dovecot
  #       listeners:
  #         - quota-warning:
  #             type: unix
  #             user: vmail
```

