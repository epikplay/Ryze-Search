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
        self.search_string = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&%s' \
                                 % (self.API_KEY, self.CSE_ID, self.query)

        # Number of results
        try:
            if (kwargs['num'] < 11) and (round(kwargs['num']) == kwargs['num']):
                self.search_string += ('&' + urllib.urlencode({'num': kwargs['num']}))
        except:
            pass

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
        self.refinements_list = []

        for index in range(0, self.query_loop):
            if index == 0:
                current_loaded_url = loaded_url
            else:
                current_loaded_url = loaded_url + "&start=" + str(index*10)

            data = json.loads(urllib.urlopen(current_loaded_url).read())

            try:
                # Search info
                self.total_results = data['searchInformation']['totalResults']
                self.formatted_total_results = data['searchInformation']['formattedTotalResults']
                self.search_time = data['searchInformation']['searchTime']
                self.formatted_search_time = data['searchInformation']['formattedSearchTime']
            except:
                break

            # The results
            result_list.append(data['items'])

            # The refinements
            self.refinements_list.append(data['context']['facets'])

            # If the total possible pages are less than the number of pages that
            # have been requested, end this for-loop early at this point,
            # because it is pointless to make more requests
            if (float(self.total_results) % 10) > 1:
                total_pages = (float(self.total_results) / 10) + 1
            else:
                total_pages = float(self.total_results) / 10

            if (self.query_loop > total_pages) and (index == total_pages):
                break
            else:
                pass

        return result_list

    def image_results(self, **kwargs):
        loaded_url = self.url(**kwargs) + '&searchType=image'

        data = ''
        result_list = []

        data = json.loads(urllib.urlopen(loaded_url).read())

        try:
            # Search info
            self.total_results = data['searchInformation']['totalResults']
            self.formatted_total_results = data['searchInformation']['formattedTotalResults']
            self.search_time = data['searchInformation']['searchTime']
            self.formatted_search_time = data['searchInformation']['formattedSearchTime']
        except:
            pass

        # The image results
        result_list.append(data['items'])

        return result_list

    def sorted_results(self, **kwargs):
        loaded_url = self.url(**kwargs) + '&sort=date'

        data = ''
        result_list = []

        data = json.loads(urllib.urlopen(loaded_url).read())

        try:
            # Search info
            self.total_results = data['searchInformation']['totalResults']
            self.formatted_total_results = data['searchInformation']['formattedTotalResults']
            self.search_time = data['searchInformation']['searchTime']
            self.formatted_search_time = data['searchInformation']['formattedSearchTime']
        except:
            pass

        # The image results
        result_list.append(data['items'])

        return result_list
