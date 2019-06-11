#!/usr/bin/python

import re
import sys
import os

versions_name = r"versions.mk"
versions_name_tmp = r"versions.mk.tmp"

versionsMK = open(versions_name, "r")
versionsMK_tmp = open(versions_name_tmp, "w")

version_key = ['VERSION_MAIN_B', 'VERSION_SOFT', 'VERSION_DATA', 'VERSION_RELEASED_SOFT_MAIN',
               'VERSION_RELEASED_DATA_MAIN']

for line in versionsMK:
    for key in version_key:
        if (re.match(key, line)):
            line_len = len(line)
            new_id = int(line[line_len - 3: -1]) + 1
            if new_id > 99 or new_id < 10:
                new_id = 10
            line_new = line[0:line_len - 3] + str(new_id) + '\n'
            print(line_new)
            break

        else:
            line_new = line
    #print(line_new)
    versionsMK_tmp.write(line_new)

versionsMK.close()
versionsMK_tmp.close()

os.replace(versions_name_tmp, versions_name)
