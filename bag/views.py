from django.shortcuts import render


def view_bag(request):

    """ A view to that renders the Bag content page """
    
    return render(request, 'bag/bag.html')
