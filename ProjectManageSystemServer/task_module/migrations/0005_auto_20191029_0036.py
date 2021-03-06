# Generated by Django 2.2.6 on 2019-10-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_module', '0004_auto_20191026_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prevtask',
            options={'verbose_name': '前置任务', 'verbose_name_plural': '前置任务'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': '任务', 'verbose_name_plural': '任务'},
        ),
        migrations.AlterModelOptions(
            name='taskprogress',
            options={'verbose_name': '任务进度请求', 'verbose_name_plural': '任务进度请求'},
        ),
        migrations.AlterModelOptions(
            name='tasktake',
            options={'verbose_name': '任务参与关系', 'verbose_name_plural': '任务参与关系'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='order',
        ),
        migrations.AddField(
            model_name='task',
            name='auto_adjust',
            field=models.BooleanField(default=True, verbose_name='自动调整'),
        ),
        migrations.AddField(
            model_name='task',
            name='next_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_order_task', to='task_module.Task', verbose_name='后序任务'),
        ),
        migrations.AlterField(
            model_name='prevtask',
            name='prev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prevtask', to='task_module.Task', verbose_name='前置任务'),
        ),
        migrations.AlterField(
            model_name='prevtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currtask', to='task_module.Task', verbose_name='本任务'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='删除标志'),
        ),
        migrations.AlterField(
            model_name='task',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, '阶段'), (2, '主任务'), (3, '子任务'), (4, '清单')], default=0, verbose_name='任务层级'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=24, verbose_name='任务名'),
        ),
        migrations.AlterField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_task', to='task_module.Task', verbose_name='父任务'),
        ),
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='任务进度'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_module.Project', verbose_name='项目'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, '未开始'), (2, '进行中'), (3, '已完成'), (4, '未完成'), (5, '已暂停'), (6, '已取消')], default=0, verbose_name='任务状态'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='进度说明'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='progress',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='目标进度'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='result',
            field=models.BooleanField(default=False, verbose_name='评审结果'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='result_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='评审时间'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_module.Task', verbose_name='任务'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_module.User', verbose_name='发起用户'),
        ),
        migrations.AlterField(
            model_name='tasktake',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_module.Task', verbose_name='任务'),
        ),
        migrations.AlterField(
            model_name='tasktake',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_module.User', verbose_name='用户'),
        ),
    ]
