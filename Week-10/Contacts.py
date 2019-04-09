class Contacts:
    def __init__(self, given=None, last=None, email=None):
        self.given = given
        self.last = last
        self.email = email

    def __str__(self):
        full = None
        if self.given:
            full = self.given.__str__()

        if self.last:
            full = full + " " + self.last.__str__()

        if self.email:
            full = full + " " + self.email.__str__()

        if full:
            return full
        else:
            return "EMPTY"

    def __repr__(self):
        return self.__str__()

    def equals(self,toFind):
        return self.given == toFind or self.last == toFind or self.email == toFind