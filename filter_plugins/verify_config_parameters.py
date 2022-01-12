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
            'validate_attachment_hash': self.validate_attachment_hash,
        }

    def compare_list(self, data_list, compare_to_list):
        """
        """
        display.v("compare_list({}, {})".format(data_list, compare_to_list))

        result = []

        for i in data_list:
            if i in compare_to_list:
                result.append(i)

        # randomized result :(
        #result = list(
        #    set(
        #        data_list).intersection(sorted(compare_to_list)
        #    )
        #)

        display.v("return : {}".format(result))
        return result

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

    def validate_attachment_hash(self, data, compare_to_list):
        """

        """
        display.v("validate_attachment_hash({}, {})".format(data, compare_to_list))

        if ':' in data:
            for i in compare_to_list:
                if i[:-1] in data:
                    return True
        else:
            if data in compare_to_list:
                return True

        return False
