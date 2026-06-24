# Email setup for production

This project currently uses a console email backend for local development, which is fine for testing but does not send real messages.

## What to do on production

1. Switch Django to SMTP backend.
2. Configure real SMTP credentials.
3. Set a sender address.

## Recommended Django settings

Add these values to your environment or production settings:

```python
import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.example.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'true').lower() == 'true'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'no-reply@example.com')
SERVER_EMAIL = DEFAULT_FROM_EMAIL
```

## Example for popular providers

### SendGrid

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = 'no-reply@example.com'
```

### Mailgun

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = 'no-reply@example.com'
```

## Notes

- Keep secrets in environment variables, not in source code.
- For local testing, the current console backend is fine.
- If you use allauth email verification, make sure the sender address is valid and the domain is configured correctly.
