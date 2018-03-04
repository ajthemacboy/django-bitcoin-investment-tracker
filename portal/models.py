from django.db import models


class INVESTMENT(models.Model):
    investment_date = models.DateField()
    investment_time = models.TimeField()
    investment_price = models.FloatField()
    investment_amount = models.FloatField()

    def __str__(self):
        result = "{} | {} | {} | {}".format(self.investment_date, self.investment_time, self.investment_price, self.investment_amount)
        return result
