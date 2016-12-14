from django.db import models


class Result(models.Model):
    StdID = models.CharField(max_length=15) # 學號
    Score = models.IntegerField() # 得分
    Json_Str = models.CharField(max_length=1000)

    def __str__(self):
        return self.StdID + ' - ' + str(self.Score)
