from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """
    Renders content of the shoppingbag
    """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    '''
    Adds specified quantity of product to bag
    '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # Gets the users bag as a dict
    bag = request.session.get('bag', {})

    if size:  # block that executes if size is an option
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:  # executes if size is not an option for the item that is being added
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    '''
    View for handling removing and adding items from the bag itself
    '''

    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # Gets the users bag as a dict
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
    else:  # executes if size is not an option for the item that is being added
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
