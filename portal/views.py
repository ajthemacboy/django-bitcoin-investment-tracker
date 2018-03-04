from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Investment
from .models import INVESTMENT
from .functions import get_btcprice


def landing(request):
    return HttpResponseRedirect('add')


def portal_add(request):
    if request.method == 'POST':
        investment = Investment(request.POST, request.FILES)
        if investment.is_valid():
            investment.save()
            return HttpResponseRedirect('/investments/list')

    else:
        investment = Investment()
        return render(request, 'investments/portal_home.html', context={
            'investment': investment,
            'submit_text': "Add Investment"
        })


def portal_list(request):
    objects = {}
    btcprice = get_btcprice()
    totalamount = 0
    totalworth = 0

    for object in INVESTMENT.objects.all().order_by('investment_date', 'investment_time'):
        origworth = object.investment_price * object.investment_amount
        currworth = btcprice * object.investment_amount
        worthchng = currworth - origworth

        objects[object.id] = {
            'date': object.investment_date,
            'time': object.investment_time,
            'price': object.investment_price,
            'amount': object.investment_amount,
            'origworth': round(origworth, 5),
            'currworth': round(currworth, 5),
            'worthchng': round(worthchng, 5)
        }

        totalamount += object.investment_amount
        totalworth += currworth

    return render(request, 'investments/portal_post.html', context={
        'objects': objects,
        'currentprice': btcprice,
        'totalamount': round(totalamount, 5),
        'totalworth': round(totalworth, 5)
    })


def portal_edit(request, id):
    instance = get_object_or_404(INVESTMENT, id=id)
    if request.method == 'POST':
        investment = Investment(request.POST, instance=instance)

        if investment.is_valid():
            investment.save()
            return HttpResponseRedirect('/investments/list')

    else:
        investment = Investment(instance=instance)
        return render(request, 'investments/portal_home.html', context={
            'investment': investment,
            'submit_text': "Update Investment"
        })



def portal_delete(request, id):
    print("Deleting ID", id)
    INVESTMENT.objects.filter(id=id).delete()
    return HttpResponseRedirect('/investments/list')
