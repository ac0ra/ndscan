#!/bin/env python

## IMPORTS ##

from pydblite.pydblite import Base


def setupdb(ndbl = 'ndb.pd1', hdbl = 'hdb.pd1'):
    global ndb
    global hdb
    ndb = Base(ndbl)
    hdb = Base(hdbl)

    ndb.create('NID', 'Range', mode="open")
    hdb.create('UID', 'HID', 'NID', 'ip', 'bridge')
