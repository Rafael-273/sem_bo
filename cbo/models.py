from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class User(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    CPF = models.CharField(max_length=11)
    specialty = models.CharField(max_length=255)
    email = models.CharField(max_length=55)
    telephone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    CRM = models.CharField(max_length=15)


class Occupation(BaseModel):
    occupation_code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='occupations')


class Occupation_history(BaseModel):
    occupation_code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='occupations_history')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, null=True, related_name='occupations_history')


class Record(BaseModel):
    record_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    competence_date = models.CharField(max_length=6, null=False)


class Record_history(BaseModel):
    record_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    competence_date = models.CharField(max_length=6, null=False)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, related_name='records_history')


class Procedure(BaseModel):
    procedure_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=250, null=True)
    complexity_type = models.CharField(max_length=1, null=True)
    sex_type = models.CharField(max_length=1, null=True)
    maximum_execution_amount = models.IntegerField(null=True)
    stay_day_number = models.CharField(max_length=4, null=True)
    points_number = models.IntegerField(null=True)
    minimum_age_value = models.IntegerField(null=True)
    maximum_age_value = models.IntegerField(null=True)
    SH_value = models.IntegerField(null=True)
    SA_value = models.IntegerField(null=True)
    SP_value = models.IntegerField(null=True)
    stay_time_number = models.IntegerField(null=True)
    competence_date = models.CharField(max_length=6, null=True)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, related_name='procedures')


class Procedure_history(BaseModel):
    procedure_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=250, null=True)
    complexity_type = models.CharField(max_length=1, null=True)
    sex_type = models.CharField(max_length=1, null=True)
    maximum_execution_amount = models.IntegerField(null=True)
    stay_day_number = models.CharField(max_length=4, null=True)
    points_number = models.IntegerField(null=True)
    minimum_age_value = models.IntegerField(null=True)
    maximum_age_value = models.IntegerField(null=True)
    SH_value = models.IntegerField(null=True)
    SA_value = models.IntegerField(null=True)
    SP_value = models.IntegerField(null=True)
    stay_time_number = models.IntegerField(null=True)
    competence_date = models.CharField(max_length=6, null=True)
    record = models.ForeignKey(Record_history, on_delete=models.CASCADE, null=True, related_name='procedures_history')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_history')


class Cid(BaseModel):
    cid_code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    grievance_type = models.CharField(max_length=1, null=False)
    sex_type = models.CharField(max_length=1, null=False)
    stadium_stype = models.CharField(max_length=1, null=False)
    irradiated_fields_value = models.IntegerField(null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='cids')


class Cid_history(BaseModel):
    cid_code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    grievance_type = models.CharField(max_length=1, null=False)
    sex_type = models.CharField(max_length=1, null=False)
    stadium_stype = models.CharField(max_length=1, null=False)
    irradiated_fields_value = models.IntegerField(null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='cids_history')
    cid = models.ForeignKey(Cid, on_delete=models.CASCADE, null=True, related_name='cids_history')


class Procedure_has_cid(BaseModel):
    st_principal = models.CharField(max_length=4, null=False)
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_has_cid')
    cid = models.ForeignKey(Cid, on_delete=models.CASCADE, null=True, related_name='cids_has_procedure')


class Procedure_has_cid_history(BaseModel):
    st_principal = models.CharField(max_length=4, null=False)
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='procedures_has_cid')
    cid = models.ForeignKey(Cid_history, on_delete=models.CASCADE, null=True, related_name='cids_has_procedure')
    procedure_has_cid = models.ForeignKey(Procedure_has_cid, on_delete=models.CASCADE, null=True)


class Procedure_has_occupation(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_has_occupation')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, null=True, related_name='occupations_has_procedure')


class Procedure_has_occupation_history(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='procedures_has_occupation')
    occupation = models.ForeignKey(Occupation_history, on_delete=models.CASCADE, null=True, related_name='occupations_has_procedure')
    procedure_has_occupation = models.ForeignKey(Procedure_has_occupation, on_delete=models.CASCADE, null=True)


class Procedure_has_record(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_has_record')
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, related_name='records_has_procedure')


class Procedure_has_record_history(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='procedures_has_record')
    record = models.ForeignKey(Record_history, on_delete=models.CASCADE, null=True, related_name='records_has_procedure')
    procedure_has_record = models.ForeignKey(Procedure_has_record, on_delete=models.CASCADE, null=True)
