# coding=utf-8
import re
import urllib2
import warnings
from lxml import etree

# we know we may get a warning about not having the C version of
# NameMapper on importing or using Cheetah, so let's hide it; we don't
# really care about the speed that much
warnings.simplefilter('ignore')

from Cheetah.Template import Template

__author__ = 'jason'

ephesians_414_xslt = """<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <title>
                    Bible Reader: <xsl:value-of select="bible/range/result"/>
                </title>
                <style>
                    body {
                        width: 35em;
                        margin: 0px auto;
                        text-align: justify;
                        font-family: the_font; sans;
                    }
                    b.verse {
                        font-family: serif;
                        font-weight: light;
                        vertical-align: super;
                        font-size: 70%;
                        padding-left: 1em;
                    }
                    div.error {
                        size: smaller;
                    }
                </style>
            </head>
            <body>
                <h2>
                    <xsl:value-of select="bible/range/result"/>
                </h2>
                <div class="error">
                    <xsl:value-of select="/bible/error" />
                </div>
                <xsl:for-each select="bible/range/item">
                    <xsl:if test="verse = 1">
                        <h2 class="chapter">
                            <xsl:value-of select="chapter"/>
                        </h2>
                    </xsl:if>
                    <b class="verse">
                        <xsl:value-of select="verse"/>
                    </b>
                    <span class="verse">
                        <xsl:value-of select="text"/>
                    </span>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
"""

class Ephesians414Session(object):
    """Fetcher of formatted texts using the Ephesians 4:14 API"""
    def __init__(self, font, version="kjv"):
        self.base_url = ("http://api.preachingcentral.com/bible.php?" +
                         "passage=%s&version=" + version)
        self.font = font

    def query(self, passage_ref):
        """return formatted HTML for the passage specified by passage_ref"""
        passage = '+'.join(passage_ref.split())
        url = (self.base_url % passage)
        response = urllib2.urlopen(url)
        passage_xml = response.read()
        return self._transform(passage_xml)

    def _transform(self, xml):
        """Use XSLT to transform the XML response to ugly but workable HTML"""
        source = etree.fromstring(xml)
        xslt = etree.fromstring(ephesians_414_xslt)
        transform = etree.XSLT(xslt)
        result = etree.tostring(transform(source))
        # this is ugly, but I don't think the string "the_font" appears in
        # the Bible.
        return result.replace("the_font", self.font)


esv_tmpl = """<html>
<head>
    <title>$passage: ESV</title>
    <style>
        .esv {
            width: 35em;
            margin: 0px auto;
            text-align: justify;
            font-family: "$font";
            sans;
        }

        span.verse-num {
            font-family: serif;
            font-weight: light;
            vertical-align: super;
            font-size: 70%;
        }

        span.chapter-num {
            font-family: serif;
            font-weight: bold;
            vertical-align: super;
            font-size: 90%;
        }

        .footnotes {
            font-size: 70%;
            color: #555555;
        }
    </style>
</head>
<body>
$content
</body>
</html>
"""


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
        tmpl = Template(esv_tmpl,
            searchList={'passage': passage_ref,
                        'content': passage_html,
                        'font': self.font})
        return unicode(tmpl)

    
net_tmpl = """<html>
<head>
    <title>$passage.title()</title>
    <style>
        body {
            width: 35em;
            margin: 0px auto;
            text-align: justify;
            font-family: "$font";
            sans;
        }

        b.verse {
            font-family: serif;
            font-weight: light;
            vertical-align: super;
            font-size: 70%;
        }
    </style>
</head>
<body>
<h2>$passage.title()</h2>
$content
</body>
</html>
"""


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
        # about all the error handling we can do, since if it can extract
        # meaningless numbers, NET returns a passage from Genesis.  To get
        # here, you'd have to enter something like "Beelzebub, yo".  Our
        # target audience is above that, I think.
        if passage_html == "":
            return "<p>Bad reference: %s.</p>" % passage_ref
        passage_html = self.rearrange_html(passage_html)
        tmpl = Template(net_tmpl,
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
