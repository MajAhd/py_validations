from datetime import datetime
import re


class DateTime:
    """
      Validate value is date/time
      :param value : string
    """

    def __init__(self, value):
        self.value = value

    def is_date(self):
        """
        check date : YY-MM-YY
        :return: bool
        """
        try:
            return re.match(r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))', self.value)
        except Exception:
            return False

    def is_time(self):
        """
        check Time : HH:MM AM , HH:MM PM , HH:MM
        :return: bool
        """
        try:
            return re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]([AaPp][Mm])?$', self.value)
        except Exception:
            return False

    def is_date_time(self):
        """
        check datetime : YY-MM-YY HH:MM
        :return: bool
        """
        try:
            return re.match(
                r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])) ([0-1]?[0-9]|2[0-3]):[0-5][0-9]$',
                self.value)
        except Exception:
            return False

    def is_timezone(self):
        """
        check timezone : +1:30 , -02:00
        :return: bool
        """
        try:
            return re.match(r'[+-][0-9]{2}:[0-9]{2}\b', self.value)
        except Exception:
            return False

    def date_equals(self, target):
        """
        check datetime : YY-MM-YY  == YY-MM-YY
        :param target: YY-MM-YY
        :return: bool
        """
        try:
            dt1 = datetime.strptime(self.value, "%Y-%M-%d")
            dt2 = datetime.strptime(target, "%Y-%M-%d")
            return dt1 == dt2
        except Exception:
            return False

    def is_after(self, target):
        """
        check datetime : YY-MM-YY  > YY-MM-YY
        :param target: YY-MM-YY
        :return: bool
        """
        try:
            dt1 = datetime.strptime(self.value, "%Y-%M-%d")
            dt2 = datetime.strptime(target, "%Y-%M-%d")
            return dt1 > dt2
        except Exception:
            return False

    def is_after_or_equal(self, target):
        """
        check datetime : YY-MM-YY  >= YY-MM-YY
        :param target: YY-MM-YY
        :return: bool
        """
        try:
            dt1 = datetime.strptime(self.value, "%Y-%M-%d")
            dt2 = datetime.strptime(target, "%Y-%M-%d")
            return dt1 >= dt2
        except Exception:
            return False

    def is_before(self, target):
        """
        check datetime : YY-MM-YY  < YY-MM-YY
        :param target: YY-MM-YY
        :return: bool
        """
        try:
            dt1 = datetime.strptime(self.value, "%Y-%M-%d")
            dt2 = datetime.strptime(target, "%Y-%M-%d")
            return dt1 < dt2
        except Exception:
            return False

    def is_before_or_equal(self, target):
        """
        check datetime : YY-MM-YY  <= YY-MM-YY
        :param target: YY-MM-YY
        :return: bool
        """
        try:
            dt1 = datetime.strptime(self.value, "%Y-%M-%d")
            dt2 = datetime.strptime(target, "%Y-%M-%d")
            return dt1 <= dt2
        except Exception:
            return False
