import uuid
from customers.models import Customer
from profiles.models import Profile
#Transaction id 를 생성해주는 code
def generate_code():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code
    #code d7asdjhk22-47dfhnjk-83789-234d-gfhfghg
    #code_mode d7asdjhk2247df

def get_salesman_from_id(val): #Profile 에서 __str__값을 return 받음
    salesman =Profile.objects.get(id=val)

    return salesman.user.username

def get_customer_from_id(val): #Customer 에서 __str__ 값을 return 받음
    customer = Customer.objects.get(id=val)
    return customer