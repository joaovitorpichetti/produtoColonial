from django.db import models


def regenerate_key():
    from django.utils.crypto import get_random_string
    return get_random_string(40)


class AdminToken(models.Model):
    key = models.CharField(max_length=40, help_text="Deixe em branco para gerar um novo token", unique=True, blank=True)
    user = models.ForeignKey('auth.User', models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = regenerate_key()
        return super().save(*args, **kwargs)