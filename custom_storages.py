from django.cong import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MeidaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
