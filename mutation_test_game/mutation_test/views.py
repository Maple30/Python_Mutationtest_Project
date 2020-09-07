import sys
import traceback
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool")
import mutation
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/T35")
import T35, mutateT35
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_1")
import AssertCode_Processer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages

from .forms import UploadFileForm
# filehandler = __import__("/mutation_test/file_handler")
import mutation_test.file_handler as fh



def index(request):
    # print(fh.handle_uploaded_file())
    # return TemplateResponse(request, template_name, args)
    return render(request,'mutation_test/index.html')

    # return HttpResponse(ans)
    # Create your views here.

def upload_file(request):
    diff = ['diff_1', 'diff_2', 'diff_3'] #Level分類
    # 是post才進入執行階段
    # print(request.POST)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # print(request.FILES)
        if form.is_valid():
            # print(request.POST['page'])
            page = 'mutation_test/' + request.POST['page'] + '.html'
            # 判斷page參數是否被更改過
            if request.POST['page'] in diff:
                # 嘗試執行程式
                try:
                    if request.FILES['file1'].name[-3:-1] + request.FILES['file1'].name[-1] != '.py':
                        raise IndexError("請上傳副檔名為py的檔案") 
                    fh.handle_uploaded_file(request.FILES['file1'])
                    bemutafile = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool/threefive.py"
                    assert_file = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/testfile/" + request.FILES['file1'].name
                    option = [True, False, False, False]
                    args = {}
                    ans_arr, killper = mutation.mutationtest(assert_file, bemutafile, option)
                    ans = '#這是輸出\n'
                    for i,item in enumerate(ans_arr):
                        ans += item + "\n"
                    # print('here is views','')
                    # print(ans)
                    return JsonResponse({'ans':ans,'killper':killper})
                    # return render(request, page,{'ans':ans})
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
    else:# 不是POST的情況
        form = UploadFileForm()
    return render(request, 'mutation_test/upload.html', {'form': form})

#Level-1題目處理
def diff_1(request):
    if request.method == 'POST':
        print(request.POST['input'])
        #分割字串
        a = request.POST['input'].split(',')
        print(a)

        num_ar = []
        #捨棄非數字的輸入
        for i in a:
            try:
                num_ar.append(int(i))
            except:
                print("有非數字的輸入")
                continue
        print(num_ar)
        # assert game(3,10) == 2
        # assert game(10,0) == 10
        # assert game(10,1) == 1
        AssertCode_Processer.AssertCode([(3,10), (10,0)])
        # unmutate_ans = ''
        # mutated_ans = ''
        # unmutate_ans = T35.T35(int(request.POST['Num']))
        # mutated_ans = mutateT35.T35(int(request.POST['Num']))
        # print(unmutate_ans, mutated_ans, request.POST['Num'])
        # print(unmutate_ans, mutated_ans)
        # T35.T35(int(request.POST['Num']))
        return JsonResponse({'ans1':"Testing",'ans2':"Testing"})
        # return JsonResponse({'ans1':unmutate_ans,'ans2':mutated_ans})
    return render(request, 'mutation_test/diff_1.html')

#Level-2題目處理
def diff_2(request):
    
    return render(request, 'mutation_test/diff_2.html')

#Level-3題目處理
def diff_3(request):
    return render(request, 'mutation_test/diff_3.html')

def ajax(request):
    return render(request, 'mutation_test/diff_1.html', {'suc' : success})

# 小工具下載路徑
from urllib import parse
def tool_download(request):
    Zip = '/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_guitool.zip'
    z_file = open(Zip, 'rb')
    data = z_file.read()
    z_file.close()
    # os.remove(z_file.name)
    response = HttpResponse(data, content_type='application/zip')
    
    response['Content-Disposition'] = 'attachment;filename=' + parse.quote("guitool.zip ")
    return response


#暫定沒有
# def login(request):
#     return render(request, 'register/login.html')

# def register(request):
#     return render(request, 'register/register.html')

