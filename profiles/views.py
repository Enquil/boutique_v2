from django.shortcuts import render


def profile(request):
    '''
    Views the Profile
    '''
    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)
