# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
      ansible filter
    """

    def filters(self):
        return {
            'type': self.var_type,
            'config_value': self.config_value,
        }

    def var_type(self, var):
        """
          Get the type of a variable
        """
        return type(var).__name__

    def config_value(self, data, default=None):
        """
        """
        # display.v(f"config_value({data}, {default})")

        result = None

        if type(data) is None:
            result = False
        elif type(data) is bool:
            result = 'yes' if data else 'no'
        else:
            result = data

        # display.v(f"return : {result}")
        return result
