# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advogado(models.Model):
    id_adv = models.IntegerField(primary_key=True)
    num_oab = models.BigIntegerField()
    escala_preco = models.IntegerField()
    celular = models.BigIntegerField()
    telefone = models.BigIntegerField(blank=True, null=True)
    cpf_cnpj = models.BigIntegerField()
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    descricao = models.CharField(max_length=1000, blank=True, null=True)
    avaliacao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Advogado'


class AdvogadoEspecialidade(models.Model):
    advogado_id_adv = models.ForeignKey(Advogado, models.DO_NOTHING, db_column='Advogado_id_adv')  # Field name made lowercase.
    especialidade_id_especialidade = models.ForeignKey('Especialidade', models.DO_NOTHING, db_column='Especialidade_id_especialidade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Advogado_Especialidade'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    field_telefone = models.BigIntegerField(db_column=' telefone')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    cpf_cnpj = models.BigIntegerField()
    id_adv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'


class ClienteAdvogado(models.Model):
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id_cliente')  # Field name made lowercase.
    advogado_id_adv = models.ForeignKey(Advogado, models.DO_NOTHING, db_column='Advogado_id_adv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente_Advogado'


class Endereco(models.Model):
    num = models.ForeignKey(Advogado, models.DO_NOTHING, db_column='num')
    logradouro = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=35)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Endereco'


class Especialidade(models.Model):
    nome = models.CharField(max_length=40)
    id_especialidade = models.IntegerField(primary_key=True)
    id_adv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Especialidade'


class Preco(models.Model):
    id_servico = models.OneToOneField(Advogado, models.DO_NOTHING, db_column='id_servico', primary_key=True)
    preco = models.TextField()  # This field type is a guess.
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Preco'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    email = models.CharField(unique=True, max_length=255)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
