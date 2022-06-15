class De:
    """
    Validation Exception message in Deutsch language
    :param attribute : name of validation target
    :param value : value of attribute
    """

    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def messages(self):
        """
        validation messages
        :return: dict
        """
        return {
            "field": f"Das {self.attribute} ist nicht vorhanden",
            "required": f"Das Feld {self.attribute} ist erforderlich.",
            "required_if": f"Das Feld {self.attribute} ist erforderlich, wenn {self.value} vorhanden ist.",
            "required_unless": f"Das Feld {self.attribute} ist erforderlich, es sei denn, {self.value} ist nicht vorhanden oder leer.",
            "required_with": f"Das Feld {self.attribute} ist erforderlich, wenn {self.value} vorhanden ist/sind.",
            "required_without": f"Das Feld {self.attribute} ist erforderlich, wenn {self.value} nicht vorhanden ist/sind.",
            "accepted": f"Das {self.attribute} muss akzeptiert werden.",
            "alpha": f"Das {self.attribute} darf nur Buchstaben enthalten.",
            "boolean": f"Das {self.attribute} darf nur einen booleschen Wert haben: true , false , 1 oder 0.",
            "string": f"Das {self.attribute} darf nur Strings enthalten.",
            "start_with": f"Das {self.attribute} darf nur mit {self.value} beginnen.",
            "end_with": f"Das {self.attribute} darf nur mit {self.value} enden.",
            "numeric": f"Das {self.attribute} muss eine Zahl sein.",
            "digits": f"Das {self.attribute} muss aus {self.value} Ziffern bestehen.",
            "max": f"Das {self.attribute} darf nicht größer als {self.value} sein.",
            "min": f"Das {self.attribute} muss mindestens {self.value} sein.",
            "email": f"Das {self.attribute} muss eine gültige E-Mail-Adresse sein.",
            "url": f"Das {self.attribute} muss eine gültige URL-Adresse sein.",
            "ip": f"Das {self.attribute} muss eine gültige IP-Adresse sein.",
            "ipv4": f"Das {self.attribute} muss eine gültige IPv4-Adresse sein.",
            "ipv6": f"The {self.attribute} must be a valid IPv6 address.",
            "in": f"Das ausgewählte {self.attribute} ist ungültig.",
            "not_in": f"Das ausgewählte {self.attribute} ist ungültig.",
            "uuid": f"Das {self.attribute} muss eine gültige UUID sein.",
            "date": f"Das {self.attribute} ist kein gültiges Datum.",
            "time": f"Das {self.attribute} ist keine gültige Zeit.",
            "datetime": f"Das {self.attribute} ist kein gültiges datetime.",
            "timezone": f"Das {self.attribute} ist keine gültige Zeitzone.",
            "date_equals": f"Das {self.attribute} muss ein Datum gleich {self.value} sein.",
            "after": f"Das {self.attribute} muss ein Datum nach {self.value} sein.",
            "after_or_equal": f"Das {self.attribute} muss ein Datum nach oder gleich {self.value} sein.",
            "before": f"Das {self.attribute} muss ein Datum vor {self.value} sein.",
            "before_or_equal": f"Das {self.attribute} muss ein Datum vor oder gleich {self.value} sein.",
            "different": f"Das {self.attribute} muss sich von {self.value} unterscheiden.",
            "equal": f"Das {self.attribute} muss gleich {self.value} sein.",
            "gt": f"Das {self.attribute} muss größer als {self.value} sein.",
            "gte": f"Das {self.attribute} muss größer oder gleich {self.value} sein.",
            "lt": f"Das {self.attribute} muss kleiner als {self.value} sein.",
            "lte": f"Das {self.attribute} muss kleiner oder gleich {self.value} sein.",
            "confirmed": f"Die {self.attribute}-Bestätigung stimmt nicht überein.",
            "nullable": f"Das {self.attribute} kann eine Null sein.",
            "file": f"Das {self.attribute} muss eine Datei sein.",
            "mimes": f"Das {self.attribute} muss eine Datei des Typs sein: {self.value}.",
            "mime_types": f"Das {self.attribute} muss eine Datei des Typs sein: {self.value}.",
            "max_size": f"Das {self.attribute} darf nicht größer als {self.value} Kilobyte sein.",
            "min_size": f"Das {self.attribute} muss mindestens {self.value} Kilobyte groß sein.",
        }
