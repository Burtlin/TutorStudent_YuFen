#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


lst = []
path = raw_input('Input search path:Default={}\n'.format(os.getcwd()))
if len(path) == 0:
    path = os.getcwd()

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(path):
    path = root.split(os.sep)
    for file in files:
        #print(len(path) * '---', file)
        ext = file.split('.')[-1]
        if ext in ['png', 'jpg']:
            if len(file.split('-')) == 2:
                lst.append([os.path.join(root, file), root, os.path.basename(file)])


process_list = []
for f in lst:
    #print unicode(f[0], 'utf-8'), unicode(f[1], 'utf-8')
    filename = unicode(f[2], 'utf-8')
    tokens = filename.split('-')
    subtokens = tokens[1].split(' ')
    activity_name = tokens[0]
    if len(subtokens) < 2:
        print "Invalid filename, skip:", filename
        continue
    tpe = subtokens[0]
    lang = subtokens[1]

    replace_filename = activity_name
    if tpe == u'大廳':
        replace_filename += '_LOBBY'
    elif tpe == u'WEB':
        replace_filename += '_WEB'
    else:
        print "Error filename!", unicode(f[0], 'utf-8')
        sys.exit(1)
    replace_filename+='_{}'.format(lang)

    t0 = f[0]
    t1 = os.path.join(f[1], replace_filename)
    print "Found:", t0 , ", Replace with:", t1
    process_list.append([t0, t1])

x = raw_input('press y to continue, others to abort\n')

if x != 'y':
    sys.exit(0)

for i in process_list:
    os.rename(i[0],i[1])

