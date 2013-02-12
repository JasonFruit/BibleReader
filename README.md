BibleReader
============================================

A Python/Qt interface to several Bible web APIs.  Right now, it can connect to three:

 - [The ESV API](http://esvapi.org)
 - [The NET API](http://labs.bible.org/api_web_service)
 - [The Ephesians 4:14 API](http://www.4-14.org.uk/xml-bible-web-service-api)

More may be added.  An interface to `libsword` using the `diatheke` command-line tool is also planned.

Status
----------------------------------------------------------------

This application is under initial, pre-release development, and
is not really ready for public use.  Though it works fairly well,
and copyright notices and source attributions have been
implemented in accordance with licensing for the various versions,
there are still licensing questions to be answered regarding the
ESV translation; please don't use it until that is resolved.

A Note On Licensing
-----------------------------------------------------------------

The application itself is licensed under the GNU GPLv3; that
doesn't change the terms of use of the various translations and
the APIs by which they are accessed.