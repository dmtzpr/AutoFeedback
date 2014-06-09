from django.contrib import admin
from make.models import Make, Model, Generation, Comment

class MakeInline(admin.StackedInline):
    model = Model
    extra = 1

class GenerationInline(admin.StackedInline):
    model = Generation
    extra = 7

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class MakeAdmine(admin.ModelAdmin):
#    fields = ['',''] show all fileds
#    list_filter = []
     inlines = [MakeInline, GenerationInline]


class ModelAdmine(admin.ModelAdmin):
#    fields = ['',''] show all fileds
#    list_filter = []
     inlines = [GenerationInline]

class GenerationAdmine(admin.ModelAdmin):
#    fields = ['',''] show all fileds
#    list_filter = []
     inlines = [CommentInline]


admin.site.register(Make, MakeAdmine)
admin.site.register(Model, ModelAdmine)
admin.site.register(Generation, GenerationAdmine)