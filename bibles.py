# coding=utf-8
import re
import urllib2
import warnings
from lxml import etree

# we know we'll get a warning about not having the C version of NameMapper on
# importing or using Cheetah, so let's hide it
warnings.simplefilter('ignore')

from Cheetah.Template import Template

__author__ = 'jason'

class Ephesians414Session(object):
    def __init__(self, font, version="kjv"):
        self.base_url = ("http://api.preachingcentral.com/bible.php?" +
                         "passage=%s&version=" + version)
        self.font = font

    def query(self, passage_ref):
        passage = '+'.join(passage_ref.split())
        url = (self.base_url % passage)
        response = urllib2.urlopen(url)
        passage_xml = response.read()
        return self.transform(passage_xml)

    def transform(self, xml):
        source = etree.fromstring(xml)
        xslt = etree.parse("414.xml")
        transform = etree.XSLT(xslt)
        result = etree.tostring(transform(source))
        # this is ugly.
        return result.replace("the_font", self.font)


class ESVSession(object):
    def __init__(self, font, key='IP', output_format='html'):
        options = ['include-short-copyright=0',
                   'output-format=%s' % output_format,
                   'include-passage-horizontal-lines=0',
                   'include-heading-horizontal-lines=0']
        self.options = '&'.join(options)
        self.base_url = 'http://www.esvapi.org/v2/rest/passageQuery?key=%s' % (key)
        self.font = font

    def query(self, passage_ref):
        passage = '+'.join(passage_ref.split())
        url = (self.base_url +
               '&passage=%s&%s' % (passage, self.options))
        page = urllib2.urlopen(url)
        passage_html = page.read()
        tmpl = Template(file='esv.tmpl',
            searchList={'passage': passage_ref,
                        'content': passage_html,
                        'font': self.font})
        return unicode(tmpl)


class NETSession(object):
    def __init__(self, font):
        self.base_url = 'http://labs.bible.org/api/?passage=%s&formatting=para'
        self.font = font

    def rearrange_html(self, html):
        html = html.replace('“', '"')
        html = html.replace('”', '"')
        html = html.replace("‘", "'")
        html = html.replace("’", "'")
        html = re.sub(
            re.compile(r'(<b>[1234567890:]+</b>)\s*<p class="bodytext">'),
            r'<p class="bodytext">\1 ',
            html)
        html = re.sub(re.compile(r'<b>([1234567890:]+)</b>'),
            r'<b class="verse">\1</b> ',
            html)
        return html

    def query(self, passage_ref):
        passage = '+'.join(passage_ref.split())
        url = self.base_url % passage
        page = urllib2.urlopen(url)
        passage_html = page.read()
        passage_html = self.rearrange_html(passage_html)
        tmpl = Template(file='net.tmpl',
            searchList={'passage': passage_ref,
                        'content': passage_html,
                        'font': self.font})
        return unicode(tmpl)


class Bible(object):
    def __init__(self, version, font="Helvetica"):
        if version == 'esv':
            self.lookup = ESVSession(font=font)
        elif version == 'net':
            self.lookup = NETSession(font=font)
        else:
            self.lookup = Ephesians414Session(font, version)

    def query(self, passage):
        return self.lookup.query(passage)
