# Generated by Django 3.0.6 on 2020-05-31 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20200530_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target_ip_assets',
            old_name='target_domain_assets_middleware',
            new_name='target_ip_assets_middleware',
        ),
        migrations.RenameField(
            model_name='target_ip_assets',
            old_name='target_domain_assets_port',
            new_name='target_ip_assets_port',
        ),
        migrations.RenameField(
            model_name='target_ip_assets',
            old_name='target_domain_assets_service',
            new_name='target_ip_assets_service',
        ),
        migrations.RenameField(
            model_name='target_ip_assets',
            old_name='target_domain_assets_title',
            new_name='target_ip_assets_title',
        ),
        migrations.RemoveField(
            model_name='target_domain_assets',
            name='target_domain_assets_ip',
        ),
        migrations.RemoveField(
            model_name='target_domain_assets',
            name='target_domain_assets_localtion',
        ),
        migrations.RemoveField(
            model_name='target_domain_assets',
            name='target_domain_assets_port',
        ),
        migrations.AddField(
            model_name='target_domain_assets',
            name='target_domain_assets_length',
            field=models.IntegerField(default=0, verbose_name='响应包大小'),
        ),
        migrations.AddField(
            model_name='target_domain_assets',
            name='target_domain_assets_statuscode',
            field=models.IntegerField(default=200, verbose_name='状态码'),
        ),
        migrations.AddField(
            model_name='target_ip_assets',
            name='target_ip_assets_length',
            field=models.IntegerField(default=0, verbose_name='响应包大小'),
        ),
        migrations.AddField(
            model_name='target_ip_assets',
            name='target_ip_assets_statuscode',
            field=models.IntegerField(default=200, verbose_name='状态码'),
        ),
        migrations.AddField(
            model_name='target_sudomain_assets',
            name='target_subdomain_assets_length',
            field=models.IntegerField(default=0, verbose_name='响应包大小'),
        ),
        migrations.AddField(
            model_name='target_sudomain_assets',
            name='target_subdomain_assets_statuscode',
            field=models.IntegerField(default=200, verbose_name='状态码'),
        ),
    ]
