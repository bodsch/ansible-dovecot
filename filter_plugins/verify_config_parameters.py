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
            'compare_list': self.compare_list,
            'compare_dict': self.compare_dict,
        }

    def compare_list(self, data_list, compare_to_list):
        """
        """
        display.v("compare_list({}, {})".format(data_list, compare_to_list))

        result = list(
            set(
                sorted(data_list)).intersection(sorted(compare_to_list)
            )
        )

        display.v("return : {}".format(result))
        return sorted(result)

    def compare_dict(self, left_dict, right_dict):
        """
        """
        result = {}

        if(isinstance(left_dict, list)):
            _dict = {}

            for e in left_dict:
                name = e.get('name')
                image = e.get('image')

                registry      = image.split('/')[0]
                container     = image.split('/')[1].split(':')[0]
                container_tag = image.split(':')[1]

                _dict[name] = {
                    "container": container,
                    "registry": registry,
                    "tag": container_tag,
                    "created": "None",
                }

            left_dict = _dict

        for k in left_dict:
            l_dict = left_dict[k]
            r_dict = right_dict[k]
            _ = l_dict.pop('created')
            _ = r_dict.pop('created')

            if (k not in right_dict):
                result[k] = l_dict
            else:
                left  = json.dumps(l_dict, sort_keys=True)
                right = json.dumps(r_dict, sort_keys=True)

                if(left != right):
                    result[k] = l_dict

        # display.v("return : {}".format(result))
        return result
