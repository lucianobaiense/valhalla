#---------------------------------------------------------
#    Imports
#---------------------------------------------------------

from django.db import models
from django.contrib.auth.models import User

#---------------------------------------------------------
#    Models
#---------------------------------------------------------

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=False)
    skype = models.CharField(max_length=100, blank=False)
    hipchat = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(blank=False)
    about = models.TextField(max_length=400, blank=False)
    photo = models.ImageField(upload_to='profiles/', max_length=100, blank=True)
    agent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = ('Profile')
        verbose_name_plural = ('Profile')

    def __str__(self):
        return u'{0}'.format(self.username)

    def __unicode__(self):
        return u'{0}'.format(self.username)


class News(models.Model):
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=400, blank=False)
    author = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE, related_name='news_author')
    readers = models.ManyToManyField(User, through='Reader', through_fields=('notification', 'reader'), related_name='news_reader')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = ('News')
        verbose_name_plural = ('News')

    def __str__(self):
        return u'{0}'.format(self.subject)

    def __unicode__(self):
        return u'{0}'.format(self.subject)


class Reader(models.Model):
    notification = models.ForeignKey(News, blank=False, on_delete=models.CASCADE)
    reader = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    read_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('read_date',)
        verbose_name = ('Reader')
        verbose_name_plural = ('Reader')

    def __str__(self):
        return u'{0}'.format(self.notification)

    def __unicode__(self):
        return u'{0}'.format(self.notification)


class System(models.Model):
    message = models.TextField(max_length=100, blank=False)
    link = models.CharField(max_length=100, blank=True)
    reader = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = ('System')
        verbose_name_plural = ('System')

    def __str__(self):
        return u'{0}'.format(self.message)

    def __unicode__(self):
        return u'{0}'.format(self.message)


class Change(models.Model):
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=400, blank=False)
    ticket = models.IntegerField(blank=False)
    uol = models.CharField(max_length=20, blank=True)
    rdm = models.IntegerField(blank=False)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    close_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    impact = models.BooleanField(default=False)
    validate = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = ('Change')
        verbose_name_plural = ('Change')

    def __str__(self):
        return u'{0}'.format(self.subject)

    def __unicode__(self):
        return u'{0}'.format(self.subject)
