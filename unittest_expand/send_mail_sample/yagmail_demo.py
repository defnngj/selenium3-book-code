import yagmail

#连接邮箱服务器
yag = yagmail.SMTP(user="sender@126.com", password="a123456", host='smtp.126.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']

# 发送邮件
yag.send('receiver@126.com', 'send email subject', contents)
