from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm

# Create your views here.


class UserCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('show:home')

    '''def form_valid(self, form):
        print(self.request.POST['next'])
        if self.request.POST['next'] == 'back':
            return render(self.request, 'user/create.html', {'form': form})
        elif self.request.POST['next'] == 'confirm':
            return render(self.request, 'user/create_confirm.html', {'form': form})
        elif self.request.POST['next'] == 'user':
            form.save()
            # 認証
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            # ログイン
            login(self.request, user)
            return super().form_valid(form)
        else:
            # 通常このルートは通らない
            return redirect(reverse_lazy('show:home'))
    '''

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())  # リダイレクト
