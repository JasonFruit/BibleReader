# coding=utf-8

import re
import urllib2
import warnings
from lxml import etree

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
                        <br />
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

class Bible(object):
    def __init__(self, version, font="Helvetica"):
        self.lookup = Ephesians414Session(font, version)

    def query(self, passage):
        return self.lookup.query(passage)
