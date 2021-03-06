# Generated by Django 2.2 on 2020-07-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('discount_price', models.IntegerField()),
                ('final_price', models.IntegerField()),
                ('product_desc', models.TextField()),
                ('category', models.CharField(choices=[('S', 'SmartPhone'), ('L', 'Laptop'), ('D', 'Desktop'), ('W', 'Watch'), ('H', 'HeadPhone'), ('T', 'Telivision'), ('C', 'Camera')], max_length=2)),
                ('availabily', models.CharField(blank=True, choices=[('S', 'In Stock'), ('0', 'Out Of Range')], max_length=1, null=True)),
                ('product_img1', models.ImageField(upload_to='Images')),
                ('product_img2', models.ImageField(upload_to='Images')),
            ],
        ),
    ]
