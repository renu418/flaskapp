import smtplib
import base64
import random

charlist = "qwertyuioplkjhgfdsazxcvbnm1234567890!@#$%^&*()PLMNKOIHVGYTFCXDRESZAQW"
passwd_len = 10

def send_mail(username, reciever_email):
    rand_passwd = ''
    for c in range(passwd_len):
        rand_passwd += random.choice(charlist)
    print("++++++++++++++++Password+++++", rand_passwd)
    sender_email = "mahawargupta.rajat@gmail.com"
    sender_passwd = "__c0dingislife"
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.ehlo()
        mail.login(sender_email, sender_passwd)
        body = "Dear "+username+" Your Login Details are as Follow\nEmail : "+reciever_email+"\nPassword : "+rand_passwd
        mail.sendmail(sender_email, reciever_email, body)
        print("______________________MAIL SENT________________________")
        return (rand_passwd)
    except:
        print("______________________MAIL NOT SENT________________________")
