# pyEmail邮件处理


import smtplib
from email.mime.text import MIMEText  # 用于构建邮箱内容

msg_from = "banmafriday@126.com"  # 发件人
password = "FMFYRBYRDGMPSNXK"  # 授权码

msg_to = "294350757@qq.com"  # 收件人

# 构建邮箱内容
subject = "0414测试邮件"

content = "你中奖了！5毛钱"

msg = MIMEText(content)  # 邮件内容对象

msg["Subject"] = subject

msg["From"] = msg_from
msg["To"] = msg_to

# 发送邮件
smtpObj = smtplib.SMTP_SSL("smtp.126.com", 465)

smtpObj.login(msg_from, password)  # 登录

smtpObj.sendmail(msg_from, msg_to, str(msg))   #发送邮件
print("发送成功")
smtpObj.quit()
