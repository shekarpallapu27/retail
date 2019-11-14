from django.db import models

# Create your models here.



class ProductDetails(models.Model):

    prodct_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True,null=True)
    portfolio_name = models.CharField(max_length=100,blank=True,null=True)
    currency = models.CharField(max_length=100,blank=True,null=True)
    campaign_name = models.CharField(max_length=100,blank=True,null=True)
    bidding_strategy = models.CharField(max_length=100,blank=True,null=True)
    placement = models.CharField(max_length=100,blank=True,null=True)
    impressions = models.CharField(max_length=100,blank=True,null=True)
    clicks = models.CharField(max_length=100,blank=True,null=True)
    cost_per_click = models.CharField(max_length=100,blank=True,null=True)
    spend = models.CharField(max_length=100,blank=True,null=True)
    day7_total_sales = models.CharField(max_length=100,blank=True,null=True)
    total_advertising_cost_of_sales = models.CharField(max_length=100,blank=True,null=True)
    total_return_on_advertising_spend = models.CharField(max_length=100,blank=True,null=True)
    day7_total_orders = models.CharField(max_length=100,blank=True,null=True)
    day7_total_units = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.portfolio_name




class AmazonProduct(models.Model):

    amz_prod_id = models.AutoField(primary_key=True)
    product_dimensions = models.CharField(max_length=300,blank=True,null=True)
    shipping_weight = models.CharField(max_length=300,blank=True,null=True)
    domestic_shipping = models.CharField(max_length=300,blank=True,null=True)
    international_shipping = models.CharField(max_length=300,blank=True,null=True)
    asin = models.CharField(max_length=300,blank=True,null=True)
    upc = models.CharField(max_length=300,blank=True,null=True)
    average_customer_review = models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.asin
