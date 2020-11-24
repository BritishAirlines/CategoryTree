from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            blank=False, null=False,
                            default='EMPTY_CATEGORY')
    parent = models.ForeignKey('self', blank=True,
                               null=True, related_name='children',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def child_list(self, include_self=False):
        result_set = []
        if include_self:
            result_set.append(self)
        for c in Category.objects.filter(parent=self):
            _r = c.child_list(include_self=True)
            if 0 < len(_r):
                result_set.extend(_r)
        return result_set

    def parents_list(self):
        if self.parent is None:
            return Category.objects.none()
        return Category.objects.filter(pk=self.parent.pk) | self.parent.parents_list()

    def siblings_list(self):
        return Category.objects.filter(parent=self.parent).exclude(id=self.id)
