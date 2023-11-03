# Generated by Django 4.2.6 on 2023-11-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbo', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='cid',
            index=models.Index(fields=['cid_code', 'name'], name='cbo_cid_cid_cod_c08b9e_idx'),
        ),
        migrations.AddIndex(
            model_name='cid_history',
            index=models.Index(fields=['cid_code', 'name', 'cid'], name='cbo_cid_his_cid_cod_c534d9_idx'),
        ),
        migrations.AddIndex(
            model_name='occupation',
            index=models.Index(fields=['occupation_code', 'name', 'user'], name='cbo_occupat_occupat_bda372_idx'),
        ),
        migrations.AddIndex(
            model_name='occupation_history',
            index=models.Index(fields=['occupation_code', 'name', 'user', 'occupation'], name='cbo_occupat_occupat_119b14_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure',
            index=models.Index(fields=['procedure_code', 'name'], name='cbo_procedu_procedu_32c72d_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_has_cid',
            index=models.Index(fields=['procedure', 'cid'], name='cbo_procedu_procedu_03e71f_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_has_cid_history',
            index=models.Index(fields=['procedure', 'cid', 'procedure_has_cid'], name='cbo_procedu_procedu_f6b178_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_has_occupation',
            index=models.Index(fields=['procedure', 'occupation'], name='cbo_procedu_procedu_1ac35f_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_has_occupation_history',
            index=models.Index(fields=['procedure', 'occupation', 'procedure_has_occupation'], name='cbo_procedu_procedu_f1da83_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_has_record',
            index=models.Index(fields=['procedure', 'record'], name='cbo_procedu_procedu_7fced0_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_has_record_history',
            index=models.Index(fields=['procedure', 'record', 'procedure_has_record'], name='cbo_procedu_procedu_8e4e67_idx'),
        ),
        migrations.AddIndex(
            model_name='procedure_history',
            index=models.Index(fields=['procedure_code', 'name', 'procedure'], name='cbo_procedu_procedu_7f7bec_idx'),
        ),
        migrations.AddIndex(
            model_name='record',
            index=models.Index(fields=['record_code', 'name'], name='cbo_record_record__6b63c2_idx'),
        ),
        migrations.AddIndex(
            model_name='record_history',
            index=models.Index(fields=['record_code', 'name', 'record'], name='cbo_record__record__ba0bae_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['first_name', 'CRM'], name='cbo_user_first_n_6f638a_idx'),
        ),
    ]
