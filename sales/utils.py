import base64
import uuid
from customers.models import Customer
from profiles.models import Profile
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
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

def get_grape():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

#chart Signal
def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    if chart_type == '#1':
        print('Bar')
        #plt.bar(data['transaction_id'],data['price'])
        sns.barplot(x='transaction_id', y='price', data=data)
    elif chart_type == '#2':
        print('Pie')
        labels = kwargs.get('labels')
        plt.pie(data=data, x='price', labels=labels)
    elif chart_type == '#3':
        print('Line')
        plt.plot(data['transaction_id'], data['price'], color='green', marker='o', linestyle='dashed')
    else:
        print('Failed......')
    plt.tight_layout()
    chart = get_grape()
    return chart
