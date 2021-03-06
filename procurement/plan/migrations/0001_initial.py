# Generated by Django 2.2.7 on 2020-03-14 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisition_approval', models.BooleanField(default=True)),
                ('plan_approval', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsolidationGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_of_procurement', models.CharField(max_length=128, null=True)),
                ('source_of_funding', models.CharField(max_length=128, null=True)),
                ('contract_type', models.CharField(max_length=64, null=True)),
                ('prequalification', models.BooleanField(null=True)),
                ('bid_invitation_date', models.DateTimeField(null=True)),
                ('bid_closing_date', models.DateTimeField(null=True)),
                ('bid_approval_and_evaluation_date', models.DateTimeField(null=True)),
                ('award_notification_date', models.DateTimeField(null=True)),
                ('contract_signing_date', models.DateTimeField(null=True)),
                ('contract_completion_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_preparation', models.BooleanField(default=False)),
                ('requisition_initiation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_approval', models.BooleanField(default=True)),
                ('role_deligation', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfPDU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_approval', models.BooleanField(default=True)),
                ('role_deligation', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('title', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
                ('hod', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PDUMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_consolidation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_of_procurement', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit_of_measure', models.CharField(max_length=100)),
                ('estimated_cost', models.IntegerField()),
                ('source_of_funding', models.CharField(max_length=100)),
                ('date_required_q1', models.BooleanField()),
                ('date_required_q2', models.BooleanField()),
                ('date_required_q3', models.BooleanField()),
                ('date_required_q4', models.BooleanField()),
                ('prepared', models.BooleanField(default=True)),
                ('hod_approved', models.BooleanField(default=False)),
                ('pdu_approved', models.BooleanField(default=False)),
                ('reverted', models.BooleanField(default=False)),
                ('consolidated', models.BooleanField(default=False)),
                ('date_prepared', models.DateTimeField(null=True)),
                ('date_hod_approved', models.DateTimeField(null=True)),
                ('date_pdu_approved', models.DateTimeField(null=True)),
                ('date_reverted', models.DateTimeField(null=True)),
                ('date_consolidated', models.DateTimeField(null=True)),
                ('chart_of_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Expense')),
                ('consolidation_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.ConsolidationGroup')),
            ],
        ),
        migrations.CreateModel(
            name='ProcurementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='SubProgramme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Programme')),
            ],
        ),
        migrations.CreateModel(
            name='VoteController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisition_approval', models.BooleanField(default=True)),
                ('sub_programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.SubProgramme')),
            ],
        ),
        migrations.CreateModel(
            name='UserDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget_sealing', models.IntegerField()),
                ('plan_prepared', models.BooleanField(default=False)),
                ('plan_prepared_date', models.DateTimeField(null=True)),
                ('plan_submitted', models.BooleanField(default=False)),
                ('plan_submitted_date', models.DateTimeField(null=True)),
                ('plan_received', models.BooleanField(default=False)),
                ('plan_received_date', models.DateTimeField(null=True)),
                ('plan_reverted', models.BooleanField(default=False)),
                ('plan_reverted_date', models.DateTimeField(null=True)),
                ('plan_reverted_reason', models.CharField(max_length=512, null=True)),
                ('sub_programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.SubProgramme')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounting_officer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.AccountingOfficer')),
                ('department_member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.DepartmentMember')),
                ('head_of_department', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.HeadOfDepartment')),
                ('head_of_pdu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.HeadOfPDU')),
                ('pdu_member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.PDUMember')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vote_controller', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.VoteController')),
            ],
        ),
        migrations.CreateModel(
            name='PlanComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=512)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Member')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='PlanAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=64)),
                ('detail', models.CharField(max_length=512, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Member')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plan')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='type_of_procurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.ProcurementType'),
        ),
        migrations.AddField(
            model_name='plan',
            name='user_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.UserDepartment'),
        ),
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.Profile'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.UserDepartment'),
        ),
        migrations.AddField(
            model_name='consolidationgroup',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Entity'),
        ),
        migrations.AddField(
            model_name='consolidationgroup',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Expense'),
        ),
    ]
