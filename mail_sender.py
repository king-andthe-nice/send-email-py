import smtplib
from email.mime.text import MIMEText
from email.header import Header

class EmailSender:
    def sendEmail(self):
        # 配置发送方信息（需要修改为你的QQ邮箱和授权码）
        sender = '3356369582@qq.com'  # 必须与登录邮箱一致
        password = 'vdraphgvsncjdaee'  # 替换为QQ邮箱的授权码
        receivers = ['1806751665@qq.com']  # 替换为接收方邮箱
        

        # 创建邮件内容
        message = MIMEText('场馆预约成功', 'plain', 'utf-8')
        message['From'] = f'{sender}'  # 简化From格式，只使用邮箱地址
        message['To'] = f'{receivers[0]}'  # 简化To格式，只使用邮箱地址
        message['Subject'] = Header('预约成功通知', 'utf-8')
        
        try:
            # 使用SSL加密连接QQ邮箱的SMTP服务器
            smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtpObj.login(sender, password)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(f"邮件发送失败，错误信息: {str(e)}")

# 使用示例
if __name__ == "__main__":
    sender = EmailSender()
    sender.sendEmail()
