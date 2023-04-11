from django.db import models

# Create your models here.

class SalesOneModel (models.Model):
    timestamp                                      = models.DateTimeField(null=True, blank=True)
    customer_name                                  = models.TextField(null=True, blank=True)
    customer_no                                    = models.TextField(null=True, blank=True)
    created_at                                     = models.DateTimeField(auto_now_add=True)
    updated_at                                     = models.DateTimeField(auto_now=True)
    is_deleted                                     = models.IntegerField(default=0)
    is_deleted_at                                  = models.DateTimeField(null=True, blank=True)
    index                                          = models.IntegerField()
    hash                                           = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name            = 'Sales One Model'
        db_table                = 'sales one model'
        

class SalesTwoModel (models.Model):
    s_no                                = models.TextField(null=True, blank=True)
    service_id                          = models.TextField(null=True, blank=True)
    case_creation_date                  = models.DateField(null=True, blank=True)
    case_creation_time                  = models.TimeField(null=True, blank=True)
    created_at                          = models.DateTimeField(auto_now_add=True)
    updated_at                          = models.DateTimeField(auto_now=True)
    index                               = models.IntegerField()
    hash                                = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name            = 'Sales Two Model'
        db_table                = 'sales two model'

class SummerSalesModel (models.Model):
    pass

class WinterSalesModel (models.Model):
    pass

class FallSalesModel (models.Model):
    start_time                          = models.DateTimeField(auto_now_add=True)
    end_time                            = models.DateTimeField(auto_now=True)
    