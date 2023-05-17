from django.shortcuts import render


def profile(request):
    '''
    Views the Profile
    '''
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
