#!/usr/bin/env python

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import re

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*')

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

for tag in total_tags:
    sTag = re.sub("^\.", "", tag)
    tag_filename = tag_dir + sTag.lower().replace('.', '-') + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\nexclude_from_search: true\ntagline: \'"Creative Active Individuals can only grow up in a society that emphasizes learning instead of teaching." - Chris Alexander\'\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
