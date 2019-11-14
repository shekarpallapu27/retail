from django.shortcuts import render
from .serializers import *
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProductDetails,AmazonProduct


from datetime import datetime
import os
import csv 
import bs4
from urllib.request import Request, urlopen
import sqlite3

path = os.getcwd()
retail_path  = path+'/data/'+'CG_SP_Placement_41.csv'
def executedata(request): 
    try:
        with open(retail_path) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter=',') 
            line_count = 0 
            for row in csv_reader: 
                if line_count == 0: 
                    print('Column names are', ", ".join(row)) 
                    line_count += 1 
                else: 
                    date_str_obj = row[0]
                    date_str_fmt='%b %d, %Y'
                    date_obj = datetime.strptime(date_str_obj,date_str_fmt)
                    prod_obj = ProductDetails.objects.create(
                                            date = date_obj,
                                            portfolio_name = row[1],
                                            currency = row[2],
                                            campaign_name = row[3],
                                            bidding_strategy = row[4],
                                            placement = row[5],
                                            impressions = row[6],
                                            clicks = row[7],
                                            cost_per_click = row[8],
                                            spend = row[9],
                                            day7_total_sales = row[10],
                                            total_advertising_cost_of_sales = row[11],
                                            total_return_on_advertising_spend = row[12],
                                            day7_total_orders = row[13],
                                            day7_total_units = row[14])
        return HttpResponse("Executed Successfully")
    except:
        return HttpResponse("Failed")





def webscrapdeatails(request):
    try:
        req = Request("https://www.amazon.com/dp/B01H8J9ULK", headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
        res = urlopen(req).read()
        soup = bs4.BeautifulSoup(res,'lxml')
        res1 = []
        res2 =[]
        cnt = 0 
        for i in soup.findAll('div',attrs={'class':'content'}):
            for j in i.findAll('li'):
                res1.append(j.text.split(':')[0].strip())
                res2.append(j.text.split(':')[1].strip().replace('\n',''))

                cnt += 1
                if cnt > 6:
                    break
        amz_prod_obj = AmazonProduct.objects.create(
                        product_dimensions = res2[0],
                        shipping_weight = res2[1],
                        domestic_shipping = res2[2],
                        international_shipping = res2[3],
                        asin = res2[4],
                        upc = res2[5],
                        average_customer_review = res2[6])
        return JsonResponse({"status":"Stored the product details successfully"})
    except:
        return JsonResponse({"status":"Failed"})



def updateproduct(request):
    try:
        path = os.getcwd()+'/db.sqlite3'
        conn = sqlite3.connect(path)
        db = conn.cursor()
        update_sql1 = """UPDATE product_productdetails SET currency='USDDD' WHERE prodct_id=1 """
        db.execute(update_sql1)
        conn.commit()
        conn.close()
        return HttpResponse("Updated Successfully")
    except:
        return HttpResponse("Failed to update the table")



class Product(APIView):
    def get(self,request):
        # import ipdb;ipdb.set_trace()
        try:
            p_id = request.GET.get('product_id')
            if p_id:
                prod_obj = ProductDetails.objects.filter(pk=p_id)
            else:
                prod_obj = ProductDetails.objects.all()
            obj = ProductSerializer(prod_obj,many=True)
            return Response(obj.data)
        except:
            return Response("failed")


class AmazonProductDetails(APIView):
    def get(self,request):
        # import ipdb;ipdb.set_trace()
        try:
            amz_prod_obj = AmazonProduct.objects.all()
            obj = AmazonSerializer(amz_prod_obj,many=True)
            return Response(obj.data)
        except:
            return Response("failed")