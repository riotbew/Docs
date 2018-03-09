#!/usr/bin/python
# -*- coding: UTF-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


#sender_qq为发件人的qq号码
sender_qq = '519463349'
#pwd为qq邮箱的授权码
pwd = 'yqllksmuvlgrbjhc'
#收件人邮箱receiver
receiver= 'qcjabc@qq.com'
#邮件的正文内容
mail_content = '你好，我是来自 ，现在在进行一项用python登录qq邮箱发邮件的测试'
#邮件标题
mail_title = '邓旭东HIT 的邮件'

def send_mail(sender_qq='',pwd='',\
    receiver='',mail_title='',mail_content=''):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    send_mail(sender_qq=sender_qq,pwd=pwd,\
    receiver=receiver,mail_title=mail_title,\
    mail_content=mail_content)

