# ansible

Mijn Ansible playbooks.
Voor (zelf)studie, werk in uitvoering.

## Basic test

Test of ansible werkt op localhost:

`ansible localhost -a 'echo Hello World!'`

Output:

```console
localhost | CHANGED | rc=0 >>
Hello World!
```

Inhoud playbook hello-world.yml:

```yml
- hosts: all
  tasks:
  - name: Hello World!
    debug:
      msg: "Hello World!"
```

Inhoud inventory/localhost:

```yml
nodes:
  hosts: 
    localhost

  vars: 
    ansible_python_interpreter: /usr/bin/python3
```

Dezelfde test met uitvoeren playbook hello-world.yml:

`ansible-playbook -i inventory/localhost hello-world.yml`

Output:

```console
PLAY [all] *******************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************
ok: [localhost]

TASK [Hello World!] **********************************************************************************************
ok: [localhost] => {
    "msg": "Hello World!"
}

PLAY RECAP *******************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Ansible Fundamentals Case

Maak een kleine PHP-applicatie die verbinding maakt met een database.

```bash
~/ansible$ ansible site.yml -i inventory/dev
~/ansible$ ansible site.yml -i inventory/test
~/ansible$ ansible site.yml -i inventory/production
```

### Inventarisatie

1. PHP
2. Apache2
3. Library
4. Config aanpassen -> docRoot
5. Enable php7.4 (8)
6. Herstart service
7. Git clone (eerst downloaden en overzetten)
8. MySQL
9. Script uitvoeren, data.sql en database
10. App config

### Roles

#### Installatie

* apache
* php
* mysql

#### Config

* doc root aanpassen
* Handler: restart apache

#### Applicatie

* applicatie downloaden naar goeie map
* config.ini vanuit template!!!!
* database maken
* data importeren
