#  __  ___ __          __  __  __  ___ ___      __  __           
# |__)|__ |  \ /\ |\ ||  \/ _`|__)|__ |__ |\ | /  `/  \ |  ||__/ 
# |  \|___|__//~~\| \||__/\__>|  \|___|___| \|.\__,\__/.\__/|  \ 
#   

import re

# -----------------------------------------------------------------------------
# Look behind example ----------------------------------------------------------
# -----------------------------------------------------------------------------
# we want the number before 'etage'

property_data = "100cat 200cat 3 etage 400cat 500car 5etage"

# Find number before Etage!
m = re.search("(\d)(\s[Ee]tage)", property_data)
#print(m)
if m:
	print(m.group)(1)

# -----------------------------------------------------------------------------
# Look ahead examples ---------------------------------------------------------
# -----------------------------------------------------------------------------
# we want the vendor name and number

invoice = "Page 1 of 1  Claim NoOur ReferenceDentist's ReferencePatientDateAmount \
Vendor InformationVendor Number:223344556677Vendor Name:BUNGLE E APayment Number:95000033000\
Remittance Date:11.01.2021Pay Run Identification:XZY11\
Bank Account Number:*******3456CLAIM ACCP.O.Box 111,LONDON,0001,\
Tel: 123445678, Website:http://www.samplename.gov.zzREMITTANCE ADVICE"

# vendor name
vendor_name = re.search(r'Vendor Name:([A-Z]).+?(?=Payment)', invoice)
m = vendor_name.group().split(":")[1]
if m:
	print("Vendor Name= ", m)

# vendor number
vendor_number = re.search(r'Vendor Number:([0-9])+', invoice) 
m = vendor_number.group().split(":")[1]
if m:
	print("Vendor Number= ", m)


