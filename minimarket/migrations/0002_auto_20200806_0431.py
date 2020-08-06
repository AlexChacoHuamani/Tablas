# Generated by Django 3.0.8 on 2020-08-06 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minimarket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='apellidoCliente',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='correoCliente',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombreCliente',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefonoCliente',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombreProducto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='ofertaProducto',
            new_name='oferta',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precioOfertaProducto',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precioProducto',
            new_name='precioOferta',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='fechaVenta',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagenProducto',
        ),
    ]