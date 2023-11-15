from django.shortcuts import render
from django.views import View
from .models import Procedure, Record
from .process_files import DataImporter
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import EmailAuthenticationForm


class UploadFilesView(View):
    template_name = 'create/send_files.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        arquivos = request.FILES.getlist('arquivos_txt')

        for arquivo in arquivos:
            if 'tb_procedimento' in arquivo.name:
                DataImporter.import_procedure_data(arquivo)
            elif 'tb_ocupacao' in arquivo.name:
                DataImporter.import_occupation_data(arquivo)
            elif 'tb_registro' in arquivo.name:
                DataImporter.import_record_data(arquivo)
            elif 'tb_cid' in arquivo.name:
                DataImporter.import_cid_data(arquivo)
            elif 'rl_procedimento_cid' in arquivo.name:
                DataImporter.import_procedure_has_cid_data(arquivo)
            elif 'rl_procedimento_ocupacao' in arquivo.name:
                DataImporter.import_procedure_has_occupation_data(arquivo)
            elif 'rl_procedimento_registro' in arquivo.name:
                DataImporter.import_procedure_has_record_data(arquivo)

        return redirect('home')

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class Home(ListView):
    model = Procedure
    template_name = 'front/home.html'
    context_object_name = 'procedures'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = Record.objects.all()

        user = self.request.user
        context['user'] = user

        return context

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        record_name = request.GET.get('record_name')

        if query:
            user_occupation = request.user.occupation

            procedures_list = Procedure.objects.filter(
                Q(name__icontains=query) &
                Q(procedures_has_occupation__occupation=user_occupation)
            ).prefetch_related('procedures_has_record__record')

            if record_name != 'all':
                procedures_list = procedures_list.filter(procedures_has_record__record__name=record_name)

            procedures_list = procedures_list.prefetch_related('procedures_has_record__record')

            page = request.GET.get('page', 1)
            paginator = Paginator(procedures_list, 20)

            try:
                procedures = paginator.page(page)
            except PageNotAnInteger:
                procedures = paginator.page(1)
            except EmptyPage:
                procedures = paginator.page(paginator.num_pages)

            data = []
            has_more_results = procedures.has_next()

            for procedure in procedures:
                data.append({
                    'name': procedure.name,
                    'records_names': procedure.get_records_names(),
                    'has_more_results': has_more_results,
                })

            return JsonResponse({'procedures': data})

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'front/login.html'
    authentication_form = EmailAuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponseRedirect(reverse_lazy('home'))

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Credenciais inválidas. Tente novamente.')
        return HttpResponseRedirect(reverse_lazy('login'))


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ChatView(View):
    template_name = 'front/chat.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)