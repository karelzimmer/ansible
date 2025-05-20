# Ansible Fundamentals Case

## Ansible Fundamentals Case (Dutch)

Maak een kleine PHP-applicatie die verbinding maakt met een database.

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

```sh
cd ~/ansible
ansible site.yml -i inventory/dev
ansible site.yml -i inventory/test
ansible site.yml -i inventory/production
```
