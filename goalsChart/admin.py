from django.contrib import admin
from goalsChart.models import User, Goal

# username: ubuntu
# password: quit

class GoalInline(admin.TabularInline):
    model = Goal
    extra = 3
    

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user_name']}),
        (None,               {'fields': ['min_balance']}),
        ('Date information', {'fields': ['profile_create_date'], 'classes': ['collapse']}),
    ]
    inlines = [GoalInline]
    list_display = ('user_name', 'min_balance') #future - add # of goals


admin.site.register(User, UserAdmin)
admin.site.register(Goal)

