# -*- encoding: utf-8 -*-
'''
:rational: Unless a server is specifically set up to act as a DHCP server, it is
recommended that this service be deleted to reduce the potential attack surface.

:maintainer: HubbleStack
:maturity: 20160216
:depends: SaltStack
:platform: Linux
:compatibility: RedHat

'''
from __future__ import absolute_import
from nova import *
import logging


def __virtual__():
    '''
    Compatibility Check
    '''
    if 'RedHat' in __salt__['grains.get']('os_family'):
        return True
    return False


def audit():
    if not _package('dhcp'):
        return True
    return False
