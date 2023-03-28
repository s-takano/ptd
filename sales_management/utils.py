from django.utils import timezone


from datetime import datetime


def parse_datetime(date_string1, date_string2=None):
    if date_string1 == "" or date_string1 is None:
        return None
    if date_string2 is not None:
        ret = datetime.combine(
            datetime.strptime(date_string1, "%Y/%m/%d").date(),
            datetime.strptime(date_string2, "%H:%M:%S").time())
    else:
        # if date_string1 is in format of "2022-07-07"
        if date_string1.find("-") != -1:
            ret = datetime.strptime(date_string1, "%Y-%m-%d")
        else:
            ret = datetime.strptime(
                date_string1, "%Y/%m/%d %H:%M:%S" if len(date_string1) > 10 else "%Y/%m/%d")

    return timezone.make_aware(ret)