# -*- coding: utf-8 -*-
'''
    tests
    ~~~~~

    Test suite for vdirsyncer.

    :copyright: (c) 2014 Markus Unterwaditzer & contributors
    :license: MIT, see LICENSE for more details.
'''

from vdirsyncer.utils.compat import text_type
from vdirsyncer.utils.vobject import normalize_item as _normalize_item


def blow_up(*a, **kw):
    raise AssertionError('Did not expect to be called.')


def normalize_item(item):
    if not isinstance(item, text_type):
        item = item.raw
    return tuple(sorted(_normalize_item(
        item, use_icalendar=False).splitlines()))


def assert_item_equals(a, b):
    assert normalize_item(a) == normalize_item(b)


VCARD_TEMPLATE = u'''BEGIN:VCARD
VERSION:3.0
FN:Cyrus Daboo
N:Daboo;Cyrus
ADR;TYPE=POSTAL:;2822 Email HQ;Suite 2821;RFCVille;PA;15213;USA
EMAIL;TYPE=PREF:cyrus@example.com
NICKNAME:me
NOTE:Example VCard.
ORG:Self Employed
TEL;TYPE=VOICE:412 605 0499
TEL;TYPE=FAX:412 605 0705
URL:http://www.example.com
X-SOMETHING:{r}
UID:{r}
END:VCARD'''

TASK_TEMPLATE = u'''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//dmfs.org//mimedir.icalendar//EN
BEGIN:VTODO
CREATED:20130721T142233Z
DTSTAMP:20130730T074543Z
LAST-MODIFIED;VALUE=DATE-TIME:20140122T151338Z
SEQUENCE:2
SUMMARY:Book: Kowlani - Tödlicher Staub
X-SOMETHING:{r}
UID:{r}
END:VTODO
END:VCALENDAR'''


BARE_EVENT_TEMPLATE = u'''BEGIN:VEVENT
DTSTART:19970714T170000Z
DTEND:19970715T035959Z
SUMMARY:Bastille Day Party
X-SOMETHING:{r}
UID:{r}
END:VEVENT'''


EVENT_TEMPLATE = u'''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
''' + BARE_EVENT_TEMPLATE + u'''
END:VCALENDAR'''


SIMPLE_TEMPLATE = u'''BEGIN:FOO
UID:{r}
X-SOMETHING:{r}
HAHA:YES
END:FOO'''
