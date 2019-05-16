from django.contrib import admin
from .models import Products,Customers,Accounts,Sales,SalesDetails,Stock,StockDetails,DebRecvLedger,PayLed,BabakLedger, EmpAccounts


admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Accounts)
admin.site.register(Sales)
admin.site.register(Stock)
admin.site.register(EmpAccounts)

