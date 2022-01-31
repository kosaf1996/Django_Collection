from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
from .utils import get_customer_from_id, get_salesman_from_id
# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    sales_df = None
    positions_df = None
    merged_df =None

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        seal_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(seal_qs) > 0: #POST 를 받아 qs(데이터) 의길이가 0 보다 크면 아래 실행
            #pandas 데이터 프레임 생성 -> 데이터를 엑셀 형식으로 나열 해준다고 생각
            sales_df = pd.DataFrame(seal_qs.values())
            #id 값을 get_customer_from_id함수를 호출해 이름으로 치환
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(get_salesman_from_id)
            #날짜 형식 변경
            sales_df['created'] = sales_df['created'].apply(lambda x: x.strftime('%Y-%m-%d'))
            #데이터 프레임 항목 rename
            sales_df.rename({'customer_id':'customer', 'salesman_id': 'salesman', 'id': 'sales_id'}, axis=1, inplace=True)

            #positions data
            positions_data = []
            for sale in seal_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id' : pos.id,
                        'product' : pos.product.name,
                        'quantity' : pos.quantity,
                        'price' : pos.price,
                        'sales_id':pos.get_sales_id(),
                    }
                    positions_data.append(obj)

            positions_df = pd.DataFrame(positions_data)

            #두 데이터 프레임 병합
            merged_df = pd.merge(sales_df,positions_df, on='sales_id')

            # html 형식으로 변경
            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()

        else:
            print('no data')


    context = {
        'form': form,
        'sales_df': sales_df,
        'positions_df': positions_df,
        'merged_df':merged_df,
    }
    return render(request, 'sales/home.html', context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'