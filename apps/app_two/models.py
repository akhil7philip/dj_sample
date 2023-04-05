from django.db import models

# Create your models here.

class ProductOneModel (models.Model):
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
        verbose_name            = 'Product One Model'
        db_table                = 'product one model'
        

class ProductTwoModel (models.Model):
    s_no                                = models.TextField(null=True, blank=True)
    service_id                          = models.TextField(null=True, blank=True)
    case_creation_date                  = models.DateField(null=True, blank=True)
    case_creation_time                  = models.TimeField(null=True, blank=True)
    created_at                          = models.DateTimeField(auto_now_add=True)
    updated_at                          = models.DateTimeField(auto_now=True)
    index                               = models.IntegerField()
    hash                                = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name            = 'Product Two Model'
        db_table                = 'product two model'