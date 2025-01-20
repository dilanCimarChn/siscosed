from django.db import models

class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=7)
    estado = models.IntegerField(default=0)
    nroinforme = models.IntegerField()
    
    class Meta:
        db_table = 'area' 
        
    def __str__(self):
        return self.nombre


from django.contrib.auth.models import User

from django.conf import settings  # Importa settings para usar AUTH_USER_MODEL

class Asistencia(models.Model):
    idasistencia = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    ip = models.CharField(max_length=30, null=True, blank=True)
    observacion = models.CharField(max_length=50, null=True, blank=True)
    id_usuario = models.IntegerField(null=True, blank=True)

    # Columnas para auditoría
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificador = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Apunta al modelo personalizado de usuario
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    valor_anterior = models.TextField(null=True, blank=True)
    valor_actual = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'asistencia'
        
    def __str__(self):
        return f"Asistencia {self.idasistencia} - {self.fecha}"


class Cargo(models.Model):
    idcargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'cargo' 
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, null=True, blank=True, default="0")
    estado = models.IntegerField(null=True, blank=True, default=0)
    
    class Meta:
        db_table = 'categoria' 

    def __str__(self):
        return self.nombre

class Cite(models.Model):
    idcite = models.AutoField(primary_key=True)
    id_area = models.IntegerField()
    id_usuario = models.IntegerField()
    
    class Meta:
        db_table = 'cite' 

    def __str__(self):
        return f"Cite {self.idcite}"

class Contrato(models.Model):
    idcontrato = models.AutoField(primary_key=True)
    id_contratante = models.IntegerField(null=True, blank=True)
    id_empleado = models.IntegerField(null=True, blank=True)
    lugartrabajo = models.CharField(max_length=15, null=True, blank=True)
    fechaingreso = models.DateField(null=True, blank=True)
    fechasalida = models.DateField(null=True, blank=True)
    cuentabanco = models.CharField(max_length=32, null=True, blank=True)
    nombrebanco = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=15, null=True, blank=True)
    
    class Meta:
        db_table = 'contrato' 

    def __str__(self):
        return f"Contrato {self.idcontrato}"

class DetalleInforme(models.Model):
    iddetalle = models.AutoField(primary_key=True)
    id_informe = models.IntegerField(null=True, blank=True, default=0)
    antecedentes = models.CharField(max_length=1000, null=True, blank=True, default="0")
    analisis = models.CharField(max_length=1000, null=True, blank=True, default="0")
    desarrollo = models.CharField(max_length=1000, null=True, blank=True, default="0")
    conclusion = models.CharField(max_length=1000, null=True, blank=True, default="0")

    class Meta:
        db_table = 'detalleinforme' 

    def __str__(self):
        return f"Detalle Informe {self.iddetalle}"

class EstadoProveido(models.Model):
    idestado_proveido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'estado_proveido' 

    def __str__(self):
        return self.nombre

class EstadoRuta(models.Model):
    idestado_ruta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'estado_ruta' 


    def __str__(self):
        return self.nombre

class ExperienciaLaboral(models.Model):
    idexperienciaLaboral = models.AutoField(primary_key=True)
    nombreEmpresa = models.CharField(max_length=100)
    cargoEmpresa = models.CharField(max_length=100, null=True, blank=True)
    estado = models.IntegerField(default=0)
    id_usuario = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'experiencialaboral' 


    def __str__(self):
        return self.nombreEmpresa

class Flujo(models.Model):
    idflujo = models.AutoField(primary_key=True)
    id_campo = models.IntegerField(null=True, blank=True)
    id_area = models.IntegerField(null=True, blank=True)
    orden = models.IntegerField(null=True, blank=True)
    id_proceso = models.IntegerField(null=True, blank=True)
    
    
    class Meta:
        db_table = 'flujo'

    def __str__(self):
        return f"Flujo {self.idflujo}"
    
class Formacion(models.Model):
    idformacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    institucion = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    estado = models.IntegerField(default=0)
    id_usuario = models.IntegerField(default=0)
    
    
    class Meta:
        db_table = 'formacion'

    def __str__(self):
        return self.nombre

from django.conf import settings  # Importa settings para usar AUTH_USER_MODEL

class Informe(models.Model):
    idinforme = models.AutoField(primary_key=True)
    cite = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    id_autor = models.IntegerField(null=True, blank=True)
    id_destinatario = models.IntegerField(null=True, blank=True)
    referencia = models.CharField(max_length=500)
    resumen = models.CharField(max_length=10000)
    adjuntoexterno = models.CharField(max_length=200, null=True, blank=True)
    fechaaceptado = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=15, null=True, blank=True)
    id_ruta = models.IntegerField(null=True, blank=True)

    # Columnas para auditoría
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificador = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Apunta al modelo personalizado de usuario
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    valor_anterior = models.TextField(null=True, blank=True)
    valor_actual = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'informe'

    def __str__(self):
        return f"Informe {self.idinforme}"

    
class Proceso(models.Model):
    idproceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    estado = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'proceso'

    def __str__(self):
        return self.nombre
    
class ProcesoProveido(models.Model):
    idproceso_proveido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'proceso_proveido'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField()
    id_categoria = models.IntegerField()

    class Meta:
        db_table = 'producto'


    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    nit = models.CharField(max_length=25, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=25, null=True, blank=True)
    observacion = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    estado = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre
    
class Proveido(models.Model):
    idproveido = models.AutoField(primary_key=True)
    id_emisor = models.IntegerField()
    id_receptor = models.IntegerField(null=True, blank=True)
    fecha_plazo_n = models.DateField(null=True, blank=True)
    fecha_remitido = models.DateTimeField()
    fecha_aceptado = models.DateTimeField(null=True, blank=True)
    fecha_procesando = models.DateTimeField(null=True, blank=True)
    fecha_concluido = models.DateTimeField(null=True, blank=True)
    asunto = models.CharField(max_length=500, null=True, blank=True)
    cite = models.CharField(max_length=20, null=True, blank=True)
    adjunto_externo = models.CharField(max_length=200, null=True, blank=True)
    id_tipo_documento = models.IntegerField(null=True, blank=True)
    id_estado_proveido = models.IntegerField(null=True, blank=True)
    id_proceso_proveido = models.IntegerField(null=True, blank=True)
    id_ruta = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'proveido'

    def __str__(self):
        return f"Proveído {self.idproveido}"

class RelacionFamiliar(models.Model):
    idrelacionFamiliar = models.AutoField(primary_key=True)
    tipoRelacion = models.CharField(max_length=30, null=True, blank=True)
    nombres = models.CharField(max_length=50, null=True, blank=True)
    codigoSeguro = models.CharField(max_length=50, null=True, blank=True)
    domicilio = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=50, null=True, blank=True)
    estado = models.IntegerField(default=0)
    id_usuario = models.IntegerField()
    
    class Meta:
        db_table = 'relacionfamiliar'

    def __str__(self):
        return self.nombres

class Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    id_autor = models.IntegerField()
    fecha_iniciada = models.DateTimeField(null=True, blank=True)
    fecha_procesada = models.DateTimeField(null=True, blank=True)
    procedencia = models.CharField(max_length=100, null=True, blank=True)
    id_estado_ruta = models.IntegerField(null=True, blank=True, default=1)
    id_estado_proveido = models.IntegerField(null=True, blank=True, default=1)
    id_area = models.IntegerField(null=True, blank=True)
    id_ruta_tipo = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'ruta' 

    def __str__(self):
        return f"Ruta {self.idruta}"

class RutaTipo(models.Model):
    idruta_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        db_table = 'ruta_tipo'
        
    def __str__(self):
        return self.nombre

class SolicitudCabecera(models.Model):
    idsolicitud_cabecera = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    trabajo = models.IntegerField(default=0)
    estado = models.CharField(max_length=15, default="0")
    id_proveedor = models.IntegerField(default=0)
    id_usuario = models.IntegerField(default=0)
    id_proceso = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'solicitud_cabecera'

    def __str__(self):
        return f"Solicitud Cabecera {self.idsolicitud_cabecera}"


class SolicitudDetalle(models.Model):
    idsolicitud_detalle = models.AutoField(primary_key=True)
    id_producto = models.IntegerField()
    cantidad = models.IntegerField(null=True, blank=True)
    preciounitario = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    detalle = models.CharField(max_length=1000, null=True, blank=True)
    id_solicitud_cabecera = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'solicitud_detalle'

    def __str__(self):
        return f"Detalle de Solicitud {self.idsolicitud_detalle}"
    
class SolicitudObservacion(models.Model):
    idsolicitud_observacion = models.AutoField(primary_key=True)
    observacion = models.CharField(max_length=500, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    id_usuario = models.IntegerField()
    id_solicitud_detalle = models.IntegerField()
    id_campo = models.IntegerField()
    
    class Meta:
        db_table = 'solicitud_observacion'

    def __str__(self):
        return f"Observación Solicitud {self.idsolicitud_observacion}"

    
class TipoDocumento(models.Model):
    idtipo_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        db_table = 'tipo_documento'

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    # Campos adicionales
    codigoUsuario = models.CharField(max_length=16, null=True, blank=True)
    apellidoPaterno = models.CharField(max_length=50, null=True, blank=True)
    apellidoMaterno = models.CharField(max_length=50, null=True, blank=True)
    nombres = models.CharField(max_length=50, null=True, blank=True)
    grado = models.CharField(max_length=200, null=True, blank=True)
    fuerza = models.CharField(max_length=200, null=True, blank=True)
    regimiento = models.CharField(max_length=200, null=True, blank=True)
    carnetMilitar = models.CharField(max_length=50, null=True, blank=True)
    fotoPerfil = models.CharField(max_length=100, null=True, blank=True)
    ci = models.IntegerField(null=True, blank=True)
    expedido = models.CharField(max_length=15, null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True, blank=True)
    estadoCivil = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=50, null=True, blank=True)
    domicilio = models.CharField(max_length=50, null=True, blank=True)
    tipoLicencia = models.CharField(max_length=50, null=True, blank=True)
    codigoSeguro = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)  # Email único como identificador principal
    password = models.CharField(max_length=200)
    codigoBiometrico = models.CharField(max_length=1000, null=True, blank=True)
    estado = models.IntegerField(default=1)
    rol = models.CharField(max_length=20, null=True, blank=True, choices=[
        ('normal', 'Normal'),
        ('admin', 'Admin'),
        ('superadmin', 'SuperAdmin'),
    ])
    id_cargo = models.IntegerField(null=True, blank=True)
    id_dependencia_cargo = models.IntegerField(null=True, blank=True)
    id_area = models.IntegerField(null=True, blank=True)
    cfgConductoRegular = models.IntegerField(null=True, blank=True)
    cfgNuevoInforme = models.IntegerField(null=True, blank=True)
    cfgAccesoRutas = models.IntegerField(default=0)

    # Configuración para usar email como identificador principal
    username = None  # Eliminar campo `username`
    USERNAME_FIELD = 'email'  # Identificador principal
    REQUIRED_FIELDS = []  # Campos adicionales requeridos al crear un usuario

    # Evitar conflictos en las relaciones inversas
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_groups',  # Nombre único para la relación inversa
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_permissions',  # Nombre único para la relación inversa
        blank=True
    )

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.email


    
    
    
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('normal', 'Normal'),
        ('admin', 'Admin'),
        ('superadmin', 'Superadmin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')

    def __str__(self):
        return f"{self.username} ({self.role})"


