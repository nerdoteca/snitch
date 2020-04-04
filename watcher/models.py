from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from model_utils.models import TimeStampedModel
from model_utils import Choices


class Package(TimeStampedModel):
    PROGRAMMING_LANGUAGE = Choices(
        ('python', 'python'),
        ('javascript', 'javascript'),
        ('css', 'css'),
    )

    CODE_HOSTING = Choices(
        ('github', 'github'),
    )

    name = models.CharField(
        _('name'), max_length=100
    )
    programming_language = models.CharField(
        _('programming language'), max_length=50, choices=PROGRAMMING_LANGUAGE
    )
    code_hosting = models.CharField(
        _('code hosting'), max_length=50, choices=CODE_HOSTING
    )
    repository_owner = models.CharField(
        _('repository owner'), max_length=100
    )
    repository_name = models.CharField(
        _('repository name'), max_length=100
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('package')
        verbose_name_plural = _('packages')
        unique_together = [
            ['name', 'programming_language'],
            ['code_hosting', 'repository_owner', 'repository_name'],
        ]
        ordering = [
            'name',
        ]


class Release(TimeStampedModel):
    STATUS = Choices(
        ('new', _('new')),
        ('available', _('available')),
        ('tweeted', _('tweeted')),
        ('fail', _('fail')),
    )

    name = models.CharField(
        _('name'), max_length=50
    )
    status = models.CharField(
        _('status'), max_length=50, db_index=True,
        choices=STATUS, default=STATUS.new
    )
    package = models.ForeignKey(
        'Package', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = _('release')
        verbose_name_plural = _('releases')
        unique_together = [
            ['name', 'package'],
        ]
        ordering = [
            '-created',
        ]


class Log(TimeStampedModel):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(
        _('object id')
    )
    content_object = GenericForeignKey(
        'content_type', 'object_id'
    )
    message = models.TextField(
        _('message')
    )

    class Meta:
        verbose_name = _('log')
        verbose_name_plural = _('logs')
        ordering = [
            '-created',
        ]
