from django.shortcuts import render


def view_bag(request):
    """
    Renders content of the shoppingbag
    """

    return render(request, 'bag.html')
