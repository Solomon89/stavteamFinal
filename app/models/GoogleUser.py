

class GoogleUser:
    def __init__(self,unique_id,users_email,picture,users_name):
        """Constructor"""
        self.unique_id = unique_id
        self.users_email = users_email
        self.picture = picture
        self.users_name = users_name
        pass
    def inLineToSave(self):
        returnStr =  self.users_name + ","
        returnStr +=  self.users_email + ","
        returnStr +=  self.picture + ","
        returnStr +=  self.unique_id
        return returnStr