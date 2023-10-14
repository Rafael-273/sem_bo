import codecs
from .models import Procedure, Procedure_history
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone

class DataImporter:
    def __init__(self, encoding='iso-8859-1'):
        self.encoding = encoding

    def import_procedure_data(files):
        procedures = Procedure.objects.all()
        created_at = timezone.now()

        if procedures:
            try:
                history_records = Procedure_history.objects.all()

                if history_records:
                    procedure_history_entries = [
                        Procedure_history(
                            name=procedure.name,
                            complexity_type=procedure.complexity_type,
                            sex_type=procedure.sex_type,
                            maximum_execution_amount=procedure.maximum_execution_amount,
                            stay_day_number=procedure.stay_day_number,
                            points_number=procedure.points_number,
                            minimum_age_value=procedure.minimum_age_value,
                            maximum_age_value=procedure.maximum_age_value,
                            SH_value=procedure.SH_value,
                            SA_value=procedure.SA_value,
                            SP_value=procedure.SP_value,
                            stay_time_number=procedure.stay_time_number,
                            competence_date=procedure.competence_date,
                            procedure=procedure,
                            created_at=created_at
                        )
                        for procedure in procedures if procedure.competence_date != Procedure_history.objects.get(procedure_code=procedure.procedure_code).competence_date
                    ]

                    Procedure_history.objects.bulk_create(procedure_history_entries)

                else:
                    procedure_history_entries = [
                        Procedure_history(
                            name=procedure.name,
                            complexity_type=procedure.complexity_type,
                            sex_type=procedure.sex_type,
                            maximum_execution_amount=procedure.maximum_execution_amount,
                            stay_day_number=procedure.stay_day_number,
                            points_number=procedure.points_number,
                            minimum_age_value=procedure.minimum_age_value,
                            maximum_age_value=procedure.maximum_age_value,
                            SH_value=procedure.SH_value,
                            SA_value=procedure.SA_value,
                            SP_value=procedure.SP_value,
                            stay_time_number=procedure.stay_time_number,
                            competence_date=procedure.competence_date,
                            procedure=procedure,
                            created_at=created_at
                        )
                        for procedure in procedures
                    ]

                    Procedure_history.objects.bulk_create(procedure_history_entries)

            except Procedure_history.DoesNotExist:
                pass

        for file in files:
            if isinstance(file, InMemoryUploadedFile):
                content = file.read()
                content_str = content.decode('iso-8859-1')

                for linha in content_str.split('\n'):
                    co_procedimento = linha[0:10].strip() if len(linha) >= 10 else ''
                    no_procedimento = linha[10:260].strip() if len(linha) >= 260 else ''
                    tp_complexidade = linha[260].strip() if len(linha) >= 260 else ''
                    tp_sexo = linha[261].strip() if len(linha) >= 261 else ''
                    qt_maxima_execucao = int(linha[262:266].strip()) if len(linha) >= 266 else 0
                    qt_dias_permanencia = int(linha[267:270].strip()) if len(linha) >= 270 else 0
                    qt_pontos = int(linha[271:274].strip()) if len(linha) >= 274 else 0
                    vl_idade_minima = int(linha[275:278].strip()) if len(linha) >= 278 else 0
                    vl_idade_maxima = int(linha[279:282].strip()) if len(linha) >= 282 else 0
                    vl_sh = int(linha[283:292].strip()) if len(linha) >= 292 else 0
                    vl_sa = int(linha[293:302].strip()) if len(linha) >= 302 else 0
                    vl_sp = int(linha[303:312].strip()) if len(linha) >= 312 else 0
                    qt_tempo_permanencia = int(linha[320:324].strip()) if len(linha) >= 324 else 0
                    dt_competencia = linha[324:330].strip() if len(linha) >= 330 else ''
                    created_at = timezone.now()

                    procedure, created = Procedure.objects.get_or_create(
                        procedure_code=co_procedimento,
                        defaults={
                            'name': no_procedimento,
                            'complexity_type': tp_complexidade,
                            'sex_type': tp_sexo,
                            'maximum_execution_amount': qt_maxima_execucao,
                            'stay_day_number': qt_dias_permanencia,
                            'points_number': qt_pontos,
                            'minimum_age_value': vl_idade_minima,
                            'maximum_age_value': vl_idade_maxima,
                            'SH_value': vl_sh,
                            'SA_value': vl_sa,
                            'SP_value': vl_sp,
                            'stay_time_number': qt_tempo_permanencia,
                            'competence_date': dt_competencia,
                            'created_at': created_at
                        }
                    )

                    if not created:
                        procedure.name = no_procedimento
                        procedure.complexity_type = tp_complexidade
                        procedure.sex_type = tp_sexo
                        procedure.maximum_execution_amount = qt_maxima_execucao
                        procedure.stay_day_number = qt_dias_permanencia
                        procedure.points_number = qt_pontos
                        procedure.minimum_age_value = vl_idade_minima
                        procedure.maximum_age_value = vl_idade_maxima
                        procedure.SH_value = vl_sh
                        procedure.SA_value = vl_sa
                        procedure.SP_value = vl_sp
                        procedure.stay_time_number = qt_tempo_permanencia
                        procedure.competence_date = dt_competencia
                        procedure.created_at = created_at

                    procedure.save()
