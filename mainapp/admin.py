from django.contrib import admin
from mainapp.models import News, Course, Lesson, CourseTeacher

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseTeacher)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted', 'slug')
    list_filter = ('deleted',)
    search_fields = ('title',)
    actions = ('mark_as_delete',)

    # Вовод читаемой новости
    def slug(self, obj):
        return obj.title.lower().replace(' ', '-')

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным '
