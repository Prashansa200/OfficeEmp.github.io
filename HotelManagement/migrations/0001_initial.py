# Generated by Django 4.2 on 2023-07-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('id_proof', models.FileField(upload_to='id_proofs/')),
                ('room_category', models.CharField(max_length=50)),
                ('single_bed_room_type', models.CharField(max_length=50)),
                ('double_bed_room_type', models.CharField(max_length=50)),
            ],
        ),
    ]