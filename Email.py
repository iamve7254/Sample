import smtplib

contact="hey i am sending test email through python"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('venky7254@gmail.com','Madathala7254')
mail.sendmail('venky7254@gmail.com','sreekanthmattupalli@gmail.com',contact)
mail.close()