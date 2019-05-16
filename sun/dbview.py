from django.db import models

class Empview(models.Model):
    employees_id = models.IntegerField(primary_key=True)
    employees_name = models.CharField(max_length=45, blank=True, null=True)
    employees_job_title = models.CharField(max_length=45, blank=True, null=True)
    employees_salary = models.IntegerField(blank=True, null=True)
    emp_accounts_credit = models.FloatField(blank=True, null=True)
    emp_accounts_debit = models.FloatField(blank=True, null=True)
    employees_status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'empview'


class SalesDef(models.Model):
    sales_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=45, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    paid = models.FloatField(blank=True, null=True)
    due = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_def'


class StockSDetail(models.Model):
    buity_no = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    puchase_price = models.FloatField(blank=True, null=True)
    retail_price = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'stock_s_detail'
