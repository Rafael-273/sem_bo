from django.shortcuts import render
from django.views import View
from .models import Procedure
from .process_files import DataImporter
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string


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

class Home(ListView):
    model = Procedure
    template_name = 'front/home.html'
    context_object_name = 'procedures'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            procedures_list = Procedure.objects.filter(Q(name__icontains=query)).prefetch_related('procedures_has_record__record')
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
                    'record_name': procedure.get_record_name(),
                    'has_more_results': has_more_results,
                })

            return JsonResponse({'procedures': data})
