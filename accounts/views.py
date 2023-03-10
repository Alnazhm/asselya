from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import LoginForm
from accounts.forms import CustomUserCreationForm, PasswordChangeForm
from requests.models import Request
from django.core.mail import send_mail

class IndexView(ListView):
    template_name = 'index.html'
    model = Request
    context_object_name = 'requests'


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next')
        user = authenticate(request, username=username, password=password)
        print(user)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            pswrd = form.cleaned_data.get('password')
            user = form.save()
            user.username = username
            user = form.save()
            subject = "?????????????????????? ?? ???????????????? ???????????????????????? ???? ?????? ????????"
            msg = f'?????? ?????????? ?????? ?????????? - {username} ?? ???????????? - {pswrd}'
            from_email = 'lgscoompany@gmail.com'
            print(subject, msg, from_email)
            send_mail(subject, msg, from_email, [username])
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # images = Image.objects.filter(users=self.request.user)
        # context['images'] = images
        return context




