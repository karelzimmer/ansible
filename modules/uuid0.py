from ansible.module_utils.basic import AnsibleModule
import uuid, os

DOCUMENTATION = r'''
---
module: uuid0
short_description: Generate a UUID and store in it in a file
version_added: "1.0.0"
description: Generate a UUID and store it into a file
options:
    path:
        description: The path to the file which will contain the UUID.
        required: true
        type: str
author:
    - you or I
'''

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(type="str", required=True)
        )
    )

    changed = False

    path = module.params["path"]
    try:
        if os.path.exists(path):
            u = open(path).read()
        else:
            u = str(uuid.uuid4())
            changed = True

        if changed:
            with open(path, "w") as f:
                f.write(u + "\n")
    except Exception as e:
        msg = "Oopsie: cannot access {0}: {1}".format(path, e)
        module.fail_json(msg=msg)

    result = dict(changed=changed, uuid=u, myname='Karel Zimmer')

    module.exit_json(**result)

if __name__ == '__main__':
    main()
