#!/usr/bin/env python

import logging
from openadr.www import *

sub_title = 'View Node'

print "Content-type: text/html"
print
print "<html>"
print "<head>"
print "<title>%s</title>" % get_title(sub_title)
print "</head>"
print "<body>"
print get_header(sub_title, page=PAGE.node, action=ACTION.view)
print "body goes here!!!"
print "</body>"
print "</html>"


