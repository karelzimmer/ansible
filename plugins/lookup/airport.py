from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.urls import open_url
import json

# Copyright (C) 2020 Jan-Piet Mens <jp@mens.de>

DOCUMENTATION = """
    lookup: airport
    author: Jan-Piet Mens (@jpmens)
    version_added: "2.10"
    short_description: Queries IATA airports from airportsd
    description:
        - Queries the airportsd server for a case-insensitive, 3-letter
          IATA code and returns the JSON, enriched with an element "osm"
          containing a URL to OpenStreetMap at that location.
    options:
        _terms:
            description:
                - The IATA codes to query
            type: list
            elements: string
            required: True
"""

EXAMPLES = """
    - debug: msg="{{ lookup('airport','bcn') }}"
"""

RETURN = """
    _raw:
        description: JSON response from query
"""


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):
        ret = []
        print("hello there!") #TODO where does this text appear?

        #TODO: once the plugin works for you, can you figure out how
        #      to pass more than one term on invocation? How does the
        #      result change?
        for term in terms:
            # http://127.0.0.1:8812/lookup?iata=bcn
            url = "http://127.0.0.1:8812/lookup?iata={0}".format(term)
            # ............TODO: ^^
            try:
                response = open_url(url)
            except Exception as e:
                raise AnsibleError("Received HTTP error for %s : %s" % (term, e))

            data = json.loads(response.read())

            #TODO: what happens if you add your name to the data?
            data["myname"] = "Karel"

            ret.append(data)

        return ret
