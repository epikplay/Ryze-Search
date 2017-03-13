from django.shortcuts import render
from google_search import googlecse
from googleapiclient.discovery import build
from ryze.registration_form import UserProfile




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

def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'ryze/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


