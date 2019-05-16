from django.contrib import admin
from django.urls import path
from sun.views import (home, add_products, add_customers, add_booking_page, add_booking_row, get_amt_for_booking,
                       add_sales_page, get_amt_for_sales,add_sale_row,
                       gen_pdf_for_sales, gen_pdf_for_booking, add_expense,
                       add_employess, all_acc, transfer_debt_from_com_to_babak_page,babak_debit,
                       add_amount_account_page,debt_ledger, add_amount_account_page_com,
                       own_debt_ledger,
                       all_stock_report, todays_sale_report, shop_exp_report_all,shop_exp_report,
                       fetch_all_sales_report, all_sales_report,
                       find_debt_recipt_for_debt, search_page_debt_bill, debt_recipt_for_debt,                                         search_page_pay_bill, find_payment_recipt,payment_recipt,
                       add_pur,add_parts,add_mani_pro, add_sales_return_page, gen_pdf_for_sales_return, add_account,give_sal_to_emp, salary_details, add_pur_row, gen_pdf_for_pur, fetch_all_pur_report,
                       search_pur_bill)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name='hom'),




    path('add_pro/', add_products, name='adpro'),
    path('add_cust/', add_customers, name='adcust'),

    path('add_booking/', add_booking_page, name='adbk'),
    path('booking_invoice/', gen_pdf_for_booking, name='bookinginvoice'),
    path('add_new_booking_row/', add_booking_row, name='adbkrw'),
    path('amt_for_booking/<str:name>/', get_amt_for_booking, name='amtfbk'),

    path('add/sale/', add_sales_page, name='adsal'),
    path('sales_invoice/', gen_pdf_for_sales, name='saleinvoice'),
    path('amt_for_sale/<str:name>/', get_amt_for_sales, name='amtfsale'),
    path('add_new_sale_row/', add_sale_row, name='adbkrw'),

    # Add Expense
    path('add_expensess/', add_expense, name='adexp'),
    # Add Employees
    path('add_emp/', add_employess, name='addemp'),
    # All Accounts
    path('accounts/', all_acc, name='allacc'),

    #------------------babak transfer_debit page----------------------
    path('transfer_debit/', transfer_debt_from_com_to_babak_page , name='transdebpage'),
    #-------------------Babak Debit Ledger----------------------------
    path('my_debit_ledger/', babak_debit , name='bakleg'),

    # -------------- Debt Receive Update Accounts ------------------------------
    path('add_amount_page/', add_amount_account_page , name='adamtpg'),

    #-----------------debt Receive ledger--------------------------
    path('acc_ledger/', debt_ledger , name='leg'),

    # -------------- Own Debt Paying to Companies ledg ------------------------------

    path('paid_debt_ledger/', own_debt_ledger , name='paiddetail'),
    # -------------- Paying to com Update Accounts ------------------------------
    path('add_amount_page_com/', add_amount_account_page_com , name='adpycom'),

    #-----------------Reports--------------------------------------

    #-----------------all Products---------------------------------
    path('allproducts/', all_stock_report, name='alsr'),

    #---------------- Todays Sale & Stock Product Report
    path('todaysreport/', todays_sale_report, name='tdr'),

    #------------Todays Shop Exp Report and per exp report--------
    path('todays_s_exp_rep/', shop_exp_report , name='shopexpreport'),
    path('shop_all_exp/', shop_exp_report_all , name='shopexpreportall'),

    # --------- Bill Reports ------------------------------------
    path('bill/', fetch_all_sales_report, name='als'),
    path('bills/<int:id>/', all_sales_report , name='alsbil'),

    #-----------------debit Receive Invoice for--------------------------------
    path('debit_rep/', debt_recipt_for_debt , name='debtrep'),
    path('search/debt_bill/', search_page_debt_bill , name='sdb'),
    path('debit_rep/<int:id>/', find_debt_recipt_for_debt , name='debtrep'),

    #------------------ Find Payment Bill-------------------------------------
    path('payment_rep/', payment_recipt , name='payrep'),
    path('search/payment_rep/',search_page_pay_bill  , name='spb'),
    path('payment_rep/<int:id>/', find_payment_recipt , name='payrep'),


    path('add_purchase/', add_pur , name='addpur'),
    path('add_parts/', add_parts , name='addprts'),
    path('add_manipro/', add_mani_pro , name='addpani'),

    path('add/sale_return/', add_sales_return_page, name='salereutrn'),
    path('sales_invoice_return/', gen_pdf_for_sales_return, name='saleinvoicereturn'),

    path('edit_acc/<int:id>/', add_account, name='adacc'),

    path('give_salary/', give_sal_to_emp, name='gvsal'),
    path('salary_details/', salary_details, name='saldetailsemp'),

    path('add_new_pur_row/', add_pur_row , name='adpurrow'),
    path('pur_invoice/', gen_pdf_for_pur, name='purinvoicereturn'),

    path('pur_bill/', fetch_all_pur_report, name='allpurbill'),
    path('s_pur_bills/<int:id>/', search_pur_bill , name='spurbill'),
]
