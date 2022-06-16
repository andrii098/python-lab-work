

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220418_1201'),
        ('cart', '0002_order_goods_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='goods_ids',
            field=models.ManyToManyField(related_name='goods_ids', to='shop.Item'),
        ),
    ]
