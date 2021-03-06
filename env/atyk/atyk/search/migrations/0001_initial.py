# Generated by Django 2.0.7 on 2018-07-10 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('reino', models.CharField(max_length=20)),
                ('propiedad_principal', models.CharField(choices=[('p', 'Proteina'), ('c', 'Carbohidrato'), ('m', 'Mineral'), ('g', 'Grano'), ('ci', 'Citrico'), ('d', 'Dulce'), ('n', 'Neutro')], help_text='Caracteristica del alimento', max_length=1)),
                ('propiedad_secundaria', models.TextField(max_length=500)),
                ('presentacion', models.CharField(max_length=50)),
                ('subproducto', models.BooleanField(default=False)),
                ('excepciones', models.CharField(blank=True, max_length=50, null=True)),
                ('restricciones', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre de un ingrediente (ejemplo: papa, nata, batata)', max_length=50)),
                ('preparacion', models.TextField(help_text='Ingrese la preparacion', max_length=1000)),
                ('tiempo_preparacion', models.CharField(help_text='Ingrese el tiempo de preparacion promedio', max_length=50)),
                ('metodo_coccion', models.CharField(help_text='Ingrese un metodo de coccion para la receta principal', max_length=50)),
                ('ingrediente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='search.Ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoReceta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(help_text='Ingrese la categoria de la receta', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='receta',
            name='tipo',
            field=models.ManyToManyField(help_text='Seleccione un tipo de receta', to='search.TipoReceta'),
        ),
    ]
