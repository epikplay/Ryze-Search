import urllib
import json

class googlecse(object):
    def __init__(self, CSE_ID, API_KEY):
        self.CSE_ID = CSE_ID
        self.API_KEY = API_KEY

    def url(self, **kwargs):

            # Input is required. If there is no input, return nothing
            if kwargs['query'] is None:
                return None

            # Checks the length of the API key
            if (len(self.CSE_ID) != 33) or (len(self.API_KEY) != 39):
                return None

            self.query = urllib.urlencode({'q': kwargs['query']})
            self.search_string = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&%s' % (self.API_KEY, self.CSE_ID, self.query)

            # Append the URL if the key is a string
            def append_url(key):
                try:
                    self.search_string += ('&' + urllib.urlencode({key: kwargs[key]}))
                except:
                    pass

            # Append the URL if the key matches one found in a list
            def append_url_list(key, term_list):
                try:
                    for term in term_list:
                        if kwargs[key] == term:
                            self.search_string += ('&' + urllib.urlencode({key: kwargs[key]}))
                            break
                except:
                    pass

            # Geo location of the end user
            country_codes = ['af', 'al', 'dz', 'as', 'ad',
                             'ao', 'ai', 'aq', 'ag', 'ar', 'am',
                             'aw', 'au', 'at', 'az', 'bs', 'bh', 'bd', 'bb',
                             'by', 'be', 'bz', 'bj', 'bm', 'bt', 'bo', 'ba',
                             'bw', 'bv', 'br', 'io', 'bn', 'bg', 'bf', 'bi',
                             'kh', 'cm', 'ca', 'cv', 'ky', 'cf', 'td', 'cl',
                             'cn', 'cx', 'cc', 'co', 'km', 'cg', 'cd', 'ck',
                             'cr', 'ci', 'hr', 'cu', 'cy', 'cz', 'dk', 'dj',
                             'dm', 'do', 'ec', 'eg', 'sv', 'gq', 'er', 'ee',
                             'et', 'fk', 'fo', 'fj', 'fi', 'fr', 'gf', 'pf',
                             'tf', 'ga', 'gm', 'ge', 'de', 'gh', 'gi', 'gr',
                             'gl', 'gd', 'gp', 'gu', 'gt', 'gn', 'gw', 'gy',
                             'ht', 'hm', 'va', 'hn', 'hk', 'hu', 'is', 'in',
                             'id', 'ir', 'iq', 'ie', 'il', 'it', 'jm', 'jp',
                             'jo', 'kz' 'ke', 'ki' 'kp', 'kr' 'kw', 'kg',
                             'la', 'lv' 'lb', 'ls', 'lr', 'ly', 'li', 'lt',
                             'lu', 'mo', 'mk', 'mg', 'mw', 'my', 'mv', 'ml',
                             'mt', 'mh', 'mq', 'mr', 'mu', 'yt', 'mx', 'fm',
                             'md', 'mc', 'mn', 'ms', 'ma', 'mz', 'mm', 'na',
                             'nr', 'np', 'nl', 'an', 'nc', 'nz', 'ni', 'ne',
                             'ng', 'nu', 'nf', 'mp', 'no', 'om', 'pk', 'pw',
                             'ps', 'pa', 'pg', 'py', 'pe', 'ph', 'pn', 'pl',
                             'pt', 'pr', 'qa', 're', 'ro', 'ru', 'rw', 'sh',
                             'kn', 'lc', 'pm', 'vc', 'ws', 'sm', 'st', 'sa', 'sn',
                             'cs', 'sc', 'sl', 'sg', 'sk', 'si', 'sb', 'so',
                             'za', 'gs', 'es', 'lk', 'sd', 'sr', 'sj', 'sz',
                             'se', 'ch', 'sy', 'tw', 'tj', 'tz', 'th', 'tl',
                             'tg', 'tk', 'to', 'tt', 'tn', 'tr', 'tm', 'tc',
                             'tv', 'ug', 'ua', 'ae', 'uk', 'us', 'um', 'uy',
                             'uz', 'vu', 've', 'vn', 'vg', 'vi', 'wf', 'eh',
                             'ye', 'zm', 'zw']

            append_url_list('gl', country_codes)

            # The domain used for the search based on the country the user is located in
            try:
                for country in country_codes:
                    if kwargs['googlehost'] == country:
                        self.search_string += ('&' + urllib.urlencode({'googlehost': 'google.' + kwargs['googlehost']}))
            except:
                    pass

            # Interface language
            language_codes = ['af', 'sq', 'sm', 'ar',
                              'az', 'eu', 'be', 'bn', 'bh', 'bs', 'bg', 'ca',
                              'zh-CN', 'zh-TW', 'hr', 'cs', 'da', 'nl', 'en', 'eo',
                              'et', 'fo', 'fi', 'fr', 'fy', 'gl', 'ka', 'de',
                              'el', 'gu', 'iw', 'hi', 'hu', 'is', 'id', 'ia',
                              'ga', 'it', 'ja', 'jw', 'kn', 'ko', 'la', 'lv',
                              'lt', 'mk', 'ms', 'ml', 'mt', 'mr', 'ne', 'no',
                              'nn', 'oc', 'fa', 'pl', 'pt-BR', 'pt-PT', 'pa', 'ro',
                              'ru', 'gd', 'sr', 'si', 'sk', 'sl', 'es', 'su',
                              'sw', 'sv', 'tl', 'ta', 'te', 'th', 'ti', 'tr',
                              'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'zu']

            append_url_list('hl', language_codes)

            # All results will contain a link to a particular site
            append_url('linkSite')

            # Number of results
            try:
                if (kwargs['num'] < 11) and (round(kwargs['num']) == kwargs['num']):
                    self.search_string += ('&' + urllib.urlencode({'num': kwargs['num']}))
            except:
                pass

            # Search safety level
            safety_levels = ['high', 'medium', 'off']
            append_url_list('safe', safety_levels)

            # If the page parameter is less than 11, increment the pages
            try:
                if (kwargs['pages'] < 11) and (round(kwargs['pages']) == kwargs['pages']):
                    self.query_loop = kwargs['pages']
                else:
                    self.query_loop = 1
            except:
                self.query_loop = 1

            return self.search_string


    def results(self, **kwargs):
        loaded_url = self.url(**kwargs)
        data = ''
        result_list = []

        for index in range(0, self.query_loop):
            if index == 0:
                current_loaded_url = loaded_url
            else:
                current_loaded_url = loaded_url + "&start=" + str(index*10)

            data = json.loads(urllib.urlopen(current_loaded_url).read())

            try:
                # Search info
                total_results = data['searchInformation']['totalResults']
                self.formatted_total_results = data['searchInformation']['formattedTotalResults']
                self.search_time = data['searchInformation']['searchTime']
                self.formatted_search_time = data['searchInformation']['formattedSearchTime']
                self.cse_title = data['context']['title']
            except:
                break

            # The results
            result_list.append(data['items'])

            # If the total possible pages are less than the number of pages that
            # have been requested, end this for-loop early at this point,
            # because it is pointless to make more requests
            if (float(total_results) % 10) > 1:
                total_pages = (float(total_results) / 10) + 1
            else:
                total_pages = float(total_results) / 10

            if (self.query_loop > total_pages) and (index == total_pages):
                break
            else:
                pass

        return result_list