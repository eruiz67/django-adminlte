from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import WorkerModel

class WorkerListView(LoginRequiredMixin, ListView):
    #model = WorkerModel
    queryset = WorkerModel.objects.filter(active=True)
    template_name = 'app/worker/worker_list.html'
    context_object_name = 'objects'