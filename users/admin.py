from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following', )
    readonly_fields = ('username', )
    fieldsets = (
        ('Dados pessoais', {
            'fields': ('username', 'email', 'date_joined'),
            }
        ),
        ('Tuirer', {
        'fields': ('following', ),
        'description': 'Coisas relacionadas ao nosso sistema',
        }
        )
    )


admin.site.register(User, UserAdmin)
