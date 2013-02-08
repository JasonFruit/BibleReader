import string

book_order = ["Genesis",
              "Exodus",
              "Leviticus",
              "Numbers",
              "Deuteronomy",
              "Joshua",
              "Judges",
              "Ruth",
              "1 Samuel",
              "2 Samuel",
              "1 Kings",
              "2 Kings",
              "1 Chronicles",
              "2 Chronicles",
              "Ezra",
              "Nehemiah",
              "Esther",
              "Job",
              "Psalms",
              "Proverbs",
              "Ecclesiastes",
              "Song of Solomon",
              "Isaiah",
              "Jeremiah",
              "Lamentations",
              "Ezekiel",
              "Daniel",
              "Hosea",
              "Joel",
              "Amos",
              "Obadiah",
              "Jonah",
              "Micah",
              "Nahum",
              "Habakkuk",
              "Zephaniah",
              "Haggai",
              "Zechariah",
              "Malachi",
              "Matthew",
              "Mark",
              "Luke",
              "John",
              "Acts",
              "Romans",
              "1 Corinthians",
              "2 Corinthians",
              "Galatians",
              "Ephesians",
              "Philippians",
              "Colossians",
              "1 Thessalonians",
              "2 Thessalonians",
              "1 Timothy",
              "2 Timothy",
              "Titus",
              "Philemon",
              "Hebrews",
              "James",
              "1 Peter",
              "2 Peter",
              "1 John",
              "2 John",
              "3 John",
              "Jude",
              "Revelation"]

books = {'Judges': [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25],
         'Micah': [16, 13, 12, 13, 15, 16, 20],
         'Proverbs': [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31],
         'Revelation': [20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21],
         'Deuteronomy': [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12],
         'Haggai': [15, 23],
         '3 John': [15],
         '1 Kings': [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53],
         'Mark': [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20],
         'Matthew': [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20],
         '1 Thessalonians': [10, 20, 13, 18, 28],
         'Daniel': [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13],
         'Malachi': [14, 17, 18, 6],
         'Colossians': [29, 23, 25, 18],
         'Ruth': [22, 23, 18, 22],
         'Genesis': [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26],
         '2 Samuel': [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25],
         'Obadiah': [21],
         'Esther': [22, 23, 15, 17, 14, 14, 10, 17, 32, 3],
         'Exodus': [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38],
         'Jeremiah': [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34],
         'Ephesians': [23, 22, 21, 32, 33, 24],
         'Habakkuk': [17, 20, 19],
         'Luke': [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53],
         'Song of Solomon': [17, 17, 11, 16, 16, 13, 13, 14],
         'Jonah': [17, 10, 10, 11],
         'Acts': [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31],
         'Job': [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17],
         'Titus': [16, 15, 15],
         '2 Timothy': [18, 26, 17, 22],
         'James': [27, 26, 18, 17, 20],
         '2 John': [13],
         'Isaiah': [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24],
         '2 Thessalonians': [12, 17, 18],
         '1 Chronicles': [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31, 32, 34, 21, 30],
         '1 Timothy': [20, 15, 16, 16, 25, 21],
         'Leviticus': [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34],
         '1 Peter': [25, 25, 22, 19, 14],
         'Psalms': [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6],
         'Zephaniah': [18, 15, 20],
         'Joel': [20, 32, 21],
         'Nahum': [15, 13, 19],
         'Jude': [25],
         '2 Chronicles': [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23],
         'Hosea': [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9],
         'Zechariah': [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21],
         'Nehemiah': [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31],
         'John': [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25],
         '1 John': [10, 29, 24, 21, 21],
         'Lamentations': [22, 22, 66, 22, 22],
         'Amos': [15, 16, 15, 13, 27, 14, 17, 14, 15],
         '1 Samuel': [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44, 25, 12, 25, 11, 31, 13],
         'Joshua': [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33],
         '1 Corinthians': [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24],
         'Ezra': [11, 70, 13, 24, 17, 22, 28, 36, 15, 44],
         'Romans': [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27],
         '2 Corinthians': [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14],
         'Hebrews': [14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25],
         'Ezekiel': [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35],
         '2 Peter': [21, 22, 18],
         'Philippians': [30, 30, 21, 23],
         'Numbers': [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13],
         'Philemon': [25],
         'Galatians': [24, 21, 29, 31, 26, 18],
         '2 Kings': [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30],
         'Ecclesiastes': [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]}

abbrevs = {'rom': 'Romans',
           'ge': 'Genesis',
           'ga': 'Galatians',
           'gn': 'Genesis',
           'i thes': '1 Thessalonians',
           'iith': '2 Thessalonians',
           'iiti': '2 Timothy',
           'iitm': '2 Timothy',
           '2chronicles': '2 Chronicles',
           'ti': 'Titus',
           'iij': '2 John',
           'esther': 'Esther',
           'song': 'Song of Solomon',
           'ii co': '2 Corinthians',
           'ii tim': '2 Timothy',
           'ii ch': '2 Chronicles',
           '1pe': '1 Peter',
           '2 corinthians': '2 Corinthians',
           'genesis': 'Genesis',
           'isaiah': 'Isaiah',
           'ii corinthians': '2 Corinthians',
           '1pt': '1 Peter',
           '1thes': '1 Thessalonians',
           '1 chronicles': '1 Chronicles',
           '2samuel': '2 Samuel',
           'joel': 'Joel',
           'i kings': '1 Kings',
           'ezra': 'Ezra',
           'judg': 'Judges',
           'iiijn': '3 John',
           'iiijo': '3 John',
           'jude': 'Jude',
           '2chron': '2 Chronicles',
           'iitimothy': '2 Timothy',
           '1 pe': '1 Peter',
           'neh': 'Nehemiah',
           '3j': '3 John',
           '1 thessalonians': '1 Thessalonians',
           '1 kg': '1 Kings',
           '1 ki': '1 Kings',
           'ithessalonians': '1 Thessalonians',
           'jonah': 'Jonah',
           '2kg': '2 Kings',
           'lev': 'Leviticus',
           '2ki': '2 Kings',
           '1 timothy': '1 Timothy',
           'micah': 'Micah',
           'iikings': '2 Kings',
           'psalms': 'Psalms',
           'ii sam': '2 Samuel',
           'joshua': 'Joshua',
           '1sa': '1 Samuel',
           '2 pt': '2 Peter',
           'ipe': '1 Peter',
           '1sm': '1 Samuel',
           '2 timothy': '2 Timothy',
           'ipt': '1 Peter',
           '2 pe': '2 Peter',
           '2thes': '2 Thessalonians',
           'iipt': '2 Peter',
           'revelation': 'Revelation',
           'iipe': '2 Peter',
           'colossians': 'Colossians',
           'isam': '1 Samuel',
           'iip': '2 Peter',
           '2king': '2 Kings',
           '2kg': '2 Kings',
           'iic': '2 Corinthians',
           '1tm': '1 Timothy',
           '1th': '1 Thessalonians',
           '1ti': '1 Timothy',
           'ii sm': '2 Samuel',
           'ml': 'Malachi',
           'jdg': 'Judges',
           'song of sol': 'Song of Solomon',
           'mi': 'Micah',
           'deu': 'Deuteronomy',
           'mk': 'Mark',
           'mt': 'Matthew',
           '1 john': '1 John',
           '1 samuel': '1 Samuel',
           '1jn': '1 John',
           '1jo': '1 John',
           'ithes': '1 Thessalonians',
           '2 chron': '2 Chronicles',
           '1corinthians': '1 Corinthians',
           'ithess': '1 Thessalonians',
           'numbers': 'Numbers',
           'ecclesiastes': 'Ecclesiastes',
           'acts': 'Acts',
           'acts of the apostles': 'Acts',
           'iiij': '3 John',
           '1 cor': '1 Corinthians',
           'hos': 'Hosea',
           'lam': 'Lamentations',
           'mar': 'Mark',
           'mat': 'Matthew',
           'iisamuel': '2 Samuel',
           '1 peter': '1 Peter',
           'mal': 'Malachi',
           'ss': 'Song of Solomon',
           '2 tim': '2 Timothy',
           'so': 'Song of Solomon',
           'sg': 'Song of Solomon',
           'zec': 'Zechariah',
           '1 corinthians': '1 Corinthians',
           'itm': '1 Timothy',
           'ith': '1 Thessalonians',
           'iti': '1 Timothy',
           '2sa': '2 Samuel',
           'zep': 'Zephaniah',
           'daniel': 'Daniel',
           'jnh': 'Jonah',
           'ichron': '1 Chronicles',
           'iitim': '2 Timothy',
           'la': 'Lamentations',
           'lk': 'Luke',
           'lv': 'Leviticus',
           'lu': 'Luke',
           '1 sam': '1 Samuel',
           'dan': 'Daniel',
           '1 thess': '1 Thessalonians',
           'ii ki': '2 Kings',
           'exod': 'Exodus',
           '2p': '2 Peter',
           'james': 'James',
           'nehemiah': 'Nehemiah',
           '2c': '2 Corinthians',
           '2j': '2 John',
           '2 samuel': '2 Samuel',
           '1 ch': '1 Chronicles',
           '1 co': '1 Corinthians',
           'obadiah': 'Obadiah',
           'iiijohn': '3 John',
           'phi': 'Philippians',
           'ec': 'Ecclesiastes',
           'i th': '1 Thessalonians',
           'exodus': 'Exodus',
           'ex': 'Exodus',
           'ez': 'Ezekiel',
           'ep': 'Ephesians',
           'es': 'Esther',
           'ru': 'Ruth',
           'rv': 'Revelation',
           '2 thes': '2 Thessalonians',
           'phm': 'Philemon',
           'rev': 'Revelation',
           're': 'Revelation',
           '2 jn': '2 John',
           '2 jo': '2 John',
           'rm': 'Romans',
           'ro': 'Romans',
           'ecc': 'Ecclesiastes',
           'jeremiah': 'Jeremiah',
           '1john': '1 John',
           'romans': 'Romans',
           '2 kings': '2 Kings',
           'i cor': '1 Corinthians',
           'ii chron': '2 Chronicles',
           'zech': 'Zechariah',
           '2 tm': '2 Timothy',
           '2 th': '2 Thessalonians',
           '2 ti': '2 Timothy',
           'i samuel': '1 Samuel',
           'ism': '1 Samuel',
           'isa': '1 Samuel',
           'i john': '1 John',
           'iichronicles': '2 Chronicles',
           'jer': 'Jeremiah',
           '1p': '1 Peter',
           'iii john': '3 John',
           '1c': '1 Corinthians',
           'ii kings': '2 Kings',
           '1j': '1 John',
           'i sam': '1 Samuel',
           'iich': '2 Chronicles',
           'iico': '2 Corinthians',
           'john': 'John',
           'icorinthians': '1 Corinthians',
           '2 co': '2 Corinthians',
           '2 ch': '2 Chronicles',
           '1 jo': '1 John',
           '1 jn': '1 John',
           'psalm': 'Psalms',
           'iithes': '2 Thessalonians',
           'i ch': '1 Chronicles',
           '1tim': '1 Timothy',
           'iijn': '2 John',
           'iijo': '2 John',
           '1thessalonians': '1 Thessalonians',
           'pro': 'Proverbs',
           'jerem': 'Jeremiah',
           'ii cor': '2 Corinthians',
           'prv': 'Proverbs',
           '1pet': '1 Peter',
           'i pet': '1 Peter',
           'mic': 'Micah',
           '2corinthians': '2 Corinthians',
           'deut': 'Deuteronomy',
           'lamen': 'Lamentations',
           'icor': '1 Corinthians',
           '2tm': '2 Timothy',
           '2ti': '2 Timothy',
           '2th': '2 Thessalonians',
           'philem': 'Philemon',
           '2cor': '2 Corinthians',
           'exo': 'Exodus',
           'phil': 'Philippians',
           '3 john': '3 John',
           '2sm': '2 Samuel',
           '1 pt': '1 Peter',
           '2 thess': '2 Thessalonians',
           'philippians': 'Philippians',
           'philemon': 'Philemon',
           '1thess': '1 Thessalonians',
           'zeph': 'Zephaniah',
           'judges': 'Judges',
           'jas': 'James',
           'i thess': '1 Thessalonians',
           'jam': 'James',
           'ii sa': '2 Samuel',
           'ijohn': '1 John',
           'dn': 'Daniel',
           'luke': 'Luke',
           'de': 'Deuteronomy',
           'da': 'Daniel',
           '1samuel': '1 Samuel',
           'dt': 'Deuteronomy',
           'du': 'Deuteronomy',
           'gen': 'Genesis',
           '1king': '1 Kings',
           '3 jo': '3 John',
           '3 jn': '3 John',
           'titus': 'Titus',
           'i peter': '1 Peter',
           'hosea': 'Hosea',
           'ii timothy': '2 Timothy',
           'iichron': '2 Chronicles',
           'i timothy': '1 Timothy',
           'ipet': '1 Peter',
           '2 chronicles': '2 Chronicles',
           'num': 'Numbers',
           'eccles': 'Ecclesiastes',
           'iithessalonians': '2 Thessalonians',
           'zechariah': 'Zechariah',
           '3jn': '3 John',
           '3jo': '3 John',
           '2timothy': '2 Timothy',
           'luk': 'Luke',
           'i pe': '1 Peter',
           'jos': 'Joshua',
           '2pt': '2 Peter',
           '2thessalonians': '2 Thessalonians',
           'ju': 'Jude',
           'i chron': '1 Chronicles',
           'jl': 'Joel',
           'jn': 'John',
           'i pt': '1 Peter',
           '2pe': '2 Peter',
           'joe': 'Joel',
           'joh': 'John',
           'je': 'Jeremiah',
           'iki': '1 Kings',
           'ii peter': '2 Peter',
           'ja': 'James',
           'jb': 'Job',
           'i corinthians': '1 Corinthians',
           'job': 'Job',
           'i co': '1 Corinthians',
           'jo': 'John',
           'ikg': '1 Kings',
           'col': 'Colossians',
           'co': 'Colossians',
           'song of solomon': 'Song of Solomon',
           'ii chronicles': '2 Chronicles',
           'ps': 'Psalms',
           'pv': 'Proverbs',
           '1sam': '1 Samuel',
           'mark': 'Mark',
           '1timothy': '1 Timothy',
           '2 cor': '2 Corinthians',
           'iikg': '2 Kings',
           'jon': 'Jonah',
           'iiki': '2 Kings',
           '2pet': '2 Peter',
           'i ki': '1 Kings',
           '2tim': '2 Timothy',
           'esth': 'Esther',
           'i kg': '1 Kings',
           'gal': 'Galatians',
           'leviticus': 'Leviticus',
           '2 peter': '2 Peter',
           '2 ki': '2 Kings',
           'ii thess': '2 Thessalonians',
           'ii thes': '2 Thessalonians',
           'iicor': '2 Corinthians',
           '2 pet': '2 Peter',
           'ip': '1 Peter',
           'is': 'Isaiah',
           'iithess': '2 Thessalonians',
           'ij': '1 John',
           'ic': '1 Corinthians',
           'isamuel': '1 Samuel',
           '2 thessalonians': '2 Thessalonians',
           'iisam': '2 Samuel',
           'i chronicles': '1 Chronicles',
           'matthew': 'Matthew',
           '3john': '3 John',
           'ruth': 'Ruth',
           'i ti': '1 Timothy',
           '2sam': '2 Samuel',
           'i tm': '1 Timothy',
           'ephesians': 'Ephesians',
           'habakkuk': 'Habakkuk',
           'galatians': 'Galatians',
           '1chron': '1 Chronicles',
           '1 thes': '1 Thessalonians',
           'php': 'Philippians',
           'ii thessalonians': '2 Thessalonians',
           '2kings': '2 Kings',
           'zephaniah': 'Zephaniah',
           '1 ti': '1 Timothy',
           '1 th': '1 Thessalonians',
           '1 tm': '1 Timothy',
           'eph': 'Ephesians',
           '1ch': '1 Chronicles',
           '1co': '1 Corinthians',
           '1kings': '1 Kings',
           'nahum': 'Nahum',
           'ikings': '1 Kings',
           '2jo': '2 John',
           '2jn': '2 John',
           '2 sam': '2 Samuel',
           'ezek': 'Ezekiel',
           'iijohn': '2 John',
           'hab': 'Habakkuk',
           'josh': 'Joshua',
           'hag': 'Haggai',
           'ichronicles': '1 Chronicles',
           'nehem': 'Nehemiah',
           'amo': 'Amos',
           'psa': 'Psalms',
           'pss': 'Psalms',
           'i thessalonians': '1 Thessalonians',
           'ii samuel': '2 Samuel',
           'ii john': '2 John',
           'amos': 'Amos',
           'i sa': '1 Samuel',
           'hebrews': 'Hebrews',
           'ezr': 'Ezra',
           'i sm': '1 Samuel',
           'revel': 'Revelation',
           'ezk': 'Ezekiel',
           'eze': 'Ezekiel',
           'iiking': '2 Kings',
           'ijn': '1 John',
           'ijo': '1 John',
           'est': 'Esther',
           'ico': '1 Corinthians',
           'prov': 'Proverbs',
           '1 kings': '1 Kings',
           '2thess': '2 Thessalonians',
           'itimothy': '1 Timothy',
           'i tim': '1 Timothy',
           'jgs': 'Judges',
           '2john': '2 John',
           'haggai': 'Haggai',
           '1 tim': '1 Timothy',
           'iicorinthians': '2 Corinthians',
           '1 sm': '1 Samuel',
           '1 sa': '1 Samuel',
           'rut': 'Ruth',
           'ii pt': '2 Peter',
           'ob': 'Obadiah',
           'oba': 'Obadiah',
           'le': 'Leviticus',
           '2co': '2 Corinthians',
           '2ch': '2 Chronicles',
           'ii pe': '2 Peter',
           'act': 'Acts',
           '1chronicles': '1 Chronicles',
           'deuteronomy': 'Deuteronomy',
           'son': 'Song of Solomon',
           'sos': 'Song of Solomon',
           'iipet': '2 Peter',
           'i jo': '1 John',
           'i jn': '1 John',
           'heb': 'Hebrews',
           'iii jo': '3 John',
           'iii jn': '3 John',
           'jud': 'Jude',
           'iking': '1 Kings',
           'ho': 'Hosea',
           '2 sa': '2 Samuel',
           'hb': 'Habakkuk',
           '2 sm': '2 Samuel',
           'hg': 'Haggai',
           'he': 'Hebrews',
           'proverbs': 'Proverbs',
           'itim': '1 Timothy',
           'iism': '2 Samuel',
           'iisa': '2 Samuel',
           'ac': 'Acts',
           'am': 'Amos',
           'ezekiel': 'Ezekiel',
           '2 john': '2 John',
           'ii jo': '2 John',
           'ii jn': '2 John',
           'obad': 'Obadiah',
           'nm': 'Numbers',
           'tit': 'Titus',
           'na': 'Nahum',
           'nah': 'Nahum',
           '1 pet': '1 Peter',
           'ne': 'Nehemiah',
           'malachi': 'Malachi',
           'nu': 'Numbers',
           '1ki': '1 Kings',
           'ii tm': '2 Timothy',
           '1cor': '1 Corinthians',
           '1kg': '1 Kings',
           'matt': 'Matthew',
           'ii ti': '2 Timothy',
           'ii th': '2 Thessalonians',
           'ich': '1 Chronicles',
           '1 chron': '1 Chronicles',
           'ii pet': '2 Peter',
           'lamentations': 'Lamentations'}


class ReferenceError(Exception):
    """Any error while parsing a range or verse reference"""
    pass

class ReferenceValidator(object):
    def __init__(self):
        pass
    def regularize_verse(self, verse):
        try:
            verse.book = abbrevs[verse.book.lower()]
        except KeyError:
            raise ReferenceError("Unrecognized book: %s" % verse.book)

    def regularize_range(self, rng):
        self.regularize_verse(rng.from_)

        if not rng.from_.verse:
            rng.from_.verse = 1

        if not rng.from_.chapter:
            rng.from_.chapter = 1
            
        self.regularize_verse(rng.to)

        if not rng.to.chapter:
            rng.to.chapter = len(books[rng.to.book])

        if not rng.to.verse:
            rng.to.verse = books[rng.to.book][rng.to.chapter - 1]
        
    def validate_verse(self, verse):
        book = None
        
        try:
            book = abbrevs[verse.book.lower()]
        except KeyError:
            return False

        if verse.chapter:
            if not (0 < verse.chapter <= len(books[book])):
                return False

        if verse.verse:
            if not (0 < verse.verse <= books[book][verse.chapter - 1]):
                return False

        return True

    def validate_range(self, rng):
        math = VerseMath()
        lt = math.lt(rng.from_, rng.to)

        if not lt:
            raise ReferenceError(
                "End of range precedes start of range: %s" % rng)
        
        return (self.validate_verse(rng.from_) and
                self.validate_verse(rng.to) and
                lt)


class VerseMath(object):
    def __init__(self):
        pass
    def next_book(self, book):
        return book_order[book_order.index(book) + 1]
    def previous_book(self, book):
        return book_order[book_order.index(book) - 1]
    def add(self, verse, verses):
        book = verse.book
        chapter = verse.chapter
        remaining = verses + verse.verse

        while remaining > 0:
            remaining = remaining - books[book][chapter - 1]
            if remaining > 0:
                if chapter == len(books[book]):
                    book = self.next_book(book)
                    chapter = 1
                else:
                    chapter += 1

        return Verse(book, chapter, books[book][chapter - 1] + remaining)
    
    def lt(self, verse1, verse2):
        return ((book_order.index(verse1.book) <
                 book_order.index(verse2.book)) or
                ((verse1.book == verse2.book) and
                 (verse1.chapter < verse2.chapter)) or
                ((verse1.book == verse2.book) and
                 (verse1.chapter == verse2.chapter) and
                 (verse1.verse < verse2.verse)))
    def eq(self, verse1, verse2):
        return ((verse1.book == verse2.book) and
                (verse1.chapter == verse2.chapter) and
                (verse1.verse == verse2.verse))
    def gt(self, verse1, verse2):
        return not (self.lt(verse1, verse2) or
                    self.eq(verse1, verse2))


class Verse(object):
    """Represents a verse of the Bible"""
    def __init__(self, book, chapter, verse):
        self.book = book
        self.chapter = chapter
        self.verse = verse
    def __repr__(self):
        if self.verse:
            return "%s %s:%s" % (self.book,
                                 self.chapter,
                                 self.verse)
        elif self.chapter:
            return "%s %s" % (self.book,
                              self.chapter)
        else:
            return self.book

class Range(object):
    """Represents a range of Bible text from one verse to another"""
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def __repr__(self):
        return "%s - %s" % (self.from_, self.to)
    
class VerseParser(object):
    """A parser for Bible verse references"""
    def __init__(self):
        self.validator = ReferenceValidator()
    def is_digit(self):
        try:
            return self.verse[self.index].isdigit()
        except IndexError:
            return False
    def parse(self, verse):
        self.verse = verse.strip()
        self.index = 0

        # skip any leading numeric characters
        while self.is_digit():
            self.index += 1

        # skip up to a number (or the end)
        while not self.is_digit() and self.index < len(self.verse):
            self.index += 1

        # a numeric character after alphabetic ends the book name
        book = self.verse[:self.index].strip()

        # the rest is chapter and verse
        remainder = self.verse[self.index:].strip()

        # initialize to None to indicate that none was specified
        verse, chapter = None, None

        # if there's a :, then it separates chapter and verse
        if ":" in remainder:
            try:
                chapter, verse = map(int,
                                     map(string.strip,
                                         remainder.split(":")))
            except ValueError:
                raise ReferenceError(
                    "Unable to parse verse reference: %s" % self.verse)
        else:
            # otherwise, if there's an integer, it's the chapter #
            try:
                int(remainder)
                chapter = int(remainder.strip())
            except ValueError:
                # and if it's not, there's no chapter or verse
                pass

        out = Verse(book, chapter, verse)
        
        if self.validator.validate_verse(out):
            self.validator.regularize_verse(out)
            return out
        else:
            raise ReferenceError("Invalid verse: %s" % out)

class ReferenceParser(object):
    """A parser for Scripture references (single verse or range)"""
    def __init__(self):
        self.validator = ReferenceValidator()
    def validate(self, output):
        if type(output) == Verse:
            if self.validator.validate_verse(output):
                self.validator.regularize_verse(output)
                return output
            else:
                raise ReferenceError(
                    "Invalid reference: %s" % output)
        else:
            if self.validator.validate_range(output):
                self.validator.regularize_range(output)
                return output
            else:
                raise ReferenceError(
                    "Invalid reference: %s" % output)
                    
    def parse(self, reference):
        # if there's a dash, it's not a verse but a range
        if "-" in reference:
            # split into its component verses
            from_, to = map(string.strip,
                            reference.split("-"))

            # the first is easy; it must be a complete verse/chapter
            # reference
            from_verse = VerseParser().parse(from_)

            # start with an ending verse that duplicates the beginning
            # one, and change it according to what is specified
            to_verse = Verse(from_verse.book,
                             from_verse.chapter,
                             from_verse.verse)

            # if there's a colon, it must specify both chapter and
            # verse, but may also contain a book name
            if ":" in to:
                # split the verse part from the rest
                rest, verse = map(string.strip, to.split(":"))

                # try to make the verse part an int; if it fails, it
                # can't be a valid reference
                try:
                    to_verse.verse = int(verse)
                except ValueError:
                    raise ReferenceError(
                        "Unable to parse reference: %s" % reference)

                # then, try to make the rest an int; if it works, it's
                # a bare chapter; otherwise, `to` is a complete
                # reference and we should parse it using the
                # VerseParser
                try:
                    to_verse.chapter = int(rest)
                except ValueError:
                    to_verse = VerseParser().parse(to)
                return self.validate(Range(from_verse, to_verse))
            
            else:
                # if there's no colon, try the `to` section as an int.
                # If there was a verse in the from-reference, the int
                # is a verse; if a chapter, it's a chapter; if
                # neither, it's got to be a more complete reference
                # --- try to parse it as such
                try:
                    if to_verse.verse:
                        to_verse.verse = int(to.strip())
                    elif to_verse.chapter:
                        to_verse.chapter = int(to.strip())
                    else:
                        to_verse = VerseParser().parse(to)
                    return self.validate(Range(from_verse, to_verse))

                # if you can't make it an int, try to parse `to` as a
                # complete verse reference; if it doesn't work, give up
                except ValueError:
                    try:
                        return self.validate(
                            Range(from_verse,
                                  VerseParser().parse(to)))
                    except:
                        raise ReferenceError(
                            "Unable to parse reference: %s" % reference)
            
        else:
            # it's a simple verse reference
            return self.validate(VerseParser().parse(reference))

if __name__ == "__main__":
    import sys
    rng = ReferenceParser().parse("John 1:1")
    print VerseMath().add(rng, 500)
