# Generated by Django 4.0.4 on 2022-06-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='id de Producto')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('imagen', models.ImageField(upload_to='Productos')),
                ('descripcion', models.CharField(max_length=600, verbose_name='Descripcion')),
                ('cantidad_prod',models.IntegerField(verbose_name='Cantidad de productos')),
                ('precio', models.IntegerField(max_length=10, verbose_name='Precio')),
            ],
        ),
      
    ]
