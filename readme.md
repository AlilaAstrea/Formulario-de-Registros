# Formulario Interpretes

>El proposito de este Proyecto es manejar la navegabilidad en django, junto a los templates y views llamando sus funciones para guardar datos en una base de datos
>
---

## Instalación

Con el comando pip instala estos paquetes en tu entorno virtual o raiz *(Teniendo en cuenta que ya está instalado Python)*

* `pip install django`
* `pip install pymysql`
* [XAMPP](https://www.apachefriends.org/es/download.html)

>Con XAMPP podremos ejecutar la interfaz de la base de datos, iniciando Apache y MySQL
![](https://github.com/AlilaAstrea/Formulario-de-Registros/blob/main/assets/xamppa.png)

>En la interfaz de **phpMyAdmin**, debes crear la base de datos con nombre `django_bd2`. 
![](https://github.com/AlilaAstrea/Formulario-de-Registros/blob/main/assets/nombrebd.png)
Una vez creada en la terminal con la ruta del proyecto, ejecuta el comando:
```
py manage.py makemigrations
```
```
py manage.py migrate
```




*Con la finalidad de realizar la migración de la tabla **Interprete** que se encuentra en el archivo models.py*
>

---