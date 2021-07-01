# Generated by Django 3.2.3 on 2021-06-30 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_para1', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_para', models.CharField(max_length=150)),
                ('Blog_date', models.DateTimeField()),
                ('Blog_img', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_first_name', models.CharField(max_length=50)),
                ('Customer_Last_Name', models.CharField(max_length=50)),
                ('Customer_Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Contact_Number', models.CharField(max_length=50)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_payment', models.IntegerField()),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_FirstName', models.CharField(max_length=50)),
                ('distributor_Last_Name', models.CharField(max_length=50)),
                ('distributor_Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='distributor_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_Company_Name', models.CharField(max_length=60)),
                ('distributor_Company_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='distributor_Company_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_Company_Product_Name', models.CharField(max_length=50)),
                ('distributor_Company_Product_Min_Quantity', models.CharField(max_length=50)),
                ('distributor_Company_Product_Expected_Deivery', models.CharField(max_length=50)),
                ('distributor_Company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.distributor_company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_First_Name', models.CharField(max_length=50)),
                ('Employee_Last_Name', models.CharField(max_length=50)),
                ('Employee_Email', models.EmailField(max_length=254)),
                ('Employee_Type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Professional_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Experince', models.CharField(max_length=50)),
                ('Job_description', models.CharField(max_length=50)),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='mukarram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Our_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Our_Product_Name', models.CharField(max_length=50)),
                ('Our_Product_Price', models.IntegerField()),
                ('Our_Product_Discount', models.IntegerField()),
                ('Our_Product_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('Description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('Description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purchase_Date_Time', models.DateTimeField()),
                ('Distributor_Company_Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.distributor_company_product')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Recieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purchase_Recieve_Date', models.DateField()),
                ('Purchase_recieve_Bill', models.IntegerField()),
                ('Purchase_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.purchase')),
            ],
        ),
        migrations.CreateModel(
            name='req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='term_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_para', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='test_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_para', models.CharField(max_length=150)),
                ('test_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vechicle_Type', models.CharField(max_length=50)),
                ('Vehicle_Date', models.DateField()),
                ('Vechicle_Under', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity_in_stock', models.IntegerField()),
                ('Stock_Date', models.DateField()),
                ('Purchase_Recieve_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.purchase_recieve')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Schedule_Name', models.CharField(max_length=50)),
                ('Vehicle_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sale_Quantity', models.IntegerField()),
                ('Sale_Bill', models.IntegerField()),
                ('Sale_Date', models.DateField()),
                ('Customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('Product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.our_product')),
                ('Sale_By_Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity_in_number', models.IntegerField()),
                ('Qunatit_in_litter', models.IntegerField()),
                ('Quantity_in_kg', models.IntegerField()),
                ('Purchase_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.purchase')),
            ],
        ),
        migrations.CreateModel(
            name='payment_installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recieve_amount', models.IntegerField()),
                ('remaining_amount', models.IntegerField()),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer_payment')),
            ],
        ),
        migrations.CreateModel(
            name='orderel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('quan', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.req')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_date_time', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users_name')),
            ],
        ),
        migrations.CreateModel(
            name='Empty_Recieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empty_recieve', models.IntegerField()),
                ('Empty_remaining', models.IntegerField()),
                ('Sale_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sale')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_Name', models.CharField(max_length=50)),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee_professional_details')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salary_Ammount', models.IntegerField()),
                ('Advance_Salary', models.IntegerField()),
                ('Paid', models.IntegerField()),
                ('Remaining', models.IntegerField()),
                ('Salary_Date', models.DateField()),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Previous_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Previous_job', models.CharField(max_length=50)),
                ('Previous_job_duration', models.CharField(max_length=50)),
                ('Previous_job_Company', models.CharField(max_length=50)),
                ('Reason_to_left_old_job', models.CharField(max_length=50)),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_CNIC', models.CharField(max_length=50)),
                ('Employee_DOB', models.DateField()),
                ('Employee_Age', models.CharField(max_length=50)),
                ('Employee_Education', models.CharField(max_length=100)),
                ('Employee_Can_Drive', models.CharField(max_length=20)),
                ('Employee_House_Number', models.CharField(max_length=50)),
                ('Employee_Street', models.CharField(max_length=50)),
                ('Employee_Town', models.CharField(max_length=50)),
                ('Employee_City', models.CharField(max_length=50)),
                ('Employee_Country', models.CharField(max_length=60)),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Login_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(max_length=50)),
                ('Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Contact_Numeber', models.CharField(max_length=50)),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee_personal')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='distributor_professional_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_Office_Address', models.CharField(max_length=100)),
                ('distributor_Office_Contact', models.CharField(max_length=30)),
                ('distributor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='distributor_personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_CNIC', models.IntegerField()),
                ('distributor_DOB', models.DateField()),
                ('distributor_House_Number', models.IntegerField()),
                ('distributor_Street', models.CharField(max_length=100)),
                ('distributor_Town', models.CharField(max_length=100)),
                ('distributor_City', models.CharField(max_length=100)),
                ('distributor_Country', models.CharField(max_length=100)),
                ('distributor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.distributor')),
            ],
        ),
        migrations.CreateModel(
            name='Distributor_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_recieve', models.IntegerField()),
                ('remaining_amount', models.IntegerField()),
                ('Purchase_Recieve_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.purchase_recieve')),
            ],
        ),
        migrations.CreateModel(
            name='distributor_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_Contact_Number', models.CharField(max_length=30)),
                ('distributor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.distributor')),
            ],
        ),
        migrations.AddField(
            model_name='distributor_company',
            name='distributor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.distributor_professional_details'),
        ),
        migrations.CreateModel(
            name='Customer_professional_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_profession', models.CharField(max_length=60)),
                ('Customer_Office_Address', models.CharField(max_length=50)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer_contact')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_CNIC', models.IntegerField()),
                ('Customer_DOB', models.DateField()),
                ('Customer_age', models.IntegerField()),
                ('Customer_House_Number', models.IntegerField()),
                ('Customer_Street', models.CharField(max_length=50)),
                ('Customer_Town', models.CharField(max_length=50)),
                ('Customer_City', models.IntegerField()),
                ('Customer_Country', models.CharField(max_length=50)),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]