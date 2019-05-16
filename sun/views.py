from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from datetime import date
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from .forms import PartsForm, ManiProForm,AccountsForm,EmpAccForm
from .models import (Products, Customers, Accounts, Booking, BookingDetails, Sales, SalesDetails,
                     ProVdPpPr, AccountsLedger, Employees, EmpAccounts, BabakLedger, DebRecvLedger,
                    PayLed, Purchase, PurchaseDetails, Parts, ManiPro, Salesreturn, Salesreturndetail,
                    SalDetails, Stock, StockDetails)

from .dbview import Empview
from .forms import EmployeeForm


def home(request):
    return render(request, 'dashboard.html')


@csrf_exempt
def add_products(request):
    if request.POST:
        name = request.POST.getlist('pn')[0]
        pp = float(request.POST.getlist('pp')[0])
        rp = float(request.POST.getlist('rp')[0])
        qty = int(request.POST.getlist('qty')[0])
        e = request.POST.getlist('ecod')[0]

        p = Products.objects.create(name=name, p_p=pp, r_p=rp, qty=qty, e_code=e, dt=date.today())

    return render(request, 'products/add_product_fp.html')


@csrf_exempt
def add_customers(request):
    if request.POST:
        name = request.POST.getlist('cname')[0]
        cty = request.POST.getlist('city')[0]
        add = request.POST.getlist('add')[0]
        cont = request.POST.getlist('con')[0]

        c = Customers.objects.create(cust_name=name, city=cty, contact_no=cont, dat=date.today())
        a = Accounts.objects.create(accounts_name=name, credit=int(0), debit=int(0), customers_cust=c,opn_date=date.today())

    return render(request, 'customers/add_customer_fp.html')


@csrf_exempt
def add_booking_page(request):
    all_cust = Customers.objects.all()
    all_pus = Products.objects.all()
    if request.method == 'POST':
        cust = request.POST.getlist('cust')[0]
        dt = request.POST.getlist('dt')[0]

        pro = request.POST.getlist('pro')
        amt = request.POST.getlist('amt')
        dis = request.POST.getlist('dis')
        qty = request.POST.getlist('qty')
        ec = request.POST.getlist('ecode')
        t = request.POST.getlist('total')

        b = Booking.objects.create(cust_name=cust, dat=dt)
        btotal = 0
        for x in range(len(pro)):
            bd = BookingDetails.objects.create(pro_name=pro[x], qty=qty[x],
                                               amt=amt[x],  booking_booking=b,
                                               ecode=ec[x], discount=dis[x], total=float(t[x]))
            btotal += float(t[x])

            p = get_object_or_404(Products,name=pro[x])
            p.qty = p.qty - int(qty[x])
            p.save()





        cust = Accounts.objects.get(accounts_name=cust)
        cust.var = btotal
        cust.bkvar = cust.debit

        cust.debit = cust.debit + btotal
        cust.save()



    context = {'all_com': all_cust, 'all_pus': all_pus}
    return render(request, 'booking/add_booking.html', context)

@csrf_exempt
def gen_pdf_for_booking(request):
    a = Booking.objects.latest('booking_id')
    cacc = Accounts.objects.get(accounts_name=a.cust_name)
    custt = get_object_or_404(Customers, cust_name=a.cust_name)

    b = BookingDetails.objects.filter(booking_booking=a)
    return render(request, 'booking/booking_bill.html', {'aa': a, 'bb': b, 'cact': cacc, 'c':custt})



def add_booking_row(request):
    all_pus = Products.objects.all()
    htmlf = render_to_string('booking/add_booking_row.html', {'all_pus': all_pus}, request=request)
    return JsonResponse({'htmlf': htmlf})


def get_amt_for_booking(request, name):
    c = get_object_or_404(Products, name=name)
    d = [c.r_p]
    print(d)
    return JsonResponse({'d': d})


def add_sale_row(request):
    all_pus = Products.objects.all()
    htmlf = render_to_string('orders/old/orders_2nd.html', {'all_pus': all_pus}, request=request)
    return JsonResponse({'htmlf': htmlf})


def get_amt_for_sales(request, name):
    c = get_object_or_404(Products, name=name)
    d = [c.qty, c.r_p, c.e_code]
    print(d)
    return JsonResponse({'d': d})

@csrf_exempt
def add_sales_page(request):
    allpro = Products.objects.all()
    all_cust = Customers.objects.all()

    if request.method == 'POST':
        print(request.POST)

        cust = request.POST.getlist('cust')[0]
        pro = request.POST.getlist('pro')
        price = request.POST.getlist('price')
        qty = request.POST.getlist('qty')
        dis = request.POST.getlist('dis')
        amt = request.POST.getlist('price')
        net_total = request.POST.getlist('net_total')[0]
        paid = request.POST.getlist('paid')[0]
        due = request.POST.getlist('due')[0]
        ecode = request.POST.getlist('Ecode')


        b = Sales.objects.create(cust_name=cust,dat=date.today(),net_total = float(net_total),
                                 paid = float(paid), due=round(float(due),2))

# t - ((t * dis)/100)

        for x in range(len(pro)):
            f = int(price[x]) * int(qty[x])
            ff = f - (f * int(dis[x])/100)

            sd = SalesDetails.objects.create(pro_name= pro[x], price = amt[x], qty=qty[x],
                                            total= float(ff), dat=date.today(),
                                             sales_sales = b, dis=dis[x],ecode=ecode[x])

            p = get_object_or_404(Products, name=pro[x])
            p.qty = p.qty - int(qty[x])
            p.save()

            nw = ProVdPpPr()
            nw.p_name = p.name
            nw.p_pp   = p.p_p

            nw.p_rp   = p.r_p
            nw.saled_price = price[x]
            total = float(nw.saled_price) - nw.p_pp
            nw.profit = total

            nw.total = total * int(qty[x])

            nw.dat = date.today()
            nw.qty = int(qty[x])
            nw.sal_id = b.sales_id
            nw.save()

        owner = Accounts.objects.get(accounts_name='Mr Sun')
        owner.credit = owner.credit + float(paid)
        owner.save()

        cust = Accounts.objects.get(accounts_name=cust)
        cust.var = cust.debit

        cust.debit = cust.debit + float(due)
        cust.save()




    context = {'all_pus': allpro, 'all_cust': all_cust}
    return render(request, 'orders/old/orders.html', context)

@csrf_exempt
def gen_pdf_for_sales(request):
    a = Sales.objects.latest('sales_id')
    cacc = Accounts.objects.get(accounts_name=a.cust_name)
    custt = get_object_or_404(Customers, cust_name=a.cust_name)


    b = SalesDetails.objects.filter(sales_sales=a)
    return render(request, 'sales/sales_report.html', {'aa': a, 'bb': b, 'cact': cacc, 'c':custt})

def todays_sale_report(request):
    # Sales list
    s = Sales.objects.filter(order_date=date.today())

    print('todays salessssss')
    # Sum of Products Saled Price
    pr = ProVdPpPr.objects.filter(dat=date.today()).aggregate(Sum('total'))
    if pr['total__sum'] is None:
        pr['total__sum'] = 0
    tp = round(pr['total__sum'],2)


    # Sum of Sales Paid => means sales of the day
    ns = Sales.objects.filter(order_date=date.today()).aggregate(Sum('paid'))
    if ns['paid__sum'] is None:
        ns['paid__sum'] = 0
    todays_sale = round(ns['paid__sum'], 2)

    # Sum of Sales Due => means Dues of the Day
    nd = Sales.objects.filter(order_date=date.today()).aggregate(Sum('due'))
    if nd['due__sum'] is None:
        nd['due__sum'] = 0
    todays_due = round(nd['due__sum'], 2)

    # Sum of Expenses of the Day
    exp = AccountsLedger.objects.filter(dat=date.today()).aggregate(Sum('amount'))
    if exp['amount__sum'] is None:
        exp['amount__sum'] = 0

    exp2 = exp['amount__sum']
    print('hererere is exp2: line 289', exp2)
    totalsale = round(todays_sale + todays_due, 2)

    fprofit = tp - exp2
    context = {'s': s, 'todayssale': todays_sale, 'todaysdue': todays_due, 'totalsale': totalsale, 'exp': exp2,'profit': fprofit}
    return render(request, 'sales/todays_sale_report.html',context )



@csrf_exempt
def add_expense(request):

    if request.method == 'POST':
        des = request.POST.getlist('des')[0]
        amt = request.POST.getlist('amount')[0]
        dt = request.POST.getlist('dt')[0]
        # frm = request.POST.getlist('dcom')
        gv = request.POST.getlist('gv')[0]

        ac = Accounts.objects.get(accounts_name='Mr Sun')
        ac.credit = ac.credit - float(amt)
        ac.save()

        al = AccountsLedger.objects.create(
        given_from='Mr Sun', given_to= gv, desc=des, amount= float(amt),
                dat=str(dt), accounts_accounts= ac
            )
        al.save()
        return JsonResponse({})
    else:
        return render(request,'expense/add_exp.html')


    #
    # acc.credit_amount = acc.credit_amount - int(form.cleaned_data['amount'])
    # acc.save()
    # xp = Accounts.objects.get(accounts_name='Daily Expenses')
    # xp.credit_amount = xp.credit_amount + int(form.cleaned_data['amount'])
    # xp.save()
    # print('okkkk')
    # return redirect('addly')

def add_employess(request):
    e = Empview.objects.all()

    form = EmployeeForm(request.POST or None)
    if form.is_valid():

        form.save()
        e = Employees.objects.latest('employees_id')
        ea = EmpAccounts.objects.create(
            emp_account_name=e.employees_name, emp_accounts_credit=0, emp_accounts_debit=0,
            employees_employees=e
        )
        return redirect('addemp')

    return render(request, 'employess/add_emp_fp.html', {'form': form,'e':e})

def all_acc(request):
    bab = Accounts.objects.get(accounts_name='Mr Sun')

    accs = Accounts.objects.all().exclude(accounts_name='Mr Sun')
    query = request.GET.get('q')
    if query:
        accs = Accounts.objects.filter(accounts_name__icontains=query)

    acd = Accounts.objects.exclude(accounts_name='Mr Sun').aggregate(Sum('debit'))
    if acd['debit__sum'] is None:
        acd['debit__sum'] = 0
    d = round(acd['debit__sum'])
    dtonyou = Accounts.objects.exclude(accounts_name='Mr Sun').aggregate(Sum('credit'))

    if dtonyou['credit__sum'] is None:
        dtonyou['credit__sum'] = 0

    print('this is aggre without babak and mukadam',dtonyou)

    tdf = Accounts.objects.filter(debit__gt=1).count()

    tdtonyou = Accounts.objects.exclude(accounts_name='Mr Sun').filter(credit__gt=1).count()


    e = round(dtonyou['credit__sum'])
    print('here is eeee: ',e)
    context = {'accs': accs ,'dd':d, 'mydebit':e, 'df':tdf,'total':tdtonyou,'cash':bab}

    return render(request, 'allaccounts/acc.html', context )

@csrf_exempt
def transfer_debt_from_com_to_babak_page(request):
    acc = Accounts.objects.all()

    if request.method == 'POST':
        c = request.POST.getlist('com')[0]
        amt = request.POST.getlist('amount')[0]
        dt = request.POST.getlist('dt')[0]
        descrp = request.POST.getlist('des')[0]
        rm = request.POST.getlist('RMB')[0]
        rup = request.POST.getlist('Rupees')[0]

        # bl,created =  BabakLedger.objects.get_or_create(name=c,
        #                                         debit_amount=0,desc=descrp,dat=dt,rmb=rm,rup=rup)
        # bl.debit_amount = bl.debit_amount + float(amt)
        # bl.
        # bl.save()
        bl = BabakLedger.objects.create(name=c,debit_amount=amt,desc=descrp,dat=dt,rmb=rm,rup=rup)

        c = get_object_or_404(Accounts,accounts_name=c)

        print('condition meet')

        c.credit = c.credit + float(amt)
        c.save()




        return JsonResponse({})

    context = {'acc':acc}
    return render(request,'allaccounts/transfer_debt_to_babak_acc.html',context)


def babak_debit(request):
    bd = BabakLedger.objects.all()

    return render(request,'allaccounts/bak_ledger.html',{'leg':bd})


# ------------Debt Update Accounts Page --------------------------------

@csrf_exempt
def add_amount_account_page(request):
    acc = Accounts.objects.all()
    if request.method == 'POST':
        c = request.POST.getlist('comn')[0]
        amt = request.POST.getlist('amount')[0]
        dt = request.POST.getlist('dt')[0]
        descrp = request.POST.getlist('des')[0]
        m = request.POST.getlist('method')[0]

        com = get_object_or_404(Customers, cust_name=c)
        acc = get_object_or_404(Accounts, customers_cust=com)
        if acc.debit == 0:
            return redirect('adamtpg')
        else:
            print('i am in else block: ')
            acc.debit = int(acc.debit) - int(amt)
            ow = get_object_or_404(Accounts, accounts_name='Mr Sun')
            ow.credit = int(ow.credit) + int(amt)
            acc.desc = descrp
            acc.save()
            print('else block okay done')
            # add details to Ledger

            al = DebRecvLedger()
            al.name   = c
            al.desc   = descrp
            al.amount = int(amt)
            al.dat    = str(dt)
            al.customers_customers = com
            al.method = m

            al.debit_amount = acc.debit
            al.save()

            ow.save()
            return JsonResponse({})
    else:
        return render(request, 'debt/add_return_amount.html', {'acc': acc})




@csrf_exempt
def add_amount_account_page_com(request):
    acc = Accounts.objects.all()
    if request.method == 'POST':
        c = request.POST.getlist('comn')[0]
        amt = request.POST.getlist('amount')[0]
        dt = request.POST.getlist('dt')[0]
        descrp = request.POST.getlist('des')[0]
        m = request.POST.getlist('method')[0]

        com = get_object_or_404(Customers, cust_name=c)
        acc = get_object_or_404(Accounts, customers_cust=com)
        if acc.credit == 0:
            print('i am in else block: ')
            acc.credit = int(acc.credit) - int(amt)
            ow = get_object_or_404(Accounts, accounts_name='Mr Sun')
            ow.credit = int(ow.credit) - int(amt)
            acc.save()
            print('else block okay done')
            # add details to Ledger

            al = PayLed()
            al.name   = c
            al.desc   = descrp
            al.amount = int(amt)
            al.dt    = str(dt)
            al.customers_customers = com
            al.method = m
            al.save()
            ow.save()
            return redirect('adamtpg')
        else:

            print('i am in else block: ')
            acc.credit = int(acc.credit) - int(amt)
            ow = get_object_or_404(Accounts, accounts_name='Mr Sun')
            ow.credit = int(ow.credit) - int(amt)
            acc.save()
            print('else block okay done')
            # add details to Ledger

            al = PayLed()
            al.name   = c
            al.desc   = descrp
            al.amount = int(amt)
            al.dt    = str(dt)
            al.customers_customers = com
            al.method = m
            al.save()
            ow.save()
            return JsonResponse({})
    else:
        return render(request, 'payment/pay_to_company.html', {'acc': acc})










#-----------------------ledger of Recieved Debts-------------------------
def debt_ledger(request):
    l = DebRecvLedger.objects.all()

    return render(request,'allaccounts/ledger.html',{'leg':l})





#-----------------------ledger of Paid Debts-------------------------
def own_debt_ledger(request):
    l = PayLed.objects.all()

    return render(request,'payment/ledger.html',{'leg':l})

#---------------- All Reports---------------------------------


@staff_member_required
def all_stock_report(request):
    allstock = Products.objects.all()
    tp = Products.objects.count()
    pp = Products.objects.all().aggregate(Sum('p_p'))
    if pp['p_p__sum'] is None:
        pp['p_p__sum'] = 0
    ppp = round(pp['p_p__sum'], 2)

    rp = Products.objects.all().aggregate(Sum('r_p'))
    if rp['r_p__sum'] is None:
        rp['r_p__sum'] = 0
    r = round(rp['r_p__sum'], 2)

    rr = r - ppp
    print('profit is : ',rr)

    context = {'allstock': allstock, 'tp': tp, 'amt': ppp, 'r': rr}
    return render(request, 'products/product_stock_report.html',context )


















# ------------------Todays Sales Report -----------------------------
def todays_sale_report(request):
    # Sales list
    s = Sales.objects.filter(dat=date.today())

    print('todays salessssss')
    # Sum of Products Saled Price
    pr = ProVdPpPr.objects.filter(dat=date.today()).aggregate(Sum('total'))
    if pr['total__sum'] is None:
        pr['total__sum'] = 0
    tp = round(pr['total__sum'],2)


    # Sum of Sales Paid => means sales of the day
    ns = Sales.objects.filter(dat=date.today()).aggregate(Sum('paid'))
    if ns['paid__sum'] is None:
        ns['paid__sum'] = 0
    todays_sale = round(ns['paid__sum'], 2)

    # Sum of Sales Due => means Dues of the Day
    nd = Sales.objects.filter(dat=date.today()).aggregate(Sum('due'))
    if nd['due__sum'] is None:
        nd['due__sum'] = 0
    todays_due = round(nd['due__sum'], 2)

    # Sum of Expenses of the Day
    exp = AccountsLedger.objects.filter(dat=date.today()).aggregate(Sum('amount'))
    if exp['amount__sum'] is None:
        exp['amount__sum'] = 0

    exp2 = exp['amount__sum']
    print('hererere is exp2: line 289', exp2)
    totalsale = round(todays_sale + todays_due, 2)

    fprofit = tp - exp2
    context = {'s': s, 'todayssale': todays_sale, 'todaysdue': todays_due, 'totalsale': totalsale, 'exp': exp2,'profit': fprofit}
    return render(request, 'sales/todays_sale_report.html',context )


# -------------Shop and Personal Expense Report ------------------------

def shop_exp_report(request):
    al = AccountsLedger.objects.filter(accounts_accounts__accounts_name='Mr Sun').filter(dat=date.today())
    t = AccountsLedger.objects.filter(dat=date.today()).aggregate(Sum('amount'))
    total = t['amount__sum']
    return render(request,'expense/shop.html',{'leg':al,'total':total})

def shop_exp_report_all(request):
    al = AccountsLedger.objects.filter(accounts_accounts__accounts_name='Mr Sun')
    t = AccountsLedger.objects.filter(accounts_accounts__accounts_name='Mr Sun').aggregate(Sum('amount'))
    total = t['amount__sum']
    return render(request,'expense/shop.html',{'leg':al,'total':total})


#------Find Sales Bill Page --------------------------------------
def fetch_all_sales_report(request):
    return render(request, 'sales/bills.html')


# -----------Search Invoice by Bill No Page ----------------------
def all_sales_report(request, id):
    s = get_object_or_404(Sales, sales_id=id)
    cacc = Accounts.objects.get(accounts_name=s.cust_name)
    cust = get_object_or_404(Customers, cust_name=cacc.accounts_name)
    print(cacc.debit)
    return render(request, 'sales/bills_2nd.html', {'s': s, 'cact': cacc, 'cust':cust})

#-----------------------Debt Recieve Inovice--------------------------------------
def debt_recipt_for_debt(request):
    a = DebRecvLedger.objects.all().count()
    if a > 0:
        l = DebRecvLedger.objects.latest('deb_recv_ledger_id')


        a = Accounts.objects.get(customers_cust=l.customers_customers)
        cust = get_object_or_404(Customers, cust_name=a.accounts_name)
        context = {
        'l':l, 'ac':a,
        'cust':cust
        }
        return render(request,'debt/debt_bill.html',context)
    else:
        return redirect('dsnot')


def search_page_debt_bill(request):
    return render(request,'debt/search_bill.html')


def find_debt_recipt_for_debt(request,id):
    l = get_object_or_404(DebRecvLedger,deb_recv_ledger_id=id)

    a = Accounts.objects.get(customers_cust=l.customers_customers)
    context = {
        'l':l, 'ac':a
    }
    return render(request,'debt/debt_bill.html',context)

def find_payment_recipt(request,id):
    l = get_object_or_404(PayLed,pay_led_id=id)

    a = Accounts.objects.get(customers_cust=l.customers_customers)
    context = {
        'l':l, 'ac':a
    }
    return render(request,'payment/payrecipt.html',context)


def search_page_pay_bill(request):
    return render(request,'payment/search_bill.html')


def payment_recipt(request):
    l = PayLed.objects.latest('pay_led_id')

    a = Accounts.objects.get(customers_cust=l.customers_customers)
    context = {
        'l':l, 'ac':a
    }
    return render(request,'payment/payrecipt.html',context)

@csrf_exempt
def add_pur(request):
    if request.method == 'POST':
        pro = request.POST.getlist('pn')
        chr = request.POST.getlist('cr')
        per = request.POST.getlist('percent')
        rp = request.POST.getlist('rp')
        qty = request.POST.getlist('qty')
        ec = request.POST.getlist('ecod')
        tt = request.POST.getlist('tt')

        a = Purchase.objects.create(com_name='China')

        for x in range(len(pro)):
            b = PurchaseDetails.objects.create(pro_name=pro[x], qty=int(qty[x]), p_p=float(chr[x]), r_p=rp[x], dat=date.today(),purchase_purchase=a,total=float(tt[x]),ec=ec[x],dis=float(per[x]))

        return  JsonResponse({})
    else:
        return render(request,'purchase/add_purchase.html')



def add_parts(request):
    p = Parts.objects.all()
    form = PartsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return  redirect('addprts')
    else:
        return render(request,'parts/add_parts.html',{'form':form, 'p':p})



def add_mani_pro(request):
    p = ManiPro.objects.all()
    form = ManiProForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        a = form.cleaned_data['name']
        t = int(form.cleaned_data['qty'])
        g = get_object_or_404(Products, name=a)
        g.qty = int(g.qty) + t
        g.save()

        for y in Parts.objects.all():
            y.qty = y.qty - int(t)
            y.save()

        form.save()
        return  redirect('addpani')
    else:
        return render(request,'manipro/add.html',{'form':form, 'p':p})



@csrf_exempt
def add_sales_return_page(request):
    allpro = Products.objects.all()
    all_cust = Customers.objects.all()

    if request.method == 'POST':
        print(request.POST)

        cust = request.POST.getlist('cust')[0]
        pro = request.POST.getlist('pro')
        price = request.POST.getlist('price')
        qty = request.POST.getlist('qty')
        dis = request.POST.getlist('dis')
        amt = request.POST.getlist('price')
        net_total = request.POST.getlist('net_total')[0]
        paid = request.POST.getlist('paid')[0]
        due = request.POST.getlist('due')[0]
        ecode = request.POST.getlist('Ecode')


        b = Salesreturn.objects.create(customer_name=cust,order_date=date.today(),net_total = float(net_total),
                                 paid = float(paid), due=round(float(due),2))

# t - ((t * dis)/100)

        for x in range(len(pro)):
            f = int(price[x]) * int(qty[x])
            ff = f - (f * int(dis[x])/100)

            sd = Salesreturndetail.objects.create(product_name= pro[x], price = amt[x], qty=qty[x],
                                            total= float(ff), salesreturn_salereturn = b, dis=dis[x],ecode=ecode[x])

            p = get_object_or_404(Products, name=pro[x])
            p.qty = p.qty + int(qty[x])
            p.save()



        owner = Accounts.objects.get(accounts_name='Mr Sun')
        owner.credit = owner.credit - float(paid)
        owner.save()

        cust = Accounts.objects.get(accounts_name=cust)
        cust.var = cust.debit

        cust.debit = cust.debit - float(due)
        cust.save()




    context = {'all_pus': allpro, 'all_cust': all_cust}
    return render(request, 'orders/old/orders.html', context)



@csrf_exempt
def gen_pdf_for_sales_return(request):
    a = Salesreturn.objects.latest('salesreturn_id')
    cacc = Accounts.objects.get(accounts_name=a.customer_name)
    custt = get_object_or_404(Customers, cust_name=a.customer_name)


    b = Salesreturndetail.objects.filter(salesreturn_salereturn=a)
    return render(request, 'sales/sales_return.html', {'aa': a, 'bb': b, 'cact': cacc, 'c':custt})


def add_account(request, id):
    acc = get_object_or_404(Accounts, accounts_id=id)

    f = AccountsForm(request.POST or None, instance=acc)
    if f.is_valid():
        f.save()
        return redirect('allacc')

    return render(request, 'allaccounts/add_account.html', {'form': f})

@csrf_exempt
def give_sal_to_emp(request):
    emps = Employees.objects.all()
    if request.method == 'POST':
        c = request.POST.getlist('comn')[0]
        amt = request.POST.getlist('amount')[0]
        dt = request.POST.getlist('dt')[0]
        descrp = request.POST.getlist('des')[0]
        m = request.POST.getlist('method')[0]


        empacc = get_object_or_404(EmpAccounts,emp_account_name=c)
        empacc.emp_accounts_credit = float(empacc.emp_accounts_credit) + float(amt)
        empacc.save()
        acc = get_object_or_404(Accounts, accounts_name='Mr Sun')
        acc.credit = float(acc.credit) - float(amt)
        acc.save()

        sal = SalDetails.objects.create(emp_name=c, amount=float(amt), desc=descrp, method=m, dat=dt)

        return JsonResponse({})

    else:
        return render(request, 'employess/sal.html',{'acc':emps})


#-----------------------ledger of Paid Debts-------------------------
def salary_details(request):
    l = SalDetails.objects.all()

    return render(request,'employess/saldetails.html',{'leg':l})


def add_pur_row(request):

    htmlf = render_to_string('purchase/newrow.html', request=request)
    return JsonResponse({'htmlf': htmlf})


@csrf_exempt
def gen_pdf_for_pur(request):
    a = Purchase.objects.latest('purchase_id')
    b = PurchaseDetails.objects.filter(purchase_purchase=a)
    c = PurchaseDetails.objects.filter(purchase_purchase=a).aggregate(Sum('total'))
    cd = round(c['total__sum'],2)
    return render(request, 'purchase/pur_report.html', {'aa': a, 'bb': b,'cc':cd})


def fetch_all_pur_report(request):
    return render(request, 'purchase/bills.html')


def search_pur_bill(request, id):
    a = Purchase.objects.get(purchase_id=id)
    b = PurchaseDetails.objects.filter(purchase_purchase=a)
    c = PurchaseDetails.objects.filter(purchase_purchase=a).aggregate(Sum('total'))
    cd = round(c['total__sum'],2)
    return render(request, 'purchase/pur_report.html', {'aa': a, 'bb': b,'cc':cd})

# # ----------- All Company & All Products in Stock Form --------------------
# def fetch_com_pro_for_stock(request):
#     all_com = Customers.objects.all()
#     all_pus = Products.objects.filter(company_company__in=Subquery(all_com.values('company_id')))
#     return render(request, 'stock/add_stock_detail_fp.html', {'all_pus': all_pus, 'all_com': all_com})
#
#
# @csrf_exempt
# def save_stock_detail_form(request):
#     if request.method == 'POST':
#
#         com = request.POST.getlist('com')
#         ncom = str(com[0])
#
#         bilno = request.POST.getlist('billno')
#         nbilno = int(bilno[0])
#
#         blty = request.POST.getlist('builtyno')
#         nbltyno = int(blty[0])
#
#         bexp = request.POST.getlist('expense')
#         nexp = float(bexp[0])
#
#         total_bill = request.POST.getlist('bamt')
#         ntotalbill = float(total_bill[0])
#
#         dt = request.POST.getlist('dt')
#         stock_date = str(dt[0])
#
#         sta = request.POST.getlist('sta')
#         status = str(sta[0])
#
#         tn = request.POST.getlist('tn')
#         tn = tn[0]
#
#         #------------- upper stock form data collected-----------------------
#
#
#         pro = request.POST.getlist('pro')
#         pprice = request.POST.getlist('pprice')
#         rprice = request.POST.getlist('rprice')
#
#         qty = request.POST.getlist('qty')
#         unt = request.POST.getlist('unit')
#
#
#         bval = request.POST.getlist('bxv')
#
#         total_pro_price = 0
#         for p in pprice:
#             total_pro_price += float(p)
#
#         # ---------------Stock & Company----------------
#
#         c = Customers.objects.get(cust_name=ncom)
#         s = Stock()
#         s.company_company = c
#         s.bill_no = nbilno
#         s.buity_no = nbltyno
#         s.exp = nexp
#
#         s.date = stock_date
#         s.total_bill = ntotalbill
#         s.status = status
#         s.save()
#
#         # builty exp and pp
#         p_vd_exp = []
#
#         for x in range(len(pro)):
#             # ----------Product----------------------------
#             p = Products.objects.get(products_name=pro[x])
#
#             a = round(nexp * float(pprice[x]), 2)
#             print('a is: ',a)
#             b = round(a / total_pro_price, 2)
#             c = round(b / float(qty[0]), 2)
#
#             p_vd_exp.append(c)
#
#             # -----------Stock Detail----------------
#             sd = StockDetails()
#             sd.stock_st = s
#             sd.product_name = pro[x]
#
#             sd.puchase_price = float(pprice[x]) + float(p_vd_exp[x])
#             sd.retail_price = float(rprice[x]) + float(p_vd_exp[x])
#             sd.qty = int(qty[x])
#
#             if unt[x] == 'dozen':
#                 print('yes i am inside dozen')
#
#                 nps = int(sd.qty) * 12
#                 p.products_stock = p.products_stock + nps
#                 p.purchase_price = float(pprice[x])
#                 p.purchase_price = round(p.purchase_price + p_vd_exp[x] / 12, 2)
#
#                 p.retail_price = float(rprice[x])
#                 p.retail_price = round(p.retail_price + p_vd_exp[x] / 12, 2)
#
#                 sd.unit = unt[x]
#                 sd.products_products = p
#                 sd.save()
#                 p.unit = unt[x]
#                 p.save()
#
#
#
#             elif unt[x] == 'box':
#                 print('yes i m inside box')
#
#                 sd.stock_st = s
#                 sd.product_name = pro[x]
#                 bxv = int(bval[x])
#                 nps = int(qty[x]) * int(bxv)
#
#                 p.products_stock = nps
#                 pp = float(pprice[x])
#                 ppp = pp + p_vd_exp[x]
#                 p.purchase_price = ppp / nps
#
#                 rp = float(rprice[x])
#                 rpp = rp + p_vd_exp[x]
#                 p.retail_price = rpp / nps
#
#                 sd.products_products = p
#                 p.boxval = int(bxv)
#                 p.unit = unt[x]
#                 p.date = str(dt[0])
#
#                 sd.puchase_price = round(pp + p_vd_exp[x], 2)
#                 p.retail_price = round(rp + p_vd_exp[x], 2)
#                 sd.retail_price = round(rp + p_vd_exp[x], 2)
#
#                 sd.qty = int(qty[x])
#                 sd.unit = unt[x]
#                 sd.dat = str(dt[0])
#
#                 p.save()
#                 sd.save()
#
#
#
#
#
#
#
#             else:
#                 print('here in else part')
#
#                 t = float(pprice[x])
#                 p.purchase_price = t + p_vd_exp[x]
#                 tt = float(rprice[x])
#                 p.retail_price = round(tt + p_vd_exp[x], 2)
#
#                 p.products_stock = int(p.products_stock) + int(sd.qty)
#                 sd.products_products = p
#                 p.save()
#                 sd.save()
#
#         acc = Accounts.objects.get(accounts_name=tn)
#         acc.credit_amount = float(acc.credit_amount) + float(nexp)
#         acc.save()
#         print('noor khan updated')
#
#         # Builty Dues Added to babak
#         acc = Accounts.objects.get(accounts_name=ncom)
#         acc.credit_amount = float(acc.credit_amount) + float(ntotalbill)
#         acc.save()
#         print(ncom + 'Updates....!!!!!')
#
#         acc = Accounts.objects.get(accounts_name='babak')
#         acc.credit_amount = float(acc.credit_amount) - float(nexp)
#         acc.save()
#         print('babak debit')
#
#
#
#         print('trans done in else')
#
#
#
#
#         print('everything went okay.....')
#     return render(request, 'stock/add_stock_detail_fp.html')