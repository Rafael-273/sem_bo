from django.contrib import admin
from .models import User, Occupation, Occupation_history, Record, Record_history, Procedure, Procedure_history, Cid, Cid_history, Procedure_has_cid, Procedure_has_cid_history, Procedure_has_occupation, Procedure_has_occupation_history, Procedure_has_record, Procedure_has_record_history

admin.site.register(User)
admin.site.register(Occupation)
admin.site.register(Occupation_history)
admin.site.register(Record)
admin.site.register(Record_history)
admin.site.register(Procedure)
admin.site.register(Procedure_history)
admin.site.register(Cid)
admin.site.register(Cid_history)
admin.site.register(Procedure_has_cid)
admin.site.register(Procedure_has_cid_history)
admin.site.register(Procedure_has_occupation)
admin.site.register(Procedure_has_occupation_history)
admin.site.register(Procedure_has_record)
admin.site.register(Procedure_has_record_history)
