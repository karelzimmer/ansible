<!---
# SPDX-FileCopyrightText: Karel Zimmer <info@karelzimmer.nl>
# SPDX-License-Identifier: CC0-1.0
--->

# ansible

My Ansible Playbooks.

For (self) study. Work in progress.

## Basic test

Test if Ansible works on localhost:

```sh
ansible localhost -a 'echo Hello World!'
```

Output:

```console
localhost | CHANGED | rc=0 >>
Hello World!
```

Run the same test with playbook hello-world.yml:

```sh
cd ~/ansible
ansible-playbook -i inventory/localhost hello-world.yml
```

Output:

```console
PLAY [all] *************************************************************************

TASK [Gathering Facts] *************************************************************
ok: [localhost]

TASK [Hello World!] ****************************************************************
ok: [localhost] => {
    "msg": "Hello World!"
}

PLAY RECAP *************************************************************************
localhost: ok=2  changed=0  unreachable=0  failed=0  skipped=0  rescued=0  ignored=0
```

Content playbook ~/ansible/hello-world.yml:

```yml
- hosts: all
  tasks:
  - name: Hello World!
    debug:
      msg: "Hello World!"
```

Inhoud ~/ansible/inventory/localhost:

```yml
nodes:
  hosts: 
    localhost

  vars: 
    ansible_python_interpreter: /usr/bin/python3
```
