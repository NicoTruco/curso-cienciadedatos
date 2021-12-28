#https://docs.python.org/es/3/library/email.examples.html
#https://pythonprogramming.altervista.org/send-a-pdf-with-an-email-with-python/
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText
from email.mime.image import MIMEImage

class SendMail:
    def pruebaGmail():
        gmail_user = 'juantio@gmail.com'
        gmail_password = 'juanito'
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
        except:
            print ("Something went wrong...")

    def pruebaHarrys():
        gmail_user = 'pedrio@xx.cl'
        gmail_password = 'maria'
        try:
            server = smtplib.SMTP_SSL('mail.xx.cl', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            msg = EmailMessage()
            msg.set_content("hola contenido")
            msg['Subject'] = f'The contents of'
            msg['From'] = "harrys@harrys.cl"
            msg['To'] = "harrys@harrys.cl"

            # Send the message via our own SMTP server.
            #server = smtplib.SMTP('localhost')
            server.send_message(msg)
            server.quit()
        except:
            print ("Something went wrong...")

    def enviaMail(gmail_user,gmail_password,stTo,stTexto):
        try:
            server = smtplib.SMTP_SSL('mail.harrys.cl', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            #msg = MIMEText("""body""")
            msg = EmailMessage()
            msg.set_content(stTexto)
            msg['Subject'] = f'The contents of'
            msg['From'] = gmail_user
            msg['To'] = stTo
            #msg['Cc'] = ', '.join(cc)
            #msg['Bcc'] = ', '.join(bcc)

            """
            with open("D:/Trabajo_Python/empresa/certfificado.pdf", 'rb') as fp:
                msg.add_attachment(fp.read()
                             , maintype='image'
                             , subtype=imghdr.what(None, img_data)
                             )
            """
            #msg = MIMEMultipart()
            #msg.attach(MIMEText(open("D:/Trabajo_Python/empresa/certfificado.pdf").read()))
            # Send the message via our own SMTP server.
            #server = smtplib.SMTP('localhost')
            server.send_message(msg)
            server.quit()
        except UnAcceptedValueError as e:
            print ("Something went wrong...",e.data)

class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)



SendMail.enviaMail("harrys@gmail.com","clave","juanto@gmail.com , josega@gmail.com ","texo")        
