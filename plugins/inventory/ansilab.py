#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2012-2025, Ton Kersten - Jan-Piet Mens
#   - Jan-Piet Mens (@jpmens@mastodon.social)
#   - Ton Kersten (@tonk@mastodon.social)
# GNU General Public License v3.0
# see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt
#
DOCUMENTATION = r'''
    name: ansilab
    plugin_type: inventory
    short_description: Constructs an inventory from thin air
    description: Returns Ansible inventory from nothingness
    options:
      plugin:
          description: Name of the plugin
          required: true
          choices: ['ansilab']
      nhosts:
        description: number of hosts to emit
        required: true
'''

from ansible.plugins.inventory import BaseInventoryPlugin

class InventoryModule(BaseInventoryPlugin):

    NAME = "ansilab"

    def parse(self, inventory, loader, path, cache=True):

        # call base method to ensure properties are available for
        # use with other helper methods
        super(InventoryModule, self).parse(inventory, loader, path, cache)

        print("ANSILAB Inventory ", path)      # path contains the name of the config file
        self._read_config_data(path)           # Get configuration
        nhosts = self.get_option('nhosts')     # Get "nhosts" from configuration

        self.inventory.add_group('resolvers')  # Create "resolver" group
        self.inventory.add_group('specials')   # create "specials" group
        for n in range(nhosts):
            # Create host in inventory
            host = "dns{0}".format(n)
            # Add the host to the "resolvers" group
            self.inventory.add_host(host, group='resolvers') #, port=22)
            # Set variable "auth" to "NSD" for this host
            self.inventory.set_variable(host, 'auth', 'NSD')

        # Create host "crate2" in group "specials"
        self.inventory.add_host('crate2', group='specials') #, port=22)
        # Add group variable "soup" with value "veggie" to group "specials"
        self.inventory.set_variable('specials', 'soup', 'veggie')
