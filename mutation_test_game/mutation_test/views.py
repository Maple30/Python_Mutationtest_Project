import sys
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool")
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import mutation
from .forms import UploadFileForm
# filehandler = __import__("/mutation_test/file_handler")
import mutation_test.file_handler as fh


def index(request):
    '''
    assert_file = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool/test_assert.py"
    bemutafile = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool/threefive.py"
    option = [True, False, False, False]
    template_name = "mutation_test/index.html"   
    args = {}
    ans = mutation.mutationtest(assert_file, bemutafile, option)
    args['mytext'] = ans
    '''

    # print(fh.handle_uploaded_file())
    # return TemplateResponse(request, template_name, args)
    return render(request,'mutation_test/index.html')

    # return HttpResponse(ans)
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # print("00000")
        # print(form)
        if form.is_valid():
            fh.handle_uploaded_file(request.FILES['file1'])
            fh.handle_uploaded_file(request.FILES['file2'])
            return render(request,'mutation_test/index.html')
    else:
        form = UploadFileForm()
    return render(request, 'mutation_test/upload.html', {'form': form})

def login(request):

    return render(request, 'register/login.html')