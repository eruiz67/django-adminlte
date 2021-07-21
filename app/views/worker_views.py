from django.views.generic import (TemplateView, ListView, DetailView,
 CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import WorkerModel
from app.forms import WorkerForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render,redirect

class WorkerListView(LoginRequiredMixin, ListView):
    #model = WorkerModel
    queryset = WorkerModel.objects.filter(active=True)
    template_name = 'app/worker/worker_list.html'
    context_object_name = 'objects'
    ordering = ['identification']

    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(*args, **kwargs)
        
       

        self.request.session['page_from'] = ""
        self.request.session['referer'] = {}
        
        if context['is_paginated']:
            list_pages = []

            if 'name' not in self.request.GET:
                for i in range(context['page_obj'].number, context['page_obj'].number + 5):
                    if i <= context['page_obj'].paginator.num_pages:
                        list_pages.append(i)
            else:
                first_range = self.request.GET.get('page', '1')

                if len(WorkerListView.get_queryset(self)) % self.paginate_by == 0:
                    paginated = int(len(WorkerListView.get_queryset(self)) / self.paginate_by)
                else:
                    paginated = int(len(WorkerListView.get_queryset(self)) / self.paginate_by) + 1

                if paginated > 1:
                    for i in range(int(first_range), int(first_range) + 5):
                        if i <= paginated:
                            list_pages.append(i)

                    context['total_pages'] = paginated
                    context['has_more_pages'] = True if int(first_range) < paginated else False
                    context['next_page'] = int(first_range) + 1 if int(first_range) < paginated else '0'
                    context['has_previous_pages'] = True if int(first_range) > 1 else False
                    context['previous_page'] = int(first_range) - 1 if int(first_range) > 1 else '0'
                    context['actual_page'] = int(first_range)

            context['paginator_rows'] = list_pages

        return context

class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = WorkerModel
    context_object_name = 'obj'
    template_name = 'app/worker/worker_detail.html'

    def post(self, request, *args, **kwargs):
        worker = WorkerModel.objects.get(id=kwargs['pk'])
        if worker.active:
            worker.active=False
        else:
            worker.active=True
        worker.save()
        return redirect(reverse_lazy("app:worker_detail", kwargs={"pk":kwargs['pk']}))


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = WorkerModel
    #group_required = [u'Auxiliar Legal', 'Jefe de la Oficina Local', 'Jefe de la RBRP']
    context_object_name = 'obj'
    template_name = 'app/worker/worker_form.html'
    form_class = WorkerForm
   
    
    #def get_success_url(self):
    #    return reverse_lazy("riesgo:worker_detail", kwargs={"pk":self.object.id})

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.active = True
        instance.create_uid = self.request.user
        instance.write_uid = self.request.user
        instance.save()
        return super(WorkerCreateView, self).form_valid(form)    

    def get_success_url(self):
        return reverse_lazy("app:worker_detail", kwargs={"pk":self.object.id})

class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkerModel
    #group_required = [u'Auxiliar Legal', 'Jefe de la Oficina Local', 'Jefe de la RBRP']
    context_object_name = 'obj'
    template_name = 'app/worker/worker_form.html'
    form_class = WorkerForm
   
    
    #def get_success_url(self):
    #    return reverse_lazy("riesgo:worker_detail", kwargs={"pk":self.object.id})

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.active = True
        instance.write_uid = self.request.user
        instance.save()
        return super(WorkerUpdateView, self).form_valid(form)    

    def get_success_url(self):
        return reverse_lazy("app:worker_detail", kwargs={"pk":self.object.id})

class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkerModel
    context_object_name = 'obj'
    template_name = 'app/worker/worker_delete.html'
    success_url = reverse_lazy("app:worker_list")