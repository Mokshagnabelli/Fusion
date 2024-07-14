# Generated by Django 3.1.5 on 2024-06-19 22:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filetracking', '0001_initial'),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndentFile',
            fields=[
                ('file_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='filetracking.file')),
                ('item_name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('present_stock', models.IntegerField()),
                ('estimated_cost', models.IntegerField(null=True)),
                ('purpose', models.CharField(max_length=250)),
                ('specification', models.CharField(max_length=250)),
                ('item_type', models.CharField(max_length=250)),
                ('item_subtype', models.CharField(default='computers', max_length=250)),
                ('nature', models.BooleanField(default=False)),
                ('indigenous', models.BooleanField(default=False)),
                ('replaced', models.BooleanField(default=False)),
                ('budgetary_head', models.CharField(max_length=250)),
                ('expected_delivery', models.DateField()),
                ('sources_of_supply', models.CharField(max_length=250)),
                ('head_approval', models.BooleanField(default=False)),
                ('director_approval', models.BooleanField(default=False)),
                ('financial_approval', models.BooleanField(default=False)),
                ('purchased', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'IndentFile',
            },
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomenclature', models.CharField(max_length=100, unique=True)),
                ('inUse', models.BooleanField(default=True)),
                ('location', models.CharField(choices=[('SR1', 'LHTC'), ('SR2', 'Computer Center'), ('SR3', 'Panini Hostel'), ('SR4', 'Lab complex'), ('SR5', 'Admin Block')], default='SR1', max_length=100)),
                ('isTransferred', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.departmentinfo')),
            ],
            options={
                'db_table': 'StockItem',
            },
        ),
        migrations.CreateModel(
            name='StockEntry',
            fields=[
                ('item_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ps1.indentfile')),
                ('vendor', models.CharField(max_length=250)),
                ('current_stock', models.IntegerField()),
                ('recieved_date', models.DateField()),
                ('bill', models.FileField(upload_to='')),
                ('location', models.CharField(choices=[('SR1', 'LHTC'), ('SR2', 'Computer Center'), ('SR3', 'Panini Hostel'), ('SR4', 'Lab complex'), ('SR5', 'Admin Block')], default='SR1', max_length=100)),
                ('dealing_assistant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'StockEntry',
            },
        ),
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_location', models.CharField(choices=[('SR1', 'LHTC'), ('SR2', 'Computer Center'), ('SR3', 'Panini Hostel'), ('SR4', 'Lab complex'), ('SR5', 'Admin Block')], default='SR1', max_length=100)),
                ('dest_location', models.CharField(choices=[('SR1', 'LHTC'), ('SR2', 'Computer Center'), ('SR3', 'Panini Hostel'), ('SR4', 'Lab complex'), ('SR5', 'Admin Block')], default='SR2', max_length=100)),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('dest_dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_dest_transfers', to='globals.departmentinfo')),
                ('indent_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.indentfile')),
                ('src_dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_src_transfers', to='globals.departmentinfo')),
                ('stockItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.stockitem')),
            ],
            options={
                'db_table': 'StockTransfer',
            },
        ),
        migrations.AddField(
            model_name='stockitem',
            name='StockEntryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.stockentry'),
        ),
    ]
