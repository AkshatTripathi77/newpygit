class Emailservice:
     def _connect(self):
         print('Connecting to server......')
     def _authenticate(self):
         print("Authenticating.........")
     def sendEmail(self):
         self._connect()
         self._authenticate()
         print("Sending E-mail.........")
         self._disconnect()
     def _disconnect(self):
         print("Disconnecting with server......")
email = Emailservice()
email.sendEmail()

