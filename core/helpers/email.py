import urllib.request

import os
from rest_framework import generics
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from rest_framework.utils import json
from rest_framework.response import Response
from datetime import datetime
from datetime import date

WELCOME = 'welcome'

class Email:
    def __init__(self, types, to, data=None, id=None):
        self.type = types
        self.data = data

        self.subject = None
        self.text_content = None
        self.from_email = 'gar_vicky93@hotmail.com'
        self.to = to
        self.cc = None
        self.html_content = None


        if self.type == WELCOME:
            self.subject = 'Bienvenida(o)'
            self.text_content = self.subject

            html_client = get_template('welcome.html')
            self.html_content = html_client.render({
                'name': self.data['name'],
                'email':self.to,
                'password': self.data['password'],
                'url': self.data['url'],
            })



    def send(self):
        msg = EmailMultiAlternatives(
            self.subject,
            self.text_content,
            self.from_email,
            [self.to]
        )
        msg.attach_alternative(self.html_content, "text/html")

        # for file in self.files:
        #     URL = file['url']
        #     if URL != None and URL != "":
        #         with urllib.request.urlopen(URL) as url:
        #             with open(str(file['name']), 'wb') as f:
        #                 f.write(url.read())
        #         msg.attach(file['name'], open(file['name'], 'rb').read(), 'application/pdf')
        #         os.remove(file['name'])

        try:
            msg.send()
            message = "Success"
            status = True
        except EmailMultiAlternatives:
            message = "Service Error"
            status = False

        return {'status': status, 'message': message}

