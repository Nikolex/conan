from django.db import models

# Create your models here.

class Problem(models.Model):
    title = models.CharField('题目', max_length=100, )
    content = models.TextField('描述')
    time_limited = models.IntegerField('时间限制', default=1000)
    memory_limited = models.IntegerField('空间限制', default=64)
    rank = models.IntegerField('等级')
    in_description = models.TextField('输入描述')
    out_description = models.TextField('输出描述')
    in_case =  models.TextField('样例输入')
    out_case = models.TextField('样例输出')
    source = models.CharField('来源', max_length=50)
    tip = models.TextField('提示')


    class Meta:
        db_table = 'problem'
        verbose_name = '题库'
        verbose_name_plural = '题库'


class CommitRecord(models.Model):
    pid = models.IntegerField('题目编号')
    uid = models.IntegerField('用户编号')
    status = models.BooleanField('状态')
    result = models.CharField('结果', max_length=20)
    cost_time = models.IntegerField('时间消耗')
    cost_memory = models.IntegerField('内存消耗')
    time_commited = models.DateField('提交时间', auto_now=True)
    code = models.TextField('代码')

    class Meta:
        db_table = 'commit_record'
        verbose_name = '提交记录'
        verbose_name_plural = '提交记录'


class ProblemCatagory(models.Model):
    category_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'problem_catagory'
