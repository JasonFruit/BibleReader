from datetime import datetime

readings = [['Genesis 1-3', 'Matthew 1'],
            ['Genesis 4-6', 'Matthew 2'],
            ['Genesis 7-9', 'Matthew 3'],
            ['Genesis 10-12', 'Matthew 4'],
            ['Genesis 13-15'],
            ['Genesis 16-17', 'Matthew 5'],
            ['Genesis 18-19', 'Matthew 6'],
            ['Genesis 20-22'],
            ['Genesis 23-24', 'Matthew 7'],
            ['Genesis 25-26'],
            ['Genesis 27-28', 'Matthew 8'],
            ['Genesis 29-30', 'Matthew 9'],
            ['Genesis 31-32'],
            ['Genesis 33-35', 'Matthew 10'],
            ['Genesis 36-38'],
            ['Genesis 39-40', 'Matthew 11'],
            ['Genesis 41-42', 'Matthew 12'],
            ['Genesis 43-45'],
            ['Genesis 46-48'],
            ['Genesis 49-50', 'Matthew 13'],
            ['Exodus 1-3', 'Matthew 14'],
            ['Exodus 4-6'],
            ['Exodus 7-8', 'Matthew 15'],
            ['Exodus 9-11'],
            ['Exodus 12-13', 'Matthew 16'],
            ['Exodus 14-15', 'Matthew 17'],
            ['Exodus 16-18'],
            ['Exodus 19-20', 'Matthew 18'],
            ['Exodus 21-22', 'Matthew 19'],
            ['Exodus 23-24', 'Matthew 20'],
            ['Exodus 25-26'],
            ['Exodus 27-28', 'Matthew 21'],
            ['Exodus 29-30'],
            ['Exodus 31-33'],
            ['Exodus 34-35', 'Matthew 22'],
            ['Exodus 36-38'],
            ['Exodus 39-40', 'Matthew 23'],
            ['Leviticus 1-3'],
            ['Leviticus 4-5', 'Matthew 24'],
            ['Leviticus 6-7', 'Matthew 25'],
            ['Leviticus 8-10'],
            ['Leviticus 11-12'],
            ['Leviticus 13', 'Matthew 26'],
            ['Leviticus 14'],
            ['Leviticus 15-16'],
            ['Leviticus 17-18', 'Matthew 27'],
            ['Leviticus 19-20'],
            ['Leviticus 21-22', 'Matthew 28'],
            ['Leviticus 23-24'],
            ['Leviticus 25', 'Mark 1'],
            ['Leviticus 26-27', 'Mark 2'],
            ['Numbers 1-2', 'Mark 3'],
            ['Numbers 3-4'],
            ['Numbers 5-6', 'Mark 4'],
            ['Numbers 7-8'],
            ['Numbers 9-11'],
            ['Numbers 12-14', 'Mark 5'],
            ['Numbers 15-16', 'Mark 6'],
            ['Numbers 17-19'],
            ['Numbers 20-22'],
            ['Numbers 23-25', 'Mark 7'],
            ['Numbers 26-28', 'Mark 8'],
            ['Numbers 29-31', 'Mark 9'],
            ['Numbers 32-34'],
            ['Numbers 35-36', 'Mark 10'],
            ['Deuteronomy 1-3'],
            ['Deuteronomy 4-6', 'Mark 11'],
            ['Deuteronomy 7-9'],
            ['Deuteronomy 10-12', 'Mark 12'],
            ['Deuteronomy 13-15'],
            ['Deuteronomy 16-18', 'Mark 13'],
            ['Deuteronomy 19-21'],
            ['Deuteronomy 22-24'],
            ['Deuteronomy 25-27', 'Mark 14'],
            ['Deuteronomy 28-29'],
            ['Deuteronomy 30-31', 'Mark 15'],
            ['Deuteronomy 32-34'],
            ['Joshua 1-3', 'Mark 16'],
            ['Joshua 4-7'],
            ['Joshua 8-10'],
            ['Joshua 11-13'],
            ['Joshua 14-15', 'Luke 1'],
            ['Joshua 16-18', 'Luke 2'],
            ['Joshua 19-21'],
            ['Joshua 22-24', 'Luke 3'],
            ['Judges 1-3', 'Luke 4'],
            ['Judges 4-6'],
            ['Judges 7-8', 'Luke 5'],
            ['Judges 9-10'],
            ['Judges 11-12', 'Luke 6'],
            ['Judges 13-15'],
            ['Judges 16-18', 'Luke 7'],
            ['Judges 19-21'],
            ['Ruth'],
            ['1 Samuel 1-3', 'Luke 8'],
            ['1 Samuel 4-7'],
            ['1 Samuel 8-10'],
            ['1 Samuel 11-12', 'Luke 9'],
            ['1 Samuel 13-14'],
            ['1 Samuel 15-16', 'Luke 10'],
            ['1 Samuel 17-18', 'Luke 11'],
            ['1 Samuel 19-21'],
            ['1 Samuel 22-24'],
            ['1 Samuel 25-26', 'Luke 12'],
            ['1 Samuel 27-29'],
            ['1 Samuel 30-31', 'Luke 13'],
            ['2 Samuel 1-2', 'Luke 14'],
            ['2 Samuel 3-5'],
            ['2 Samuel 6-8'],
            ['2 Samuel 9-11', 'Luke 15'],
            ['2 Samuel 12-13', 'Luke 16'],
            ['2 Samuel 14-15', 'Luke 17'],
            ['2 Samuel 16-18'],
            ['2 Samuel 19-20', 'Luke 18'],
            ['2 Samuel 21-22'],
            ['2 Samuel 23-24', 'Luke 19'],
            ['1 Kings 1-2'],
            ['1 Kings 3-5', 'Luke 20'],
            ['1 Kings 6-7'],
            ['1 Kings 8-9'],
            ['1 Kings 10-11', 'Luke 21'],
            ['1 Kings 12-13'],
            ['1 Kings 14-15', 'Luke 22'],
            ['1 Kings 16-18'],
            ['1 Kings 19-20', 'Luke 23'],
            ['1 Kings 21-22'],
            ['2 Kings 1-3'],
            ['2 Kings 4-6', 'Luke 24'],
            ['2 Kings 7-9'],
            ['2 Kings 10-12', 'John 1'],
            ['2 Kings 13-14', 'John 2'],
            ['2 Kings 15-16', 'John 3'],
            ['2 Kings 17-18'],
            ['2 Kings 19-21'],
            ['2 Kings 22-23', 'John 4'],
            ['2 Kings 24-25', 'John 5'],
            ['1 Chronicles 1-3'],
            ['1 Chronicles 4-7'],
            ['1 Chronicles 8-10'],
            ['1 Chronicles 11-12', 'John 6'],
            ['1 Chronicles 13-15', 'John 7'],
            ['1 Chronicles 16-18'],
            ['1 Chronicles 19-21', 'John 8'],
            ['1 Chronicles 22-24'],
            ['1 Chronicles 25-27'],
            ['1 Chronicles 28-29', 'John 9'],
            ['2 Chronicles 1-3', 'John 10'],
            ['2 Chronicles 4-6'],
            ['2 Chronicles 7-9'],
            ['2 Chronicles 10-12', 'John 11'],
            ['2 Chronicles 13-14'],
            ['2 Chronicles 15-16', 'John 12'],
            ['2 Chronicles 17-18', 'John 13'],
            ['2 Chronicles 19-20'],
            ['2 Chronicles 21-22', 'John 14'],
            ['2 Chronicles 23-24', 'John 15'],
            ['2 Chronicles 25-27', 'John 16'],
            ['2 Chronicles 28-29', 'John 17'],
            ['2 Chronicles 30-31', 'John 18'],
            ['2 Chronicles 32-33'],
            ['2 Chronicles 34-36', 'John 19'],
            ['Ezra 1-2'],
            ['Ezra 3-5', 'John 20'],
            ['Ezra 6-8', 'John 21'],
            ['Ezra 9-10', 'Acts 1'],
            ['Nehemiah 1-3'],
            ['Nehemiah 4-6', 'Acts 2'],
            ['Nehemiah 7-9', 'Acts 3'],
            ['Nehemiah 10-11', 'Acts 4'],
            ['Nehemiah 12-13'],
            ['Esther 1-2', 'Acts 5'],
            ['Esther 3-5'],
            ['Esther 6-8', 'Acts 6'],
            ['Esther 9-10', 'Acts 7'],
            ['Job 1-2'],
            ['Job 3-4'],
            ['Job 5-7', 'Acts 8'],
            ['Job 8-10'],
            ['Job 11-13', 'Acts 9'],
            ['Job 14-16'],
            ['Job 17-19'],
            ['Job 20-21', 'Acts 10'],
            ['Job 22-24', 'Acts 11'],
            ['Job 25-27', 'Acts 12'],
            ['Job 28-29', 'Acts 13'],
            ['Job 30-31'],
            ['Job 32-33', 'Acts 14'],
            ['Job 34-35', 'Acts 15'],
            ['Job 36-37'],
            ['Job 38-40'],
            ['Job 41-42', 'Acts 16'],
            ['Psalms 1-3', 'Acts 17'],
            ['Psalms 4-6'],
            ['Psalms 7-9', 'Acts 18'],
            ['Psalms 10-12'],
            ['Psalms 13-15', 'Acts 19'],
            ['Psalms 16-17', 'Acts 20'],
            ['Psalms 18-19'],
            ['Psalms 20-22'],
            ['Psalms 23-25', 'Acts 21'],
            ['Psalms 26-28', 'Acts 22'],
            ['Psalms 29-30', 'Acts 23'],
            ['Psalms 31-32'],
            ['Psalms 33-34', 'Acts 24'],
            ['Psalms 35-36', 'Acts 25'],
            ['Psalms 37-39', 'Acts 26'],
            ['Psalms 40-42', 'Acts 27'],
            ['Psalms 43-45'],
            ['Psalms 46-48', 'Acts 28'],
            ['Psalms 49-50', 'Romans 1'],
            ['Psalms 51-53', 'Romans 2'],
            ['Psalms 54-56', 'Romans 3'],
            ['Psalms 57-59', 'Romans 4'],
            ['Psalms 60-62', 'Romans 5'],
            ['Psalms 63-65', 'Romans 6'],
            ['Psalms 66-67', 'Romans 7'],
            ['Psalms 68-69'],
            ['Psalms 70-71', 'Romans 8'],
            ['Psalms 72-73', 'Romans 9'],
            ['Psalms 74-76'],
            ['Psalms 77-78', 'Romans 10'],
            ['Psalms 79-80', 'Romans 11'],
            ['Psalms 81-83'],
            ['Psalms 84-86', 'Romans 12'],
            ['Psalms 87-88', 'Romans 13'],
            ['Psalms 89-90', 'Romans 14'],
            ['Psalms 91-93', 'Romans 15'],
            ['Psalms 94-96'],
            ['Psalms 97-99', 'Romans 16'],
            ['Psalms 100-102', '1 Corinthians 1'],
            ['Psalms 103-104', '1 Corinthians 2'],
            ['Psalms 105-106', '1 Corinthians 3'],
            ['Psalms 107-109', '1 Corinthians 4'],
            ['Psalms 110-112', '1 Corinthians 5'],
            ['Psalms 113-115', '1 Corinthians 6'],
            ['Psalms 116-118', '1 Corinthians 7'],
            ['Psalms 119'],
            ['Psalms 120', '1 Corinthians 8'],
            ['Psalms 121-122', '1 Corinthians 9'],
            ['Psalms 123-125', '1 Corinthians 10'],
            ['Psalms 126-128'],
            ['Psalms 129-131', '1 Corinthians 11'],
            ['Psalms 132-134'],
            ['Psalms 135-136', '1 Corinthians 12'],
            ['Psalms 137-139', '1 Corinthians 13'],
            ['Psalms 140-142'],
            ['Psalms 143-145', '1 Corinthians 14'],
            ['Psalms 146-147', '1 Corinthians 15'],
            ['Psalms 148-150'],
            ['Proverbs 1-2', '1 Corinthians 16'],
            ['Proverbs 3-5', '2 Corinthians 1'],
            ['Proverbs 6-7', '2 Corinthians 2'],
            ['Proverbs 8-9', '2 Corinthians 3'],
            ['Proverbs 10-12', '2 Corinthians 4'],
            ['Proverbs 13-15', '2 Corinthians 5'],
            ['Proverbs 16-18', '2 Corinthians 6'],
            ['Proverbs 19-21', '2 Corinthians 7'],
            ['Proverbs 22-24', '2 Corinthians 8'],
            ['Proverbs 25-26', '2 Corinthians 9'],
            ['Proverbs 27-29', '2 Corinthians 10'],
            ['Proverbs 30-31', '2 Corinthians 11'],
            ['Ecclesiastes 1-3'],
            ['Ecclesiastes 4-6', '2 Corinthians 12'],
            ['Ecclesiastes 7-9', '2 Corinthians 13'],
            ['Ecclesiastes 10-12', 'Galatians 1'],
            ['Song of Songs 1-3', 'Galatians 2'],
            ['Song of Songs 4-5', 'Galatians 3'],
            ['Song of Songs 6-8', 'Galatians 4'],
            ['Isaiah 1-2', 'Galatians 5'],
            ['Isaiah 3-4', 'Galatians 6'],
            ['Isaiah 5-6', 'Ephesians 1'],
            ['Isaiah 7-8', 'Ephesians 2'],
            ['Isaiah 9-10', 'Ephesians 3'],
            ['Isaiah 11-13', 'Ephesians 4'],
            ['Isaiah 14-16'],
            ['Isaiah 17-19', 'Ephesians 5'],
            ['Isaiah 20-22', 'Ephesians 6'],
            ['Isaiah 23-25', 'Philippians 1'],
            ['Isaiah 26-27', 'Philippians 2'],
            ['Isaiah 28-29', 'Philippians 3'],
            ['Isaiah 30-31', 'Philippians 4'],
            ['Isaiah 32-33', 'Colossians 1'],
            ['Isaiah 34-36', 'Colossians 2'],
            ['Isaiah 37-38', 'Colossians 3'],
            ['Isaiah 39-40', 'Colossians 4'],
            ['Isaiah 41-42', '1 Thessalonians 1'],
            ['Isaiah 43-44', '1 Thessalonians 2'],
            ['Isaiah 45-46', '1 Thessalonians 3'],
            ['Isaiah 47-49', '1 Thessalonians 4'],
            ['Isaiah 50-52', '1 Thessalonians 5'],
            ['Isaiah 53-55', '2 Thessalonians 1'],
            ['Isaiah 56-58', '2 Thessalonians 2'],
            ['Isaiah 59-61', '2 Thessalonians 3'],
            ['Isaiah 62-64', '1 Timothy 1'],
            ['Isaiah 65-66', '1 Timothy 2'],
            ['Jeremiah 1-2', '1 Timothy 3'],
            ['Jeremiah 3-5', '1 Timothy 4'],
            ['Jeremiah 6-8', '1 Timothy 5'],
            ['Jeremiah 9-11', '1 Timothy 6'],
            ['Jeremiah 12-14', '2 Timothy 1'],
            ['Jeremiah 15-17', '2 Timothy 2'],
            ['Jeremiah 18-19', '2 Timothy 3'],
            ['Jeremiah 20-21', '2 Timothy 4'],
            ['Jeremiah 22-23', 'Titus 1'],
            ['Jeremiah 24-26', 'Titus 2'],
            ['Jeremiah 27-29', 'Titus 3'],
            ['Jeremiah 30-31', 'Philemon 1'],
            ['Jeremiah 32-33', 'Hebrews 1'],
            ['Jeremiah 34-36', 'Hebrews 2'],
            ['Jeremiah 37-39', 'Hebrews 3'],
            ['Jeremiah 40-42', 'Hebrews 4'],
            ['Jeremiah 43-45', 'Hebrews 5'],
            ['Jeremiah 46-47', 'Hebrews 6'],
            ['Jeremiah 48-49', 'Hebrews 7'],
            ['Jeremiah 50', 'Hebrews 8'],
            ['Jeremiah 51-52', 'Hebrews 9'],
            ['Lamentations 1-2', 'Hebrews 10'],
            ['Lamentations 3-5'],
            ['Ezekiel 1-2'],
            ['Ezekiel 3-4', 'Hebrews 11'],
            ['Ezekiel 5-7', 'Hebrews 12'],
            ['Ezekiel 8-10', 'Hebrews 13'],
            ['Ezekiel 11-13', 'James 1'],
            ['Ezekiel 14-15', 'James 2'],
            ['Ezekiel 16-17', 'James 3'],
            ['Ezekiel 18-19', 'James 4'],
            ['Ezekiel 20-21', 'James 5'],
            ['Ezekiel 22-23', '1 Peter 1'],
            ['Ezekiel 24-26', '1 Peter 2'],
            ['Ezekiel 27-29', '1 Peter 3'],
            ['Ezekiel 30-32', '1 Peter 4'],
            ['Ezekiel 33-34', '1 Peter 5'],
            ['Ezekiel 35-36', '2 Peter 1'],
            ['Ezekiel 37-39', '2 Peter 2'],
            ['Ezekiel 40-41', '2 Peter 3'],
            ['Ezekiel 42-44', '1 John 1'],
            ['Ezekiel 45-46', '1 John 2'],
            ['Ezekiel 47-48', '1 John 3'],
            ['Daniel 1-2', '1 John 4'],
            ['Daniel 3-4', '1 John 5'],
            ['Daniel 5-7', '2 John 1'],
            ['Daniel 8-10', '3 John 1'],
            ['Daniel 11-12', 'Jude 1'],
            ['Hosea 1-4', 'Revelation 1'],
            ['Hosea 5-8', 'Revelation 2'],
            ['Hosea 9-11', 'Revelation 3'],
            ['Hosea 12-14', 'Revelation 4'],
            ['Joel', 'Revelation 5'],
            ['Amos 1-3', 'Revelation 6'],
            ['Amos 4-6', 'Revelation 7'],
            ['Amos 7-9', 'Revelation 8'],
            ['Obadiah', 'Revelation 9'],
            ['Jonah', 'Revelation 10'],
            ['Micah 1-3', 'Revelation 11'],
            ['Micah 4-5', 'Revelation 12'],
            ['Micah 6-7', 'Revelation 13'],
            ['Nahum', 'Revelation 14'],
            ['Habakkuk', 'Revelation 15'],
            ['Zephaniah', 'Revelation 16'],
            ['Haggai', 'Revelation 17'],
            ['Zechariah 1-4', 'Revelation 18'],
            ['Zechariah 5-8', 'Revelation 19'],
            ['Zechariah 9-12', 'Revelation 20'],
            ['Zechariah 13-14', 'Revelation 21'],
            ['Malachi 1-4', 'Revelation 22']]

def todays_reading(testament):
    today = datetime.today()
    year_start = datetime(today.year, 1, 1)
    day_of_year = today.toordinal() - year_start.toordinal()
    if testament == "ot":
        return readings[day_of_year][0]
    elif testament == "nt":
        return readings[day_of_year][1]
    else:
        raise ValueError("Testament must be either 'ot' or 'nt'.")

