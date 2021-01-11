#  __  ___ __          __  __  __  ___ ___      __  __           
# |__)|__ |  \ /\ |\ ||  \/ _`|__)|__ |__ |\ | /  `/  \ |  ||__/ 
# |  \|___|__//~~\| \||__/\__>|  \|___|___| \|.\__,\__/.\__/|  \ 
#    

#pip install dnspython
import dns.resolver
import re

# 1 - check for typo in domain name
example = "test@gmail.com"
if re.search("@gm(ia|a|i)l.com$", example):
	print("did you mean gmail.com")

# 2 - check if the address is a valid format
address_to_verify = "sales@subscribetodrpi.com"
match = re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", address_to_verify)

if match == None:
	print("Bad Syntax")
	raise ValueError("Bad Syntax")

# 3 Check the MX record 
try:
	records = dns.resolver.resolve("http://subscribetodrpi.com/", 'MX')
	mx_record = records[0].exchange
	mx_record = str(mx_record)
	print(mx_record)
except:
	print("Domain doesn't exist")
