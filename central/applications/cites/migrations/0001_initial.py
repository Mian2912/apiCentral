# Generated by Django 4.1.2 on 2022-10-26 16:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employess', '0001_initial'),
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('type_document', models.CharField(max_length=30)),
                ('document', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('eps', models.CharField(max_length=20)),
                ('required_files', models.CharField(max_length=30)),
                ('orden_file', models.FileField(upload_to='')),
                ('autorization', models.FileField(upload_to='')),
                ('recommendations', models.CharField(max_length=100)),
                ('id_doctors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.doctors')),
                ('id_employee', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='employess.employess')),
                ('id_speciality', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='system.specialitys')),
                ('id_status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.status')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
