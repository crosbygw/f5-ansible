#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import os
import sys

TASKS_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, TASKS_DIR)

from ansible.plugins.loader import PluginLoader
from tasks.lib.common import BASE_DIR


def get_fragment_loader():
    fragment_loader = PluginLoader(
        'ModuleDocFragment',  # class_name
        '',  # package
        '{0}/library/plugins/doc_fragments'.format(BASE_DIR),  # config
        '',  # subdir
    )
    return fragment_loader
