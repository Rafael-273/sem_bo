from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
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

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'CRM']),
        ]


class Occupation(BaseModel):
    occupation_code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='occupations')

    class Meta:
        indexes = [
            models.Index(fields=['occupation_code', 'name', 'user']),
        ]

    def save(self, *args, **kwargs):
        super(Occupation, self).save(*args, **kwargs)

        try:
            history_entry = Occupation_history.objects.get(occupation=self)
            history_entry.occupation_code=self.occupation_code
            history_entry.name = self.name
            history_entry.save()
        except Occupation_history.DoesNotExist:
            Occupation_history.objects.create(
                occupation_code=self.occupation_code,
                name=self.name,
                occupation=self
            )


class Occupation_history(BaseModel):
    occupation_code = models.CharField(max_length=6)
    name = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='occupations_history')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, null=True, related_name='occupations_history')

    class Meta:
        indexes = [
            models.Index(fields=['occupation_code', 'name', 'user', 'occupation']),
        ]

class Record(BaseModel):
    record_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    competence_date = models.CharField(max_length=6, null=False)

    class Meta:
        indexes = [
            models.Index(fields=['record_code', 'name']),
        ]

    def save(self, *args, **kwargs):
        super(Record, self).save(*args, **kwargs)

        try:
            history_entry = Record_history.objects.get(record=self)
            history_entry.record_code=self.record_code
            history_entry.name = self.name
            history_entry.competence_date = self.competence_date
            history_entry.save()
        except Record_history.DoesNotExist:
            Record_history.objects.create(
                record_code=self.record_code,
                name=self.name,
                competence_date=self.competence_date,
                record=self
            )


class Record_history(BaseModel):
    record_code = models.CharField(max_length=2)
    name = models.CharField(max_length=50, null=False)
    competence_date = models.CharField(max_length=6, null=False)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, related_name='records_history')

    class Meta:
        indexes = [
            models.Index(fields=['record_code', 'name', 'record']),
        ]

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

    class Meta:
        indexes = [
            models.Index(fields=['procedure_code', 'name']),
        ]

    def get_record_name(self):
        if self.procedures_has_record.exists():
            return self.procedures_has_record.first().record.name
        return "N/A"

    def save(self, *args, **kwargs):
        super(Procedure, self).save(*args, **kwargs)

        try:
            history_entry = Procedure_history.objects.get(procedure=self)
            history_entry.procedure_code=self.procedure_code
            history_entry.name = self.name
            history_entry.complexity_type = self.complexity_type
            history_entry.sex_type = self.sex_type
            history_entry.maximum_execution_amount = self.maximum_execution_amount
            history_entry.stay_day_number = self.stay_day_number
            history_entry.points_number = self.points_number
            history_entry.minimum_age_value = self.minimum_age_value
            history_entry.maximum_age_value = self.maximum_age_value
            history_entry.SH_value = self.SH_value
            history_entry.SA_value = self.SA_value
            history_entry.SP_value = self.SP_value
            history_entry.stay_time_number = self.stay_time_number
            history_entry.competence_date = self.competence_date
            history_entry.save()
        except Procedure_history.DoesNotExist:
            Procedure_history.objects.create(
                procedure_code=self.procedure_code,
                name=self.name,
                complexity_type=self.complexity_type,
                sex_type=self.sex_type,
                maximum_execution_amount=self.maximum_execution_amount,
                stay_day_number=self.stay_day_number,
                points_number=self.points_number,
                minimum_age_value=self.minimum_age_value,
                maximum_age_value=self.maximum_age_value,
                SH_value=self.SH_value,
                SA_value=self.SA_value,
                SP_value=self.SP_value,
                stay_time_number=self.stay_time_number,
                competence_date=self.competence_date,
                procedure=self
            )


class Procedure_history(BaseModel):
    procedure_code = models.CharField(max_length=10)
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
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_history')

    class Meta:
        indexes = [
            models.Index(fields=['procedure_code', 'name', 'procedure']),
        ]


class Cid(BaseModel):
    cid_code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    grievance_type = models.CharField(max_length=1, null=False)
    sex_type = models.CharField(max_length=1, null=False)
    stadium_stype = models.CharField(max_length=1, null=False)
    irradiated_fields_value = models.IntegerField(null=False)

    class Meta:
        indexes = [
            models.Index(fields=['cid_code', 'name']),
        ]

    def save(self, *args, **kwargs):
        super(Cid, self).save(*args, **kwargs)

        try:
            history_entry = Cid_history.objects.get(cid=self)
            history_entry.cid_code=self.cid_code
            history_entry.name = self.name
            history_entry.grievance_type = self.grievance_type
            history_entry.sex_type = self.sex_type
            history_entry.stadium_stype = self.stadium_stype
            history_entry.irradiated_fields_value = self.irradiated_fields_value
            history_entry.save()
        except Cid_history.DoesNotExist:
            Cid_history.objects.create(
                cid_code=self.cid_code,
                name=self.name,
                grievance_type=self.grievance_type,
                sex_type=self.sex_type,
                stadium_stype=self.stadium_stype,
                irradiated_fields_value=self.irradiated_fields_value,
                cid=self
            )


class Cid_history(BaseModel):
    cid_code = models.CharField(max_length=4)
    name = models.CharField(max_length=100, null=False)
    grievance_type = models.CharField(max_length=1, null=False)
    sex_type = models.CharField(max_length=1, null=False)
    stadium_stype = models.CharField(max_length=1, null=False)
    irradiated_fields_value = models.IntegerField(null=False)
    cid = models.ForeignKey(Cid, on_delete=models.CASCADE, null=True, 
    related_name='cids_history')

    class Meta:
        indexes = [
            models.Index(fields=['cid_code', 'name', 'cid']),
        ]


class Procedure_has_cid(BaseModel):
    st_principal = models.CharField(max_length=4, null=False)
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_has_cid')
    cid = models.ForeignKey(Cid, on_delete=models.CASCADE, null=True, related_name='cids_has_procedure')

    class Meta:
        indexes = [
            models.Index(fields=['procedure', 'cid']),
        ]

    def save(self, *args, **kwargs):
        super(Procedure_has_cid, self).save(*args, **kwargs)

        try:
            history_entry = Procedure_has_cid_history.objects.get(procedure_has_cid=self)
            history_entry.st_principal = self.st_principal
            history_entry.competence_date = self.competence_date
            history_entry.procedure = Procedure_history.objects.get(procedure_code=self.procedure.procedure_code)
            history_entry.cid = Cid_history.objects.get(cid_code=self.cid.cid_code)
            history_entry.save()
        except Procedure_has_cid_history.DoesNotExist:
            Procedure_has_cid_history.objects.create(
                st_principal=self.st_principal,
                competence_date=self.competence_date,
                procedure=Procedure_history.objects.get(procedure_code=self.procedure.procedure_code) if self.procedure else None,
                cid=Cid_history.objects.get(cid_code=self.cid.cid_code) if self.cid else None,
                procedure_has_cid=self
            )


class Procedure_has_cid_history(BaseModel):
    st_principal = models.CharField(null=False)
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='procedures_has_cid')
    cid = models.ForeignKey(Cid_history, on_delete=models.CASCADE, null=True, related_name='cids_has_procedure')
    procedure_has_cid = models.ForeignKey(Procedure_has_cid, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['procedure', 'cid', 'procedure_has_cid']),
        ]


class Procedure_has_occupation(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_has_occupation')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, null=True, related_name='occupations_has_procedure')

    class Meta:
        indexes = [
            models.Index(fields=['procedure', 'occupation']),
        ]

    def save(self, *args, **kwargs):
        super(Procedure_has_occupation, self).save(*args, **kwargs)

        try:
            history_entry = Procedure_has_occupation_history.objects.get(procedure_has_occupation=self)
            history_entry.competence_date = self.competence_date
            history_entry.procedure = Procedure_history.objects.get(procedure_code=self.procedure.procedure_code)
            history_entry.occupation = Occupation_history.objects.get(occupation_code=self.occupation.occupation_code)
            history_entry.save()
        except Procedure_has_occupation_history.DoesNotExist:
            Procedure_has_occupation_history.objects.create(
                competence_date=self.competence_date,
                procedure=Procedure_history.objects.get(procedure_code=self.procedure.procedure_code) if self.procedure else None,
                occupation=Occupation_history.objects.get(occupation_code=self.occupation.occupation_code) if self.occupation else None,
                procedure_has_occupation=self
            )


class Procedure_has_occupation_history(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='procedures_has_occupation')
    occupation = models.ForeignKey(Occupation_history, on_delete=models.CASCADE, null=True, related_name='occupations_has_procedure')
    procedure_has_occupation = models.ForeignKey(Procedure_has_occupation, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['procedure', 'occupation', 'procedure_has_occupation']),
        ]


class Procedure_has_record(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, related_name='procedures_has_record')
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True, related_name='records_has_procedure')

    class Meta:
        indexes = [
            models.Index(fields=['procedure', 'record']),
        ]

    def save(self, *args, **kwargs):
        super(Procedure_has_record, self).save(*args, **kwargs)

        try:
            history_entry = Procedure_has_record_history.objects.get(procedure_has_record=self)
            history_entry.competence_date = self.competence_date
            history_entry.procedure = Procedure_history.objects.get(procedure_code=self.procedure.procedure_code)
            history_entry.record = Record_history.objects.get(record_code=self.record.record_code)
            history_entry.save()
        except Procedure_has_record_history.DoesNotExist:
            Procedure_has_record_history.objects.create(
                competence_date=self.competence_date,
                procedure=Procedure_history.objects.get(procedure_code=self.procedure.procedure_code) if self.procedure else None,
                record=Record_history.objects.get(record_code=self.record.record_code) if self.record else None,
                procedure_has_record=self
            )


class Procedure_has_record_history(BaseModel):
    competence_date = models.CharField(max_length=6, null=False)
    procedure = models.ForeignKey(Procedure_history, on_delete=models.CASCADE, null=True, related_name='procedures_has_record')
    record = models.ForeignKey(Record_history, on_delete=models.CASCADE, null=True, related_name='records_has_procedure')
    procedure_has_record = models.ForeignKey(Procedure_has_record, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['procedure', 'record', 'procedure_has_record']),
        ]
