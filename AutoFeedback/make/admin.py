from django.contrib import admin
from make.models import Make, Model

class MakeInline(admin.StackedInline):
    model = Model
    extra = 1

class MakeAdmine(admin.ModelAdmin):
#    fields = ['',''] show all fileds
#    list_filter = []
     inlines = [MakeInline]



admin.site.register(Make, MakeAdmine)