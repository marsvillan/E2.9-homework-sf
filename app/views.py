from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Email
from .forms import EmailForm


# Create your views here.
class EmailListView(CreateView, ListView):
    model = Email
    paginate_by = 4
    form_class = EmailForm
    success_url = reverse_lazy('main-view')

    def form_invalid(self, form):
        """
        Если дaнные формы некорректны,
        то нужно сделать запрос для ListView 
        """
        self.object_list = self.get_queryset()
        return super().form_invalid(form)

