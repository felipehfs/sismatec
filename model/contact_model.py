import datetime

class Contact(object):
    """
    Contact entity class
    """

    def __init__(self, name, email, birthday, code=None):
        self.name = name
        self.email = email
        self.birthday = birthday
        self.code = code

    def __str__(self):
        return "{code}, {name}, {email}, {birthday}".format(code=self.code, name=self.name, email=self.email, birthday=self.birthday)
