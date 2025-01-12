# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sigla = models.CharField(max_length=7)
    estado = models.IntegerField()
    nroinforme = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'area'


class Asistencia(models.Model):
    idasistencia = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    tipo = models.CharField(db_column='Tipo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(max_length=30, blank=True, null=True)
    observacion = models.CharField(max_length=50, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'


class Campo(models.Model):
    idcampo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    id_areaejemplo = models.CharField(max_length=50, blank=True, null=True)
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campo'


class Cargo(models.Model):
    idcargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo'


class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cite(models.Model):
    idcite = models.AutoField(primary_key=True)
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'cite'


class Contrato(models.Model):
    idcontrato = models.AutoField(primary_key=True)
    id_contratante = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_contratante', blank=True, null=True)
    id_empleado = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    lugartrabajo = models.CharField(db_column='LugarTrabajo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    fechasalida = models.DateField(db_column='fechaSalida', blank=True, null=True)  # Field name made lowercase.
    cuentabanco = models.CharField(db_column='cuentaBanco', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nombrebanco = models.CharField(db_column='nombreBanco', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato'


class Detalleinforme(models.Model):
    iddetalle = models.AutoField(primary_key=True)
    id_informe = models.ForeignKey('Informe', models.DO_NOTHING, db_column='id_informe', blank=True, null=True)
    antecedentes = models.CharField(max_length=1000, blank=True, null=True)
    analisis = models.CharField(max_length=1000, blank=True, null=True)
    desarrollo = models.CharField(max_length=1000, blank=True, null=True)
    conclusion = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleinforme'


class EstadoProveido(models.Model):
    idestado_proveido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'estado_proveido'


class EstadoRuta(models.Model):
    idestado_ruta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_ruta'


class Experiencialaboral(models.Model):
    idexperiencialaboral = models.AutoField(db_column='idexperienciaLaboral', primary_key=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=100)  # Field name made lowercase.
    cargoempresa = models.CharField(db_column='cargoEmpresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiencialaboral'


class Flujo(models.Model):
    idflujo = models.AutoField(primary_key=True)
    id_campo = models.ForeignKey(Campo, models.DO_NOTHING, db_column='id_campo', blank=True, null=True)
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    id_proceso = models.ForeignKey('Proceso', models.DO_NOTHING, db_column='id_proceso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flujo'


class Formacion(models.Model):
    idformacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    institucion = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'formacion'


class Informe(models.Model):
    idinforme = models.AutoField(primary_key=True)
    cite = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    id_autor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_autor', blank=True, null=True)
    id_destinatario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_destinatario', blank=True, null=True)
    referencia = models.CharField(max_length=500)
    resumen = models.CharField(max_length=10000)
    adjuntoexterno = models.CharField(max_length=200, blank=True, null=True)
    fechaaceptado = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    id_ruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='id_ruta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informe'


class Proceso(models.Model):
    idproceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proceso'


class ProcesoProveido(models.Model):
    idproceso_proveido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'proceso_proveido'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    nit = models.CharField(max_length=25, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=25, blank=True, null=True)
    observacion = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Proveido(models.Model):
    idproveido = models.AutoField(primary_key=True)
    id_emisor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_emisor')
    id_receptor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_receptor', blank=True, null=True)
    fecha_plazo_n = models.DateField(blank=True, null=True)
    fecha_remitido = models.DateTimeField()
    fecha_aceptado = models.DateTimeField(blank=True, null=True)
    fecha_procesando = models.DateTimeField(blank=True, null=True)
    fecha_concluido = models.DateTimeField(blank=True, null=True)
    asunto = models.CharField(max_length=500, blank=True, null=True)
    cite = models.CharField(max_length=20, blank=True, null=True)
    adjunto_externo = models.CharField(max_length=200, blank=True, null=True)
    id_tipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='id_tipo_documento', blank=True, null=True)
    id_estado_proveido = models.ForeignKey(EstadoProveido, models.DO_NOTHING, db_column='id_estado_proveido', blank=True, null=True)
    id_proceso_proveido = models.ForeignKey(ProcesoProveido, models.DO_NOTHING, db_column='id_proceso_proveido', blank=True, null=True)
    id_ruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='id_ruta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveido'


class Relacionfamiliar(models.Model):
    idrelacionfamiliar = models.AutoField(db_column='idrelacionFamiliar', primary_key=True)  # Field name made lowercase.
    tiporelacion = models.CharField(db_column='TipoRelacion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=50, blank=True, null=True)
    codigoseguro = models.CharField(db_column='codigoSeguro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    domicilio = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'relacionfamiliar'


class Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    id_autor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_autor')
    fecha_iniciada = models.DateTimeField(blank=True, null=True)
    fecha_procesada = models.DateTimeField(blank=True, null=True)
    procedencia = models.CharField(max_length=100, blank=True, null=True)
    id_estado_ruta = models.ForeignKey(EstadoRuta, models.DO_NOTHING, db_column='id_estado_ruta', blank=True, null=True)
    id_estado_proveido = models.ForeignKey(EstadoProveido, models.DO_NOTHING, db_column='id_estado_proveido', blank=True, null=True)
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    id_ruta_tipo = models.ForeignKey('RutaTipo', models.DO_NOTHING, db_column='id_ruta_tipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'


class RutaTipo(models.Model):
    idruta_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ruta_tipo'


class SolicitudCabecera(models.Model):
    idsolicitud_cabecera = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    trabajo = models.IntegerField()
    estado = models.CharField(max_length=15)
    id_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='id_proveedor')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_proceso = models.ForeignKey(Proceso, models.DO_NOTHING, db_column='id_proceso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_cabecera'


class SolicitudDetalle(models.Model):
    idsolicitud_detalle = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField(blank=True, null=True)
    preciounitario = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    detalle = models.CharField(max_length=1000, blank=True, null=True)
    id_solicitud_cabecera = models.ForeignKey(SolicitudCabecera, models.DO_NOTHING, db_column='id_solicitud_cabecera', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_detalle'


class SolicitudObservacion(models.Model):
    idsolicitud_observacion = models.AutoField(primary_key=True)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_solicitud_detalle = models.ForeignKey(SolicitudDetalle, models.DO_NOTHING, db_column='id_solicitud_detalle')
    id_campo = models.ForeignKey(Campo, models.DO_NOTHING, db_column='id_campo')

    class Meta:
        managed = False
        db_table = 'solicitud_observacion'


class TipoDocumento(models.Model):
    idtipo_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    codigousuario = models.CharField(db_column='codigoUsuario', max_length=16, blank=True, null=True)  # Field name made lowercase.
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=50, blank=True, null=True)
    grado = models.CharField(max_length=200, blank=True, null=True)
    fuerza = models.CharField(max_length=200, blank=True, null=True)
    regimiento = models.CharField(max_length=200, blank=True, null=True)
    carnetmilitar = models.CharField(db_column='carnetMilitar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fotoperfil = models.CharField(db_column='fotoPerfil', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ci = models.IntegerField(blank=True, null=True)
    expedido = models.CharField(db_column='Expedido', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(max_length=10, blank=True, null=True)
    estadocivil = models.CharField(db_column='estadoCivil', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.CharField(max_length=50, blank=True, null=True)
    tipolicencia = models.CharField(db_column='TipoLicencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigoseguro = models.CharField(db_column='codigoSeguro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    codigobiometrico = models.CharField(db_column='codigoBiometrico', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField()
    rol = models.CharField(max_length=20, blank=True, null=True)
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo', blank=True, null=True)
    id_dependencia_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_dependencia_cargo', blank=True, null=True)
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    cfgconductoregular = models.IntegerField(db_column='cfgConductoRegular', blank=True, null=True)  # Field name made lowercase.
    cfgnuevoinforme = models.IntegerField(db_column='cfgNuevoInforme', blank=True, null=True)  # Field name made lowercase.
    cfgaccesorutas = models.IntegerField(db_column='cfgAccesoRutas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
