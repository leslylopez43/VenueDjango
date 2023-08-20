# Generated by Django 3.2.20 on 2023-08-19 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('accommodation_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('accommodation_id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('guests', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('apartment_availability', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('accommodation_id', models.AutoField(primary_key=True, serialize=False)),
                ('weddings', models.BooleanField(default=False)),
                ('birthdays', models.BooleanField(default=False)),
                ('parties', models.BooleanField(default=False)),
                ('baby_shower', models.BooleanField(default=False)),
                ('corporate_events', models.BooleanField(default=False)),
                ('christmas', models.BooleanField(default=False)),
                ('lifestyle_photoshot', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('tenant_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('plus_18s', models.PositiveIntegerField()),
                ('under_18s', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('billing_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/default.webp', null=True, upload_to='products/'),
        ),
        migrations.CreateModel(
            name='Tenancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('sleeps', models.PositiveIntegerField()),
                ('venue_type', models.CharField(max_length=100)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.accommodation')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_details', models.CharField(max_length=100)),
                ('billing_address', models.CharField(max_length=200)),
                ('pay_with', models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], max_length=20)),
                ('add_new_card', models.BooleanField(default=False)),
                ('donate_to_charity', models.BooleanField(default=False)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('business_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('vat', models.CharField(max_length=20)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.accommodation')),
            ],
        ),
        migrations.AddField(
            model_name='accommodation',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.tenant'),
        ),
    ]
