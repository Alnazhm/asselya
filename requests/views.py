from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from requests.forms import RequestForm
from requests.models import Request


# Create your views here.

class CreateRequest(CreateView):
    template_name = 'create_request.html'
    model = Request
    form_class = RequestForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_form'] = RequestForm()
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            author = request.user
            data.author = author
            data.save()
            return redirect('index')
        context = {}
        context['request_form'] = RequestForm()
        return self.render_to_response(context)

class MyRequestsView(ListView):
    template_name = 'my_request.html'
    model = Request
    context_object_name = 'requests'
