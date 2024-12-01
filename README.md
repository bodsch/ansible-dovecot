
# Ansible Role:  `dovecot`

Ansible role to install and configure dovecot on various linux systems.

---

> I am in the process of transferring this role to a [collection](https://github.com/bodsch/ansible-collection-mail) and will therefore no longer process any issues or merge requests here.  
> However, I will include them in the collection!  
> **Please be patient until I have completed the work!**

---

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-dovecot/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-dovecot)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-dovecot)][releases]
[![Ansible Downloads](https://img.shields.io/ansible/role/d/bodsch/dovecot?logo=ansible)][galaxy]

[ci]: https://github.com/bodsch/ansible-dovecot/actions
[issues]: https://github.com/bodsch/ansible-dovecot/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-dovecot/releases
[galaxy]: https://galaxy.ansible.com/ui/standalone/roles/bodsch/dovecot/


## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)

```bash
ansible-galaxy collection install bodsch.core
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

### Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 11 / 12
    - Ubuntu 20.04 / 22.04

> **RedHat-based systems are no longer officially supported! May work, but does not have to.**

## configuration

- [/etc/dovecot/conf.d/10-auth.conf](docs/10-auth.md)
- [/etc/dovecot/conf.d/10-director.conf](docs/10-director.md)
- [/etc/dovecot/conf.d/10-logging.conf](docs/10-logging.md)
- [/etc/dovecot/conf.d/10-mail.conf](docs/10-mail.md)
- [/etc/dovecot/conf.d/10-master.conf](docs/10-master.md)
- [/etc/dovecot/conf.d/10-ssl.conf](docs/10-ssl.md)
- [/etc/dovecot/conf.d/10-tcpwrapper.conf](docs/10-tcpwrapper.md)
- [/etc/dovecot/conf.d/15-lda.conf](docs/15-lda.md)
- [/etc/dovecot/conf.d/15-mailboxes.conf](docs/15-mailboxes.md)
- [/etc/dovecot/conf.d/20-imap.conf](docs/20-imap.md)
- [/etc/dovecot/conf.d/20-lmtp.conf](docs/20-lmtp.md)
- [/etc/dovecot/conf.d/20-managesieve.conf](docs/20-managesieve.md)
- [/etc/dovecot/conf.d/20-pop3.conf](docs/20-pop3.md)
- [/etc/dovecot/conf.d/20-submission.conf](docs/20-submission.md)
- [/etc/dovecot/conf.d/90-acl.conf](docs/90-acl.md)
- [/etc/dovecot/conf.d/90-plugin.conf](docs/90-plugin.md)
- [/etc/dovecot/conf.d/90-quota.conf](docs/90-quota.md)
- [/etc/dovecot/conf.d/90-sieve.conf](docs/90-sieve.md)
- [/etc/dovecot/conf.d/90-sieve-extprograms.conf](docs/90-sieve-extprograms.md)

- [/etc/dovecot/conf.d/auth-checkpassword.conf.ext](docs/auth-checkpassword.ext.md)
- [/etc/dovecot/conf.d/auth-deny.conf.ext](docs/auth-deny.ext.md)
- [/etc/dovecot/conf.d/auth-dict.conf.ext](docs/auth-dict.ext.md)
- [/etc/dovecot/conf.d/auth-ldap.conf.ext](docs/auth-ldap.ext.md)
- [/etc/dovecot/conf.d/auth-master.conf.ext](docs/auth-master.ext.md)
- [/etc/dovecot/conf.d/auth-passwdfile.conf.ext](docs/auth-passwdfile.ext.md)
- [/etc/dovecot/conf.d/auth-sql.conf.ext](docs/auth-sql.ext.md)
- [/etc/dovecot/conf.d/auth-static.conf.ext](docs/auth-static.ext.md)
- [/etc/dovecot/conf.d/auth-system.conf.ext](docs/auth-system.ext.md)
- [/etc/dovecot/conf.d/auth-vpopmail.conf.ext](docs/auth-vpopmail.ext.md)

- [/etc/dovecot/dovecot-dict-auth.conf.ext](docs/dovecot-dict-auth.md)
- [/etc/dovecot/dovecot-dict-sql.conf.ext](docs/dovecot-dict-sql.md)
- [/etc/dovecot/dovecot-ldap.conf.ext](docs/dovecot-ldap.conf.md)
- [/etc/dovecot/dovecot-sql.conf.ext](docs/dovecot-sql.conf.md)


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-dovecot/tags)!


## Author

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
