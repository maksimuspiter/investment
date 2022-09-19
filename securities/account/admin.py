from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Securities, Currency, SecurityType, Position, InvestorUser


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


class SecurityTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


class SecuritiesAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'get_photo', 'type_securities', 'name', 'currency')
    list_display_links = ('type_securities', 'ticker', 'name')
    search_fields = ('type_securities', 'ticker',)
    list_filter = ('type_securities', 'currency')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=30 >")
        return '-'

    get_photo.short_description = 'Картинка'


class PositionAdmin(admin.ModelAdmin):
    list_display = ('security', 'investor', 'slug', 'quantity', 'price', 'total_cost')
    list_filter = ('investor', 'security', )
    list_display_links = ('security', 'slug')

    def total_cost(self, obj):
        return obj.price * obj.quantity

    total_cost.short_description = 'Общая цена'


class InvestorUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'slug')


admin.site.register(Securities, SecuritiesAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(SecurityType, SecurityTypeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(InvestorUser, InvestorUserAdmin)
