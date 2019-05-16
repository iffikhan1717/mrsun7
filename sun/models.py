from django.db import models


class Accounts(models.Model):
    accounts_id = models.AutoField(primary_key=True)
    accounts_name = models.CharField(max_length=45, blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    bal = models.FloatField(blank=True, null=True)
    customers_cust = models.ForeignKey('Customers', models.DO_NOTHING)
    var = models.FloatField(blank=True, null=True)
    bkvar = models.FloatField(blank=True, null=True)
    opn_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.accounts_name)


    class Meta:
        managed = False
        db_table = 'Accounts'
        unique_together = (('accounts_id', 'customers_cust'),)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=45, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.cust_name)


    class Meta:
        managed = False
        db_table = 'booking'


class BookingDetails(models.Model):
    booking_details_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=55, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    amt = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    booking_booking = models.ForeignKey(Booking, models.DO_NOTHING)
    ecode = models.CharField(max_length=45, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_details'
        unique_together = (('booking_details_id', 'booking_booking'),)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class Customers(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    contact_no = models.CharField(max_length=45, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.cust_name)

    class Meta:
        managed = False
        db_table = 'customers'


class Exp(models.Model):
    exp_id = models.AutoField(primary_key=True)
    amt = models.FloatField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exp'


class ExpDetails(models.Model):
    exp_details_id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    amt = models.FloatField(blank=True, null=True)
    exp_exp = models.ForeignKey(Exp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exp_details'
        unique_together = (('exp_details_id', 'exp_exp'),)


class Products(models.Model):
    products_id = models.AutoField(db_column='Products_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    p_p = models.FloatField(blank=True, null=True)
    r_p = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    e_code = models.CharField(max_length=45, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


    class Meta:
        managed = False
        db_table = 'products'



class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    com_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase'


class PurchaseDetails(models.Model):
    purchase_details_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=55, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    p_p = models.FloatField(blank=True, null=True)
    r_p = models.FloatField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    purchase_purchase = models.ForeignKey(Purchase, models.DO_NOTHING)
    total = models.FloatField(blank=True, null=True)
    ec = models.CharField(max_length=45, blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)




    class Meta:
        managed = False
        db_table = 'purchase_details'
        unique_together = (('purchase_details_id', 'purchase_purchase'),)


class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=45, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    paid = models.FloatField(blank=True, null=True)
    due = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.sales_id )

    class Meta:
        managed = False
        db_table = 'sales'


class SalesDetails(models.Model):
    sales_details_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=55, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    sales_sales = models.ForeignKey(Sales, models.DO_NOTHING)
    dis = models.FloatField(blank=True, null=True)
    ecode = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'sales_details'
        unique_together = (('sales_details_id', 'sales_sales'),)


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    com_name = models.CharField(max_length=45, blank=True, null=True)
    bilno = models.IntegerField(blank=True, null=True)
    no_of_pro = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.stock_id)

    class Meta:
        managed = False
        db_table = 'stock'


class StockDetails(models.Model):
    stock_details_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=55, blank=True, null=True)
    p_p = models.FloatField(blank=True, null=True)
    r_p = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    stock_stock = models.ForeignKey(Stock, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_details'
        unique_together = (('stock_details_id', 'stock_stock'),)


class ProVdPpPr(models.Model):
    pro_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=45, blank=True, null=True)
    p_pp = models.FloatField(blank=True, null=True)
    p_rp = models.FloatField(blank=True, null=True)
    saled_price = models.FloatField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    sal_id = models.IntegerField(blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_vd_pp_pr'

class AccountsLedger(models.Model):
    accounts_ledger_id = models.AutoField(primary_key=True)
    given_from = models.CharField(max_length=45, blank=True, null=True)
    given_to = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(db_column='Desc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    accounts_accounts = models.ForeignKey('Accounts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_ledger'
        unique_together = (('accounts_ledger_id', 'accounts_accounts'),)


class Employees(models.Model):
    employees_id = models.AutoField(primary_key=True)
    employees_name = models.CharField(max_length=45, blank=True, null=True)
    employees_job_title = models.CharField(max_length=45, blank=True, null=True)
    employees_salary = models.IntegerField(blank=True, null=True)
    employees_status = models.CharField(max_length=45, blank=True, null=True)


    def __str__(self):
        return str(self.employees_name)

    class Meta:
        managed = False
        db_table = 'employees'


class EmpAccounts(models.Model):
    emp_accounts_id = models.AutoField(primary_key=True)
    emp_account_name = models.CharField(max_length=45, blank=True, null=True)
    emp_accounts_credit = models.FloatField(blank=True, null=True)
    emp_accounts_debit = models.FloatField(blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    employees_employees = models.ForeignKey('Employees', models.DO_NOTHING)

    def __str__(self):
        return str(self.employees_employees)

    class Meta:
        managed = False
        db_table = 'emp_accounts'
        unique_together = (('emp_accounts_id', 'employees_employees'),)


class BabakLedger(models.Model):
    babak_ledger_id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    debit_amount = models.FloatField(blank=True, null=True)
    desc = models.CharField(max_length=90, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    rmb = models.FloatField(blank=True, null=True)
    rup = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'babak_ledger'


class DebRecvLedger(models.Model):
    deb_recv_ledger_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    method = models.CharField(max_length=45, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    customers_customers = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customers_customers')

    class Meta:
        managed = False
        db_table = 'deb_recv_ledger'
        unique_together = (('deb_recv_ledger_id', 'customers_customers'),)


class PayLed(models.Model):
    pay_led_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    customers_customers = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customers_customers')
    method = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_led'
        unique_together = (('pay_led_id', 'customers_customers'),)


class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    qty = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parts'


class ManiPro(models.Model):
    mani_pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    qty = models.CharField(max_length=45, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mani_pro'



class Salesreturn(models.Model):
    salesreturn_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=45, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    paid = models.FloatField(blank=True, null=True)
    due = models.FloatField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'salesreturn'


class Salesreturndetail(models.Model):
    salesreturndetail_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    salesreturn_salereturn = models.ForeignKey(Salesreturn, models.DO_NOTHING)
    dis = models.FloatField(blank=True, null=True)
    ecode = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'salesreturndetail'
        unique_together = (('salesreturndetail_id', 'salesreturn_salereturn'),)


class SalDetails(models.Model):
    sal_details_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=45, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    method = models.CharField(max_length=45, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sal_details'


# from django.db import models
#
#
# class Accounts(models.Model):
#     accounts_id = models.AutoField(primary_key=True)
#     accounts_name = models.CharField(max_length=45, blank=True, null=True)
#     credit = models.FloatField(blank=True, null=True)
#     debit = models.FloatField(blank=True, null=True)
#     bal = models.FloatField(blank=True, null=True)
#     customers_cust = models.ForeignKey('Customers', models.DO_NOTHING)
#     var = models.FloatField(blank=True, null=True)
#     bkvar = models.FloatField(blank=True, null=True)
#     opn_date = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.accounts_name)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'Accounts'
#     #     unique_together = (('accounts_id', 'customers_cust'),)
#
#
# class Booking(models.Model):
#     booking_id = models.AutoField(primary_key=True)
#     cust_name = models.CharField(max_length=45, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.cust_name)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'booking'
#
#
# class BookingDetails(models.Model):
#     booking_details_id = models.AutoField(primary_key=True)
#     pro_name = models.CharField(max_length=55, blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     amt = models.FloatField(blank=True, null=True)
#     discount = models.FloatField(blank=True, null=True)
#     booking_booking = models.ForeignKey(Booking, models.DO_NOTHING)
#     ecode = models.CharField(max_length=45, blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'booking_details'
#     #     unique_together = (('booking_details_id', 'booking_booking'),)
#
#
# class Category(models.Model):
#     category_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'category'
#
#
# class Customers(models.Model):
#     cust_id = models.AutoField(primary_key=True)
#     cust_name = models.CharField(max_length=45, blank=True, null=True)
#     city = models.CharField(max_length=45, blank=True, null=True)
#     contact_no = models.CharField(max_length=45, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.cust_name)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'customers'
#
#
# class Exp(models.Model):
#     exp_id = models.AutoField(primary_key=True)
#     amt = models.FloatField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'exp'
#
#
# class ExpDetails(models.Model):
#     exp_details_id = models.AutoField(primary_key=True)
#     desc = models.CharField(max_length=45, blank=True, null=True)
#     amt = models.FloatField(blank=True, null=True)
#     exp_exp = models.ForeignKey(Exp, models.DO_NOTHING)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'exp_details'
#     #     unique_together = (('exp_details_id', 'exp_exp'),)
#
#
# class Products(models.Model):
#     products_id = models.AutoField(db_column='Products_id', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(max_length=45, blank=True, null=True)
#     p_p = models.FloatField(blank=True, null=True)
#     r_p = models.FloatField(blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     e_code = models.CharField(max_length=45, blank=True, null=True)
#     dt = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.name)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'products'
#
#
#
# class Purchase(models.Model):
#     purchase_id = models.AutoField(primary_key=True)
#     com_name = models.CharField(max_length=45, blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'purchase'
#
#
# class PurchaseDetails(models.Model):
#     purchase_details_id = models.AutoField(primary_key=True)
#     pro_name = models.CharField(max_length=55, blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     p_p = models.FloatField(blank=True, null=True)
#     r_p = models.FloatField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     purchase_purchase = models.ForeignKey(Purchase, models.DO_NOTHING)
#     total = models.FloatField(blank=True, null=True)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'purchase_details'
#     #     unique_together = (('purchase_details_id', 'purchase_purchase'),)
#
#
# class Sales(models.Model):
#     sales_id = models.AutoField(primary_key=True)
#     cust_name = models.CharField(max_length=45, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#     net_total = models.FloatField(blank=True, null=True)
#     paid = models.FloatField(blank=True, null=True)
#     due = models.FloatField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.sales_id )
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'sales'
#
#
# class SalesDetails(models.Model):
#     sales_details_id = models.AutoField(primary_key=True)
#     pro_name = models.CharField(max_length=55, blank=True, null=True)
#     price = models.FloatField(blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     sales_sales = models.ForeignKey(Sales, models.DO_NOTHING)
#     dis = models.FloatField(blank=True, null=True)
#     ecode = models.CharField(max_length=45, blank=True, null=True)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'sales_details'
#     #     unique_together = (('sales_details_id', 'sales_sales'),)
#
#
# class Stock(models.Model):
#     stock_id = models.AutoField(primary_key=True)
#     com_name = models.CharField(max_length=45, blank=True, null=True)
#     bilno = models.IntegerField(blank=True, null=True)
#     no_of_pro = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return str(self.stock_id)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'stock'
#
#
# class StockDetails(models.Model):
#     stock_details_id = models.AutoField(primary_key=True)
#     pro_name = models.CharField(max_length=55, blank=True, null=True)
#     p_p = models.FloatField(blank=True, null=True)
#     r_p = models.FloatField(blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     stock_stock = models.ForeignKey(Stock, models.DO_NOTHING)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'stock_details'
#     #     unique_together = (('stock_details_id', 'stock_stock'),)
#
#
# class ProVdPpPr(models.Model):
#     pro_id = models.AutoField(primary_key=True)
#     p_name = models.CharField(max_length=45, blank=True, null=True)
#     p_pp = models.FloatField(blank=True, null=True)
#     p_rp = models.FloatField(blank=True, null=True)
#     saled_price = models.FloatField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     sal_id = models.IntegerField(blank=True, null=True)
#     profit = models.IntegerField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'pro_vd_pp_pr'
#
# class AccountsLedger(models.Model):
#     accounts_ledger_id = models.AutoField(primary_key=True)
#     given_from = models.CharField(max_length=45, blank=True, null=True)
#     given_to = models.CharField(max_length=45, blank=True, null=True)
#     desc = models.CharField(db_column='Desc', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     amount = models.FloatField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     accounts_accounts = models.ForeignKey('Accounts', models.DO_NOTHING)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'accounts_ledger'
#     #     unique_together = (('accounts_ledger_id', 'accounts_accounts'),)
#
#
# class Employees(models.Model):
#     employees_id = models.AutoField(primary_key=True)
#     employees_name = models.CharField(max_length=45, blank=True, null=True)
#     employees_job_title = models.CharField(max_length=45, blank=True, null=True)
#     employees_salary = models.IntegerField(blank=True, null=True)
#     employees_status = models.CharField(max_length=45, blank=True, null=True)
#
#
#     def __str__(self):
#         return str(self.employees_name)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'employees'
#
#
# class EmpAccounts(models.Model):
#     emp_accounts_id = models.AutoField(primary_key=True)
#     emp_account_name = models.CharField(max_length=45, blank=True, null=True)
#     emp_accounts_credit = models.FloatField(blank=True, null=True)
#     emp_accounts_debit = models.FloatField(blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     employees_employees = models.ForeignKey('Employees', models.DO_NOTHING)
#
#     def __str__(self):
#         return str(self.employees_employees)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'emp_accounts'
#     #     unique_together = (('emp_accounts_id', 'employees_employees'),)
#
#
# class BabakLedger(models.Model):
#     babak_ledger_id = models.AutoField(primary_key=True)
#     name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     debit_amount = models.FloatField(blank=True, null=True)
#     desc = models.CharField(max_length=90, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     rmb = models.FloatField(blank=True, null=True)
#     rup = models.FloatField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'babak_ledger'
#
#
# class DebRecvLedger(models.Model):
#     deb_recv_ledger_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     amount = models.FloatField(blank=True, null=True)
#     desc = models.CharField(max_length=45, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#     method = models.CharField(max_length=45, blank=True, null=True)
#     debit_amount = models.FloatField(blank=True, null=True)
#     customers_customers = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customers_customers')
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'deb_recv_ledger'
#     #     unique_together = (('deb_recv_ledger_id', 'customers_customers'),)
#
#
# class PayLed(models.Model):
#     pay_led_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     amount = models.FloatField(blank=True, null=True)
#     desc = models.CharField(max_length=45, blank=True, null=True)
#     dt = models.DateField(blank=True, null=True)
#     customers_customers = models.ForeignKey('Customers', models.DO_NOTHING, db_column='customers_customers')
#     method = models.CharField(max_length=45, blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'pay_led'
#     #     unique_together = (('pay_led_id', 'customers_customers'),)
#
#
# class Parts(models.Model):
#     parts_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     qty = models.CharField(max_length=45, blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'parts'
#
#
# class ManiPro(models.Model):
#     mani_pro_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     qty = models.CharField(max_length=45, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'mani_pro'
#
#
#
# class Salesreturn(models.Model):
#     salesreturn_id = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=45, blank=True, null=True)
#     order_date = models.DateField(blank=True, null=True)
#     net_total = models.FloatField(blank=True, null=True)
#     paid = models.FloatField(blank=True, null=True)
#     due = models.FloatField(blank=True, null=True)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'salesreturn'
#
#
# class Salesreturndetail(models.Model):
#     salesreturndetail_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=45, blank=True, null=True)
#     price = models.FloatField(blank=True, null=True)
#     qty = models.IntegerField(blank=True, null=True)
#     total = models.IntegerField(blank=True, null=True)
#     salesreturn_salereturn = models.ForeignKey(Salesreturn, models.DO_NOTHING)
#     dis = models.FloatField(blank=True, null=True)
#     ecode = models.CharField(max_length=45, blank=True, null=True)
#
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'salesreturndetail'
#     #     unique_together = (('salesreturndetail_id', 'salesreturn_salereturn'),)
#
#
# class SalDetails(models.Model):
#     sal_details_id = models.AutoField(primary_key=True)
#     emp_name = models.CharField(max_length=45, blank=True, null=True)
#     amount = models.FloatField(blank=True, null=True)
#     desc = models.CharField(max_length=45, blank=True, null=True)
#     method = models.CharField(max_length=45, blank=True, null=True)
#     dat = models.DateField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'sal_details'
#
#
