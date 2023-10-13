from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class USUARIO(AbstractUser):
    NO_USUARIO = models.CharField(max_length=55)
    NO_SOBRENOME_USUARIO = models.CharField(max_length=55)
    CPF = models.CharField(max_length=11)
    ESPECIALIDADE = models.CharField(max_length=255)
    EMAIL = models.CharField(max_length=55)
    TELEFONE = models.CharField(max_length=15)
    DT_NASCIMENTO = models.DateField()
    CRM = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class CID(BaseModel):
    PROCEDIMENTOS_id = models.IntegerField(null=False)
    CO_CID = models.CharField(max_length=4, null=False)
    NO_CID = models.CharField(max_length=100, null=False)
    TP_AGRAVO = models.CharField(max_length=1, null=False)
    TP_SEXO = models.CharField(max_length=1, null=False)
    TP_ESTADIO = models.CharField(max_length=1, null=False)
    VL_CAMPOS_IRRADIADOS = models.IntegerField(null=False)


class CID_HISTORICO(BaseModel):
    PROCEDIMENTOS_id = models.IntegerField(null=False)
    CO_CID = models.CharField(max_length=4, null=False)
    NO_CID = models.CharField(max_length=100, null=False)
    TP_AGRAVO = models.CharField(max_length=1, null=False)
    TP_SEXO = models.CharField(max_length=1, null=False)
    TP_ESTADIO = models.CharField(max_length=1, null=False)
    VL_CAMPOS_IRRADIADOS = models.IntegerField(null=False)
    CID_id = models.IntegerField(null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)


class OCUPACAO(BaseModel):
    CO_OCUPACAO = models.CharField(max_length=6, null=False)
    NO_OCUPACAO = models.CharField(max_length=150, null=False)
    USUARIO_id = models.IntegerField(null=False)


class OCUPACAO_HISTORICO(BaseModel):
    CO_OCUPACAO = models.CharField(max_length=6, null=False)
    NO_OCUPACAO = models.CharField(max_length=150, null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)
    OCUPACAO_id = models.IntegerField(null=False)


class PROCEDIMENTOS(BaseModel):
    REGISTROS_id = models.IntegerField(null=False)
    NO_PROCEDIMENTO = models.CharField(max_length=250, null=False)
    TP_COMPLEXIDADE = models.CharField(max_length=1, null=False)
    TP_SEXO = models.CharField(max_length=1, null=False)
    QT_MAXIMA_EXECUCAO = models.IntegerField(null=False)
    QT_DIAS_PERMANENCIA = models.CharField(max_length=4, null=False)
    QT_PONTOS = models.IntegerField(null=False)
    VL_IDADE_MINIMA = models.IntegerField(null=False)
    VL_IDADE_MAXIMA = models.IntegerField(null=False)
    VL_SH = models.IntegerField(null=False)
    VL_SA = models.IntegerField(null=False)
    VL_SP = models.IntegerField(null=False)
    QT_TEMPO_PERMANENCIA = models.IntegerField(null=False)
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)


class PROCEDIMENTOS_HISTORICO(BaseModel):
    REGISTROS_id = models.IntegerField(null=False)
    NO_PROCEDIMENTO = models.CharField(max_length=250, null=False)
    TP_COMPLEXIDADE = models.CharField(max_length=1, null=False)
    TP_SEXO = models.CharField(max_length=1, null=False)
    QT_MAXIMA_EXECUCAO = models.IntegerField(null=False)
    QT_DIAS_PERMANENCIA = models.CharField(max_length=4, null=False)
    QT_PONTOS = models.IntegerField(null=False)
    VL_IDADE_MINIMA = models.IntegerField(null=False)
    VL_IDADE_MAXIMA = models.IntegerField(null=False)
    VL_SH = models.IntegerField(null=False)
    VL_SA = models.IntegerField(null=False)
    VL_SP = models.IntegerField(null=False)
    QT_TEMPO_PERMANENCIA = models.IntegerField(null=False)
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)


class REGISTROS(BaseModel):
    CO_REGISTRO = models.CharField(max_length=2, null=False)
    NO_REGISTRO = models.CharField(max_length=50, null=False)
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)


class REGISTROS_HISTORICO(BaseModel):
    CO_REGISTRO = models.CharField(max_length=2, null=False)
    NO_REGISTRO = models.CharField(max_length=50, null=False)
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)
    REGISTROS_id = models.IntegerField(null=False)


class RL_PROCEDIMENTO_CID(BaseModel):
    ST_PRINCIPAL = models.CharField(max_length=4, null=False)
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    CID_id = models.IntegerField(null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)


class RL_PROCEDIMENTO_CID_HISTORICO(BaseModel):
    ST_PRINCIPAL = models.CharField(max_length=4, null=False)
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)
    CID_id = models.IntegerField(null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)
    RL_PROCEDIMENTO_CID_id = models.IntegerField(null=False)


class RL_PROCEDIMENTO_OCUPACAO(BaseModel):
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)
    OCUPACAO_id = models.IntegerField(null=False)


class RL_PROCEDIMENTO_OCUPACAO_HISTORICO(BaseModel):
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)
    OCUPACAO_id = models.IntegerField(null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)
    RL_PROCEDIMENTO_OCUPACAO_id = models.IntegerField(null=False)


class RL_PROCEDIMENTO_REGISTRO(BaseModel):
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    REGISTROS_id = models.IntegerField(null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)


class RL_PROCEDIMENTO_REGISTRO_HISTORICO(BaseModel):
    DT_COMPETENCIA = models.CharField(max_length=6, null=False)
    REGISTROS_id = models.IntegerField(null=False)
    PROCEDIMENTOS_id = models.IntegerField(null=False)
    ULTIMA_ATUALIZACAO = models.DateField(null=False)
    RL_PROCEDIMENTO_REGISTRO_id = models.IntegerField(null=False)
