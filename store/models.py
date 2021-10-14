from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(default='placeholder.png', upload_to='products')

	@property
	def imageURL(self):
		return self.image.url

	def __str__(self):
		return self.name


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	transaction = models.CharField(max_length=100, null=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return f'Order {self.order.id}: {self.product.name} {self.quantity} units'


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=False)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	country = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)

	def __str__(self):
		return self.address
