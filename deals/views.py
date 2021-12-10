from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . models import dealTable

# Create your views here.

@csrf_exempt
def addDeal(request):

    if request.method == 'POST':
        dealName = request.POST['dealname']
        startTime = request.POST['starttime']
        endTime = request.POST['endtime']
        price =  request.POST['price']
        quantity = request.POST['quantity']

        try:
            if dealTable.objects.filter(dealname=dealName).exists == True:
                return JsonResponse({'status':"Already Exists"})
            else:
                try:
                    dealTable.objects.create(dealname=dealName,
                                            startTime=startTime,
                                            endTime=endTime,
                                            price=price,
                                            quantity=quantity)
                    return JsonResponse({'status':'Deal Created'})
                except Exception as e:
                    return JsonResponse({'status':e})
        except Exception as e:
            return JsonResponse({'status':e})


@csrf_exempt
def enddeal(request):
    if request.method == 'POST':
        dealName = request.POST['dealname']
        try:
            if dealTable.objects.filter(dealname=dealName).exists() == True:
                dealTable.objects.filter(dealname=dealName).delete()
                return JsonResponse({'status':'Deal Closed'})
            else:
                return JsonResponse({'status':'No Deal'})
        except Exception as e:
            return JsonResponse({'status':e})


@csrf_exempt
def updatedeal(request):
    if request.method == 'POST':
        dealName = request.POST['dealname']
        startTime = request.POST['starttime']
        endTime = request.POST['endtime']
        price =  request.POST['price']
        quantity = request.POST['quantity']
        

        try:
            if dealTable.objects.filter(dealname=dealName).exists() == True:
                dealTable.objects.update(dealname=dealName,
                                         startTime=startTime,
                                         endTime=endTime,
                                         price=price,
                                         quantity=quantity)
                return JsonResponse({'status':'Deal Updated'})
            else:
                return JsonResponse({'status':'No Deal'})
        except Exception as e:
            return JsonResponse({'status':e})

# #Given
# dealid = dealID

# dealTable.objects.filter(dealid=dealID).values('dealname','price')


# Book, Author 
# dealTable.objects.select_related(book_id=author_id)
