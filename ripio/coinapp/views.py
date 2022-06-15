from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.db import IntegrityError
from django.db.models import Q
from .models import Coin, User, Registry

# Create your views here.
def index(request):
    return render(request, 'coinapp/index.html')

def create_coin(request, message=None):
    try:
        coin_list = Coin.objects.all()
    except Coin.DoesNotExist:
        raise Http404("Coin does not exist on the DB")
    context = {'coin_list': coin_list, 'message': message}
    return render(request, 'coinapp/create_coin.html', context)

def balance(request, user_name):
    try:
        user_list = User.objects.filter(user_name=user_name) 
    except Coin.DoesNotExist:
        raise Http404("Coin does not exist on the DB")
    user_balance = {'balance_list':{user.coin.coin_name : user.balance for user in user_list}}
    return render(request, 'coinapp/balance.html',  user_balance)

def movements(request, user_name):
    try:
        movements = Registry.objects.filter(Q(sender_name=user_name) | Q(receiver_name=user_name))
    except Coin.DoesNotExist:
        raise Http404("Registry does not exist on the DB")
    return render(request, 'coinapp/movements.html',  {'movements': movements})

def send_money(request, message=None):
    try:
        coin_list = [coin.coin_name for coin in Coin.objects.all()]
    except Coin.DoesNotExist:
        raise Http404("Coin does not exist on the DB")
    context = {'coin_list': coin_list, 'message': message}
    return render(request, 'coinapp/send_money.html',  context)

def save_coin(request):
    try:
        coin = Coin(coin_name=request.POST['coin_name'].capitalize(), creation_date=timezone.now())
        coin.save()
        return create_coin(request)
    except IntegrityError:
        return create_coin(request, message="There is already another coin named %s" % coin)
    except ValueError as e:
        return create_coin(request, message=e)

def make_transfer(request): #This function should be separated as it does a lot of things and it's messy
    try:
        receiver = request.POST['receiver_name']
        sender = 'Diego' #This should also be request.POST['sender_name'] if there was a session
        amount = float(request.POST['amount'])
        coin = request.POST['coin']
        coinObject = Coin.objects.get(coin_name=coin)
        sender_user = User.objects.filter(user_name=sender, coin=coinObject.id)
        sender_user = sender_user[0] if sender_user else ''
        if transfer_to_myself(sender, receiver):
            message = "You cannot send money to yourself"
        elif sender_user and has_balance(sender_user, amount):
            try:
                User.objects.get(user_name=receiver)
                receiver_user_coin_balance = User.objects.filter(user_name=receiver, coin=coinObject.id)
                if not receiver_user_coin_balance:
                    receiver_user_coin_balance = User(user_name=receiver, balance=0.0, coin=coinObject)
                    receiver_user_coin_balance.save()
                receiver_user_coin_balance.balance = receiver_user_coin_balance.balance + amount
                receiver_user_coin_balance.save()
                sender_user.balance = sender_user.balance - amount
                sender_user.save()

                registry = Registry(sender_name=sender, receiver_name=receiver, coin_used=coin, amount=amount, operation_date=timezone.now())
                registry.save()

                message = "Transfer was successful"
            except User.DoesNotExist:
                message = "The user you are trying to send money to does not exist"
        else:
            message = "Transfer was unsuccessful due to lack of founds"
    except ValueError as e:
        return send_money(request, message=e)
    return send_money(request, message=message)
    # return HttpResponseRedirect(reverse('coinapp:send_money', args=(message,))) => This should solve the issue of reloading the page and sending again the post message, But I cannot resolve how to pass the message

def has_balance(sender_user, amount):
    response = False
    if sender_user.balance >= amount:
        response = True
    return response

def transfer_to_myself(sender, receiver):
    return sender == receiver


