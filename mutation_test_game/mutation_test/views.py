import sys, datetime, time, random
import traceback
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool")
import mutation
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/T35")
import T35, mutateT35
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_1/")
import AssertCode_Processer
from django.shortcuts import render, redirect
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
    
    # 建立不重複的數字list與紀錄對應時間的字典檔
    try:
        print(diff_1.Num_list)
    except AttributeError:
        diff_1.Num_list = []
        diff_1.Num_dic = dict()
        for i in range(1,1001):
            diff_1.Num_list.append(str(i))
        print(diff_1.Num_list)
    
    try:
        if Num_dic[request.Get['bangou']] == '':
            
            Num_dic[request.Get['bangou']] = datetime.datetime.now()
            now = datetime.datetime.now()
            time_subtract = time.mktime(now.timetuple()) - time.mktime(Num_dic[request.Get['bangou']])
            timeArray = time.localtime(time_subtract)
            timecout = time.strftime("%M:%S", timeArray)

            return render(request, 'mutation_test/diff_1.html',{"timecout":timecout})
        else:
            now = datetime.datetime.now()
            time_subtract = time.mktime(now.timetuple()) - time.mktime(Num_dic[request.Get['bangou']])
            timeArray = time.localtime(time_subtract)
            timecout = time.strftime("%M:%S", timeArray)

            return render(request, 'mutation_test/diff_1.html',{"timecout":timecout})
    except:
        pass

    # # 如果timepoint已被宣告代表使用者進入此頁面了
    # if (isset('timepoint') and request.method != 'POST'):
    #     # print("timepoint={timepoint}".format(timepoint = timepoint))
    #     now = datetime.datetime.now()
    #     print("nowtime={nowtime}".format(nowtime = now))
    #     time_subtract = time.mktime(now.timetuple()) - time.mktime(timepoint.timetuple())
    #     # print(time_subtract)
    #     timeArray = time.localtime(time_subtract)
    #     timecout = time.strftime("%M:%S", timeArray)
    #     # print(timecout)
    #     print("奇怪")
    #     return render(request, 'mutation_test/diff_1.html',{"timecout":timecout})
    # else:
    #     timepoint = datetime.datetime.now()
        
        # print ("timepoint = {timepoint}".format(timepoint=timepoint))

    # 使用者輸入資料的情況
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
        if True:
            now = datetime.datetime.now()
            time_subtract = time.mktime(now.timetuple()) - time.mktime(timepoint.timetuple())
            print(time_subtract)

        output_string, killper = AssertCode_Processer.AssertCode([(3,10), (10,0)])
        # print(output_string, killper)

        return JsonResponse({'ans1':"Testing",'ans2':"Testing"})
    
    # Num 是指派給使用者的數字
    Num = diff_1.Num_list[0]
    # 將此數字記錄到字典裡
    diff_1.Num_dic[diff_1.Num_list[0]] = ''
    del diff_1.Num_list[0]

    return redirect('/diff_1?bangou=' + Num)
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