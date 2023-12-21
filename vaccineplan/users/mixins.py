import django.contrib.auth.mixins
import django.shortcuts


class ActiveUserRequiredMixin(django.contrib.auth.mixins.AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            return django.shortcuts.redirect("homepage:home")
        return super().dispatch(request, *args, **kwargs)