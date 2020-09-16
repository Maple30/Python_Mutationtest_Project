import sys, datetime, time
import traceback
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool")
import mutation
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/T35")
import T35, mutateT35
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_1/")
import AssertCode_Processer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from .forms import UploadFileForm
# filehandler = __import__("/mutation_test/file_handler")
import mutation_test.file_handler as fh

# 確認變數是否已經定義
def isset(v):
    try :
        type (eval(v)) 
    except : 
        return  0  
    else :
        return  1

def index(request):
    # print(fh.handle_uploaded_file())
    # return TemplateResponse(request, template_name, args)
    return render(request,'mutation_test/index.html')

    # return HttpResponse(ans)
    # Create your views here.

#Level-1題目處理
def diff_1(request):
    global timepoint
    if (isset('timepoint')):
        print("timepoint={timepoint}".format(timepoint = timepoint))
        now = datetime.datetime.now()
        print("nowtime={nowtime}".format(nowtime = now))
        delta = time.mktime(now.timetuple()) - time.mktime(timepoint.timetuple())
        print(delta)
        timeArray = time.localtime(delta)
        timecout = time.strftime("%M:%S", timeArray)
        print(timecout)
        return render(request, 'mutation_test/diff_1.html',{"timecout":timecout})
    else:
        timepoint = datetime.datetime.now()
        print ("timepoint = {timepoint}".format(timepoint=timepoint))

    if request.method == 'POST':
        
        # print(request.POST['input'])
        #分割字串
        a = request.POST['input'].split(',')
        # print(a)

        num_ar = []
        #捨棄非數字的輸入
        for i in a:
            try:
                num_ar.append(int(i))
            except:
                print("有非數字的輸入")
                continue
        # print(num_ar)

        output_string, killper = AssertCode_Processer.AssertCode([(3,10), (10,0)])
        # print(output_string, killper)

        return JsonResponse({'ans1':"Testing",'ans2':"Testing"})
    
    return render(request, 'mutation_test/diff_1.html')

def diff_1_load(request):
    basedir = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/"
    all_shukudai = []
    
    for i in range(1,4):
        with open(basedir + "test_{num}.py".format(num=i), "r", encoding="UTF-8") as file:
            all_shukudai.append(file.read())
    # for i in all_shukudai:
        # print(i)

    return JsonResponse({'all_shukudai' : all_shukudai})

#Level-2題目處理
def diff_2(request):
    return render(request, 'mutation_test/diff_2.html')

#Level-3題目處理
def diff_3(request):
    return render(request, 'mutation_test/diff_3.html')

# 測試ajax用的
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

