from django.views.generic import ListView, CreateView, DeleteView
from .models import Post, Parts
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "show/index.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        parts = Parts.objects.all()
        context['parts'] = parts

        return context

    def get_queryset(self):
        results = self.model.objects.all()

        q_parts = self.request.GET.getlist('part')

        if len(q_parts) != 0:
            parts = [x for x in q_parts if x in ["1", "2", "3", "4"]]
            results = results.filter(part__in=parts)

        return results


class PostCreateView(CreateView):
    model = Post
    template_name = "form"
    template_name = "show/post_create.html"
    success_url = "/"
    form_class = PostForm


class PostDelete(DeleteView):
    model = Post
    context_object_name = 'delete_post'
    success_url = reverse_lazy('show:home')
    template_name = "show/post_confirm_delete.html"
