from django.contrib import admin

from example.models import FlowerType,Product,Bucket


admin.site.register(FlowerType)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'type')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'type')
    search_fields = ('name',)
    ordering = ('name',)

class BucketAdmin(admin.TabularInline):
    model = Bucket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0



