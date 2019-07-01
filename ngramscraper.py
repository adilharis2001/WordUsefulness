
#!/usr/bin/env python

from __future__ import print_function

import httplib, urllib, re, json, time, xlsxwriter

class NgramScraper(object):
    """
    Web scraper that queries Google's Ngram Viewer for the given word,
    and the scrapes out the frequencies.
    """

    def __init__(self):
        self._year_start = 1900
        self._year_end = 2019
        self._regexp = re.compile('var data = (.+?);')

    @property
    def year_start(self):
        return self._year_start

    @property
    def year_end(self):
        return self._year_end

    @year_start.setter
    def year_start(self, start):
        self._year_start = start

    @year_end.setter
    def year_end(self, end):
        self._year_end = end

    def query(self, ngram):
        # Build the request url
        url = '/ngrams/graph?content='
        url = url + urllib.quote_plus(ngram)
        url = url + '&year_start=' + str(self._year_start)
        url = url + '&year_end=' + str(self._year_end)
        url = url + '&direct_url=' + urllib.quote_plus('t1;,' + ngram + ';,c0')

        conn = httplib.HTTPSConnection('books.google.com')
        conn.request('GET', url)
        resp = conn.getresponse()
        html = resp.read()
        match = self._regexp.search(html)
        if match is None:
            return None
        data = json.loads(match.group(1))
        if len(data) < 1:
            return None
        else:
            return data[0]

    def query_most_recent_freq(self, ngram):
        data = self.query(ngram)
        return data['timeseries'][-1] if data else None

if __name__ == '__main__':
    import json
    import sys
    s = NgramScraper()
    words = open("words.txt", "r")
    from random import randint
    row_num = 1
    data = []
    for word in words:
    	result = s.query(ngram=' '+word)
        #sleep timer between queries so that we don't exceed google query threshholds
    	time.sleep(randint(0, 10))
    	output = result["timeseries"]
        lastIndex = len(output) - 1
        # Loop through to get slope ratings
        i = 0
    	j = len(output) - 1
        slopeRating = 0
        while i < j/2:
            slopeRating += output[j] - output[i]
            i = i + 1
            j = j - 1
        # End of loop for slope ratings
        data.append([row_num, word.rstrip(), round(slopeRating*100000000,2), round(output[lastIndex]*100000000,2)])
        row_num = row_num + 1
    print(data)
    workbook = xlsxwriter.Workbook('GREWordFrequencyAdil.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.add_table(0,0,row_num-1,3,{'data': data,
                                         'style': 'Table Style Light 11',
                                         'name': 'GREWordsTable',
                                         'columns': [{'header': 'Number'},
                                          {'header': 'Word'},
                                          {'header': '1900-2008 Slope Rating'},
                                          {'header': '2008 Frequency Rating'},
                                          ]})
    workbook.close()
    words.close()
