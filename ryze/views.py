from django.shortcuts import render
from google_search import googlecse
from googleapiclient.discovery import build




# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'ryze/index.html', context=context_dict)


def search(request):
    """
    user_query = request.GET.get('query')

    service = build("customsearch", "v1", developerKey="AIzaSyAjz8fLDQBNlMBLljPS8Q8VhIMYqU_opH8")
    res = service.cse().list(q='database', cx='004192970191558059822:zzokqrg_eni',).execute()

    """
    """
        for r in res['items']:
        print r.keys()
        print r['title']
        print r['formattedUrl']
        print
    """

    x = googlecse(CSE_ID='004192970191558059822:zzokqrg_eni', API_KEY='AIzaSyAjz8fLDQBNlMBLljPS8Q8VhIMYqU_opH8')
    context_dict = {}
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            y = x.results(query=query)
            for result in y:
                print result[1]['title']
                print result[1].keys()
            context_dict['results'] = result
    return render(request, 'ryze/search.html', context=context_dict)
