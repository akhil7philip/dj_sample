from __future__ import absolute_import, unicode_literals
from email import header
import hashlib
import json
import re
import time
from datetime import datetime
from email.utils import parseaddr

import logging
logger = logging.getLogger(__name__)

import gspread
import pandas as pd
import numpy as np
import pytz
from celery import shared_task
from django.conf import settings
from django.db.models import Count
from django.forms.models import model_to_dict
from gspread.exceptions import GSpreadException
from proj.celery import single_instance_task
from .models import SalesOneModel, SalesTwoModel

ourtimezone = pytz.timezone(settings.TIME_ZONE)
utctimezone = pytz.timezone("UTC")

gc, authorized_user = gspread.oauth_from_dict(settings.GOOGLE_CREDENTIALS, settings.GOOGLE_AUTHORIZED_USER)


'''
gsheet_name:    Sales Summary
url:            ...
sheet_name:     ...
'''
@shared_task
def fetch_sales_summary_records():
    
    logger.info("Starting to fetch records sales summary gsheet")
    start_time                  = time.perf_counter()

    try:
        df = open_gsheet_v2(
            sheet_id='...',
            sheet_name='Form Responses 1!A:AS')
        logger.info("Parsing sheet now")
        
        values = parse_func(
            df, 
            df_cols         = ['timestamp'],
            email_cols      = ['mail_id'],
            phone_cols      = ['contact_no','alternate_customer_contact_no'],
            date_cols       = ['date'],
            time_cols       = ['time'],
            datetime_cols   = ['timestamp']
            )
        logger.info("successfully parsed sheet")
        
        # save records
        result = save_func_v3(SalesOneModel, values, start_time)
        logger.info(result)

        # update dashboard and send email notification
        if get_current_env() == 'PROD':
            update_gsheet_v3(SalesOneModel._meta.db_table,'SUCCESS',result)

    except Exception as e:
        logger.error(e)
        # update dashboard and send email notification
        if get_current_env() == 'PROD':
            update_gsheet_v3(SalesOneModel._meta.db_table,'FAILED',e)
        return False
    
    return result

def fetch_summer_sales_records():
    pass

def fetch_fall_sales_records():
    pass

def fetch_winter_sales_records():
    pass

