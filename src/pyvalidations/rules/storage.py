import os
import mimetypes


class Storage:
    """
    Validate File : mime , size , mime type
     - the field under validation must be a file
     - empty value return error unless field is under nullable validation
    """

    def __init__(self, value):
        self.value = value

    def is_file(self):
        """
          check value is file
         :return: Boolean
        """
        try:
            return os.path.isfile(self.value)
        except Exception as e:
            print(e)
            return False

    def max_size(self, target):
        """
        maximum size (Kb) of file
        :param target : number
        :return: Boolean
        """
        try:
            size = os.path.getsize(self.value) // 1024
            return size <= float(target)
        except Exception:
            return False

    def min_size(self, target):
        """
         minimum size (Kb) of file
        :param target : number
        :return: Boolean
        """
        try:
            size = os.path.getsize(self.value) // 1024
            return size >= float(target)
        except Exception:
            return False

    def mimes(self, target):
        """
        list of accepted mimes
        :param target : string
        :return: Boolean
        """
        try:
            file_extension = os.path.splitext(self.value)[1][1:].lower()
            split_mimes = target.lower().split(",")
            return file_extension in split_mimes
        except Exception:
            return False

    def mime_types(self, target):
        """
        list of accepted mime_types
        :param target : string
        :return: Boolean
        """
        try:
            split_mime_type = target.lower().split(",")
            mimetype = mimetypes.MimeTypes().guess_type(self.value)[0].lower()
            return mimetype in split_mime_type
        except Exception:
            return False
