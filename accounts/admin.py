from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Users_Name)
admin.site.register(login)
admin.site.register(distributor)
admin.site.register(distributor_personal)
admin.site.register(distributor_contact)
admin.site.register(distributor_professional_details)
admin.site.register(distributor_Company)
admin.site.register(distributor_Company_Product)
admin.site.register(Customer)
admin.site.register(Customer_personal)
admin.site.register(Customer_Contact)
admin.site.register(Customer_professional_details)
admin.site.register(Customer_payment)
admin.site.register(payment_installment)
admin.site.register(Employee)
admin.site.register(Employee_Personal)
admin.site.register(Employee_Contact)
admin.site.register(Employee_Previous_Details)
admin.site.register(Employee_Salary)
admin.site.register(Employee_Professional_Details)
admin.site.register(Employee_skills)
admin.site.register(Employee_attandance)
admin.site.register(Employee_Login)
admin.site.register(Employee_Login_History)
admin.site.register(Purchase)
admin.site.register(Purchase_Recieve)
admin.site.register(Distributor_Payment)
admin.site.register(Purchase_Quantity)
admin.site.register(Stock)
admin.site.register(Sale)
admin.site.register(Empty_Recieve)
admin.site.register(Vehicle)
admin.site.register(Schedule)
admin.site.register(contact)
admin.site.register(mukarram)
admin.site.register(Product)
admin.site.register(Products)
admin.site.register(test_details)
admin.site.register(about_page)
admin.site.register(term_details)
admin.site.register(Blog_details)


class OrderItemInline(admin.TabularInline):
    model = orderel
    raw_id_fields = ['order']

@admin.register(req)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    #list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]