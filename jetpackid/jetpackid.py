#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re
import json
import logging


logger = logging.getLogger(__name__)


class JetpackID(object):
    def __init__(self):
        pass


    @staticmethod
    def get_id(manifest_path):
        """
        Parse 'package.json' manifest file, and then return the Add-On/Extension ID.
        :param manifest: The input 'package.json' file path
        :return: the Add-On/Extension ID
        """
        with open(manifest_path) as f:
            manifest = json.load(f)
            if 'id' in manifest and JetpackID.is_valid_id(manifest['id']):
                return manifest['id']
            if 'name' in manifest and JetpackID.is_valid_id('@' + manifest['name']):
                return '@' + manifest['name']
        return None

    @staticmethod
    def is_valid_id(id):
        """
        Return True if the ID is valid for AMO.
        Reference: http://mxr.mozilla.org/mozilla-central/source/toolkit/mozapps/extensions/internal/XPIProvider.jsm#270
        :param id: the input ID
        :return True or False
        """
        pattern = re.compile(r"^(\{[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\}|[a-z0-9-\._]*\@[a-z0-9-\._]+)$", re.IGNORECASE)
        match = re.search(pattern, id)
        if match:
            return True
        return False
