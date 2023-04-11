import os

AWS_QUERYSTRING_AUTH    = False
AWS_SECRET_KEY_ID       = os.environ.get("AWS_SECRET_KEY_ID")
AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'dj-sample-space'
AWS_S3_SIGNATURE_VERSION= 's3v4'
AWS_S3_REGION_NAME      = 'sgp1'
AWS_S3_ENDPOINT_URL     = "https://sgp1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS= {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION            = "https://dj-sample-space.sgp1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE    = 'proj.cdn.backends.MediaRootS3BotoStorage'
STATICFILES_STORAGE     = 'proj.cdn.backends.StaticRootS3BotoStorage'