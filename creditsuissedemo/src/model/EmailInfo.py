import Label


class Email():

    def __init__(self):
        self._salesforceId = ""
        self._createdDate = ""
        self._subject = ""
        self._textBody = ""
        self._label = ""
        self._toAddress = ""
        self._fromAddress = ""
        self._clientPresent = ""

    @property
    def salesforceId(self):
        return self._salesforceId

    @property
    def createdDate(self):
        return self._createdDate

    @property
    def subject(self):
        return self._subject

    @property
    def textBody(self):
        return self._textBody

    @property
    def label(self):
        return self._label

    @property
    def toAddress(self):
        return self._toAddress

    @property
    def fromAddress(self):
        return self._fromAddress

    @property
    def clientPresent(self):
        return self._clientPresent
        

    @salesforceId.setter
    def salesforceId(self, salesforceId):
        self._salesforceId = salesforceId

    @createdDate.setter
    def createdDate(self, createdDate):
        self._createdDate = createdDate

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @textBody.setter
    def textBody(self, textBody):
        self._textBody = textBody

    @label.setter
    def label(self, label):
        self._label = label

    @toAddress.setter
    def toAddress(self, toAddress):
        self._toAddress = toAddress

    @fromAddress.setter
    def fromAddress(self, fromAddress):
        self._fromAddress = fromAddress

    @clientPresent.setter
    def clientPresent(self, clientPresent):
        self._clientPresent = clientPresent    

class EmailInfo():
    """ Stores the Email Info for an individual """

    def __init__(self):
        self._emailInfoList = []

    def append_to_email_list(self, salesforceId, createdDate, subject, textBody, toAddress, fromAddress, first_name):
        emailObj = Email()
        emailObj.salesforceId = salesforceId
        emailObj.createdDate = createdDate
        emailObj.subject = subject
        emailObj.textBody = textBody
        emailObj.label = Label.generateLabel(textBody)
        emailObj.toAddress = toAddress
        emailObj.fromAddress = fromAddress
        
        index = textBody.lower().find(first_name.lower())
        if index != -1:
            emailObj.clientPresent = "Yes"
        else: emailObj.clientPresent = "No"

        print("Email obj: " + emailObj.clientPresent)    

        self._emailInfoList.append(emailObj)

    def get_email_list(self):
        return self._emailInfoList
