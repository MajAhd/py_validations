import re
import ipaddress


class Internet:
    """
    Check internet Data Validation such as email , url and ip
    """

    def __init__(self, value):
        self.value = value

    def email(self):
        """
        check is email address is correct
        :return: bool
        """
        return re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.value)

    def url(self):
        """
        check url address is correct
        :return: bool
        """
        try:
            regex = ("((http|https)://)(www.)?" +
                     "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                     "{2,256}\\.[a-z]" +
                     "{2,6}\\b([-a-zA-Z0-9@:%" +
                     "._\\+~#?&//=]*)")
            p = re.compile(regex)
            if re.search(p, self.value):
                return True
            return False
        except Exception:
            return False

    def ip(self):
        """
        check IP address v4 v6 and private
        :return: bool
        """
        return self.ipv4() or self.ipv6() or self.ipv4_private()

    def ipv4(self):
        """
        check IP address v4
        :return: bool
        """
        try:
            _ip = ipaddress.IPv4Address(self.value).is_global
            return True
        except ValueError:
            return False

    def ipv4_private(self):
        """
        check IP address private
        :return: bool
        """
        try:
            _ip = ipaddress.ip_address(self.value).is_private
            return True
        except ValueError:
            return False

    def ipv6(self):
        """
        check IP address v6
        :return: bool
        """
        try:
            _ip = ipaddress.IPv6Address(self.value).is_global
            return True
        except ValueError:
            return False
