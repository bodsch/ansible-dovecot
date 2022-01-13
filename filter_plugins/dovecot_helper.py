# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.utils.display import Display

import json
# from ruamel.yaml import YAML
# import itertools

display = Display()


class FilterModule(object):
    """
      ansible filter
    """

    def filters(self):
        return {
            'config_value': self.config_value,
        }

    def config_value(self, data, default=None):
        """
        """
        display.v("config_value({}, {})".format(data, default))

        result = None
        display.v("  - {} {}".format(data, type(data)))

        if type(data) == None:
            result = False
        elif type(data) == bool:
            result = 'yes' if data == True else 'no'
        else:
            result = data

        display.v("return : {}".format(result))
        return result
