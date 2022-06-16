

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210418_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='none.png', upload_to='goods_photos'),
        ),
    ]
