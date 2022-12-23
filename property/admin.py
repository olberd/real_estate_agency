from django.contrib import admin
from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', )


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber',
                    'owner_pure_phone')
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    raw_id_fields = ('who_liked', )

    inlines = [OwnerInline]


admin.site.register(Flat, FlatAdmin)


class ClaimAdmin(admin.ModelAdmin):
    fields = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat', )
    list_display = ('user', 'flat', 'text')


admin.site.register(Claim, ClaimAdmin)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone',)


admin.site.register(Owner, OwnerAdmin)


