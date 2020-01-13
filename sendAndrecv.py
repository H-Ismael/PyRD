# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:24:31 2019

@author: -
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:00:22 2019

@author: -
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#********************************************************************************************
import imaplib
import email
import os
#********************************************************************************************
#cmd = ""


def cmdreceiver(sender,title):
    cmd = "compile"
    svdir = 'C:\\Users\\*******\\Desktop\\*****\\p**yyremote**\\ExchangeFolder\\ToReceive'
    imap_host = 'imap.yandex.com'
    imap_user = '****.**********@yandex.com'
    imap_pass = '***'
    global fileName
    # connect to host using SSL
    imap = imaplib.IMAP4_SSL(imap_host)
    
    ## login to server
    imap.login(imap_user, imap_pass)
    
    
    imap.select('Inbox')
    
    #sender= '(FROM "******")'
    #title = '(SUBJECT "00000 hello imap 000000")'
    
    tmp, data = imap.search(None, sender,title)
    #tmpS, dataS = imap.search(None, '(SUBJECT "interprete")')
    
    for num in data[0].split():
        #imap.recent()
        tmp, data = imap.fetch(num, '(RFC822)')
    
        body = data[0][1]
        
        #attach= data[1][0]
        #attachContent = 
        #msg = email.message_from_string(body.decode('utf-8'))
        msg = email.message_from_string(body.decode('utf-8'))
        #msg1 = email.message_from_binary_file(attach)
        content = msg.get_payload(decode=True)
        #content1 = msg1.get_payload()
        
        #if msg.get_content_maintype() != 'multipart':
            #continue
        
        
        
    for part in msg.walk():
        if part.get_content_maintype() == 'text':
            
            if part.get_payload(decode=True).decode('utf-8').find(cmd) != -1 :
                
                print("found cmd")
                print(part.get_payload(decode=True).decode('utf-8'))
                
                global statusfindcmd 
                statusfindcmd=True
                
            else:
                print("did not found compile cmd")
                statusfindcmd = False
                print(part.get_payload(decode=True).decode('utf-8'))
        #print (part.get_content_type())
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        
        global fileName
        fileName = part.get_filename()
        
        print("found file name")
        if bool(fileName):
            filePath = os.path.join(svdir, fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                global statusfindfile
                statusfindfile = True
                
                
                
    #imap.close()
    #imap.logout()
    
    
#******************************************************************************************

#cmdreceiver('(FROM "****")','(SUBJECT "owl")')
#print(statusfindcmd)
#*******************************************************************************************
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:13:21 2019

"""



def sendfct():
    
    fromaddr = "****.******@sandboxe016c6aac4c14ff2b64338e6efc5f29e.mailgun.org"
    toaddr = "****.*******@yandex.com"
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE EMAIL"
    
    body = "TEXT YOU WANT TO SEND"
    
    msg.attach(MIMEText(body, 'plain'))
    execpath="C:/*****/*******/Desktop/*****/***pyyremote***/ExchangeFolder/ToSend/"

    fllpth=[]
    for root, dirs, files in os.walk(os.path.abspath(execpath)):
        for file in files:
            fullpathz =os.path.join(root, file) 
            fllpth.append(fullpathz)
            #print(fullpathz)
            
    #print(fllpth)
    
    for file in fllpth :
        filename = file
        attachment = open(file, "rb")
        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
    
    
    server = smtplib.SMTP('smtp.mailgun.org', 587)
    server.starttls()
    server.login("postmaster@sandboxe016c6aac4c14f***efc5f29e.mailgun.org", "*************-6140***2-6b254*b")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

