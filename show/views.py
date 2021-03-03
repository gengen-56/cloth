from django.views.generic import ListView, CreateView, DeleteView
from .models import Post, Parts
from .forms import PostForm, LoginForm, PartsForm, SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.auth import login
from django.http import HttpResponseRedirect

# Create your views here.


SEASONS_CHOICES = (
    '春',
    '夏',
    '秋',
    '冬',
)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "show/index.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        parts = Parts.objects.all()
        seasons = SEASONS_CHOICES
        context['parts'] = parts
        context['seasons'] = seasons
        return context

    def get_queryset(self):
        results = self.model.objects.all()
        results = results.filter(user=self.request.user).order_by('-date_created')

        q_parts = self.request.GET.getlist('part')
        q_seasons = self.request.GET.getlist('season')
        if len(q_parts) != 0:

            parts = [x for x in q_parts if x in ["1", "2", "3", "4", "5"]]
            results = results.filter(part__in=parts)
        if len(q_seasons) != 0:
            seasons = [x for x in q_seasons if x in ["春", "夏", "秋", "冬"]]
            results = results.filter(season__in=seasons)
        return results


class PostCreateView(CreateView):
    model = Post
    template_name = "form"
    template_name = "show/post_create.html"
    success_url = "/"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PartsCreateView(CreateView):
    model = Parts
    template_name = "show/parts_create.html"
    success_url = "/parts_create"
    form_class = PartsForm


class PostDelete(DeleteView):
    model = Post
    context_object_name = 'delete_post'
    success_url = reverse_lazy('show:home')
    template_name = "show/post_confirm_delete.html"


class Login(LoginView):
    form_class = LoginForm
    template_name = "user/login.html"


class Logout(LoginRequiredMixin, LogoutView):
    template_name = "user/login.html"


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "show/signup.html"
    success_url = reverse_lazy('show:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
