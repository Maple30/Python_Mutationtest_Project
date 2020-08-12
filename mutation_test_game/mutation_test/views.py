import sys
import traceback
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool")
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
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
    diff = ['diff_1', 'diff_2', 'diff_3'] #Level分類
    # 是post才進入執行階段
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            print(request.POST['page'])
            page = 'mutation_test/' + request.POST['page'] + '.html'
            # 判斷page參數是否被更改過
            if request.POST['page'] in diff:
                # 嘗試執行程式
                try:
                    if request.FILES['file1'].name[-3:-1] + request.FILES['file1'].name[-1] != '.py':
                        raise IndexError("請上傳副檔名為py的檔案") 
                    fh.handle_uploaded_file(request.FILES['file1'])
                    assert_file = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool/test_assert.py"
                    bemutafile = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/testfile/" + request.FILES['file1'].name
                    option = [True, False, False, False]
                    args = {}
                    ans_arr = mutation.mutationtest(assert_file, bemutafile, option)
                    ans = '#這是輸出\n'
                    for i,item in enumerate(ans_arr):
                        ans += item + "\n"
                    # print('here is views','')
                    # print(ans)
                    return render(request, page,{'ans':ans})
                except Exception as e:
                    # 失敗
                    print(e)
                    error_class = e.__class__.__name__ #取得錯誤類型
                    detail = e.args[0] #取得詳細內容
                    cl, exc, tb = sys.exc_info() #取得Call Stack
                    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                    fileName = lastCallStack[0] #取得發生的檔案名稱
                    lineNum = lastCallStack[1] #取得發生的行號
                    funcName = lastCallStack[2] #取得發生的函數名稱
                    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                    print(errMsg)
                    return render(request, page,{'error' : e})
            else:
                # 參數被改的情況
                error = '你是不是在搞'
                messages.error(request, error)
                return render(request,'mutation_test/index.html')
    else:
        form = UploadFileForm()
    return render(request, 'mutation_test/upload.html', {'form': form})

#暫定沒有
def login(request):
    return render(request, 'register/login.html')

def register(request):
    return render(request, 'register/register.html')

#Level-1題目處理
def diff_1(request):
    # if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES) 
    #     if form.is_valid():
    #         fh.handle_uploaded_file(request.FILES['file1'])
    #         return render(request,'mutation_test/index.html')
    # else:
    #     form = UploadFileForm()
    return render(request, 'mutation_test/diff_1.html', {'form': form})

#Level-2題目處理
def diff_2(request):
    return render(request, 'mutation_test/diff_2.html')

#Level-3題目處理
def diff_3(request):
    return render(request, 'mutation_test/diff_3.html')
