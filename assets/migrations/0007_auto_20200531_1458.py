# Generated by Django 3.0.6 on 2020-05-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20200531_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-m_time'], 'verbose_name': '厂商表', 'verbose_name_plural': '厂商表'},
        ),
        migrations.AlterModelOptions(
            name='company_domain',
            options={'ordering': ['-m_time'], 'verbose_name': '厂商域名资产总表', 'verbose_name_plural': '厂商域名资产总表'},
        ),
        migrations.AlterModelOptions(
            name='company_ips',
            options={'ordering': ['-m_time'], 'verbose_name': '厂商IP资产总表', 'verbose_name_plural': '厂商IP资产总表'},
        ),
        migrations.AlterModelOptions(
            name='target_ip',
            options={'ordering': ['-m_time'], 'verbose_name': '厂商IP资产详细表', 'verbose_name_plural': '厂商IP资产详细表'},
        ),
        migrations.AlterModelOptions(
            name='target_sudomain',
            options={'ordering': ['-m_time'], 'verbose_name': '厂商子域名资产详细表', 'verbose_name_plural': '厂商子域名资产详细表'},
        ),
        migrations.RenameField(
            model_name='target_ip',
            old_name='company',
            new_name='company_ips',
        ),
        migrations.RenameField(
            model_name='target_sudomain',
            old_name='target_domain',
            new_name='company_domain',
        ),
        migrations.AlterField(
            model_name='company_ips',
            name='company_ips_ips',
            field=models.CharField(max_length=254, verbose_name='厂商IP资产总表'),
        ),
    ]
