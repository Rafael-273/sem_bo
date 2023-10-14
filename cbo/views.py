from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Occupation, Record, Procedure, Cid
from .process_files import DataImporter
from django.shortcuts import redirect


class UploadFilesView(View):
    template_name = 'create/send_files.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        arquivos = request.FILES.getlist('arquivos_txt')

        DataImporter.import_procedure_data(arquivos)

        return redirect('home')

def home(request):
    return HttpResponse("<html><body><h1>Olá, Mundo!</h1><p>Esta é a página inicial do meu site.</p></body></html>")
