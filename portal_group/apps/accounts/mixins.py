from django.contrib.auth.mixins import UserPassesTestMixin

class ModeratorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        you = self.request.user
        return you.is_authenticated and (you.is_superuser or you.groups.filter(name__in=['Moderator', 'Admin']).exists())


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        you = self.request.user
        return you.is_authenticated and (you.is_superuser or you.groups.filter(name='Admin').exists())