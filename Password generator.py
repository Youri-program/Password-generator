import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!$%&'()*/;?@[]_{\}"
lengthpassword = 16 

all = lowercase + uppercase + numbers + symbols 

password = "".join(random.sample(all,lengthpassword))
print(f"The generated password is:  {password}")