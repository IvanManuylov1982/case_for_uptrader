from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = 'order', 'name'

    def __str__(self):
        return self.name

#
# class SubMenu(models.Model):
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class ListMenu(models.Model):
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     list_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.list_name