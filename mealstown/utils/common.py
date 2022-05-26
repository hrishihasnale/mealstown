import datetime,time
import calendar


def get_request_value_body(request, key, default_value):
    """
    To get passed key value from request object
    """

    if key in request.data:
        return request.data[key]

    return default_value


def get_query_param_value(request, key, default_value):
    """
    To get passed key value from request object
    """

    if key in request.GET:
        return request.GET[key]

    return default_value

def get_changed_time_from_year(year_val):
    """
    To get the DOB birth date from from current date
    """

    if year_val == '':
        return -1

    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day
    modified_year = year - year_val

    return datetime.datetime.strptime('{year}-{month}-{date}'.format(year=modified_year, month=month, date=day), "%Y-%m-%d").date()


def get_date_millis_from_string(str_value, str_format):
    return datetime.datetime.strptime(str_value, str_format).timestamp()

def get_date_from_string(str_value, str_format):
    return datetime.datetime.strptime(str_value, str_format)

def get_date_float_to_string(float_value,str_format):
    return time.strftime(str_format,time.gmtime(float_value))

def get_end_date_from_date(str_value, str_format):
    date_val = datetime.datetime.strptime(str_value, str_format)
    day = calendar.monthrange(date_val.year, date_val.month)[1]

    return datetime.datetime.strptime('{year}-{month}-{date}'.format(year=date_val.year, month=date_val.month, date=day), "%Y-%m-%d").timestamp()


def is_user_has_permission(request, module_name):
    """
    To get user accessibility for passed module
    """
    return True