import sys, datetime, time, random
import traceback
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_tool")
import mutation
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/T35")
import T35, mutateT35
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_1/")
import AssertCode_Processer1
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_2/")
import AssertCode_Processer2
sys.path.append("/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/shukudai/diff_3/")
import AssertCode_Processer3
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

# 輸入10, 9 , 8
#Level-1題目處理
def diff_1(request, bangou=0):

    # 建立不重複的數字list與紀錄對應時間的字典檔
    try:
        print(diff_1.Num_list)
    except AttributeError:
        diff_1.Num_list = []
        diff_1.Num_dic = dict()

        for i in range(1,1001):
            diff_1.Num_list.append(str(i))
        # print(diff_1.Num_list)

    if request.method == 'POST':
        # print(request.POST['input'])
        #分割字串
        # print(request.POST)
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
        print(num_ar)
        if num_ar == []:
            return JsonResponse({"no_input": "請輸入測試資料"})
        output_string, killper, kill_status_record = AssertCode_Processer1.AssertCode(num_ar)
        # output_string, killper, kill_status_record = AssertCode_Processer1.AssertCode([("12234"), ("214124")])
        # print(output_string)
        # print(output_string, killper)
        
        return JsonResponse({'output_string':output_string, 'killper': killper, "kill_status_record": kill_status_record})

    elif request.method == 'GET':
        #bangou=0代表是第一次進入網頁
        if(bangou == 0):
            # Num 是指派給使用者的數字
            Num = diff_1.Num_list[0]
            # 將此數字記錄到字典裡
            diff_1.Num_dic[diff_1.Num_list[0]] = ''
            # print(diff_1.Num_dic)
            del diff_1.Num_list[0]
            return redirect('/diff_1/'+Num)
        else:
        # 抓時間出來
            print(bangou)
            print('diff_dic = ',diff_1.Num_dic)
            
            try:
                if diff_1.Num_dic[bangou] == '':
                    diff_1.Num_dic[bangou] = datetime.datetime.now()
                    now = datetime.datetime.now()
                    print(diff_1.Num_dic[bangou])
                    time_subtract = time.mktime(now.timetuple()) - time.mktime(diff_1.Num_dic[bangou].timetuple())
                    timeArray = time.localtime(time_subtract)
                    timecout = time.strftime("%M:%S", timeArray)

                else:
                    now = datetime.datetime.now()
                    time_subtract = time.mktime(now.timetuple()) - time.mktime(diff_1.Num_dic[bangou].timetuple())
                    timeArray = time.localtime(time_subtract)
                    timecout = time.strftime("%M:%S", timeArray)

                return render(request, 'mutation_test/diff_1.html',{"timecout":timecout, "bangou":bangou})
            except Exception as e:
                error_class = e.__class__.__name__ #取得錯誤類型
                detail = e.args[0] #取得詳細內容
                cl, exc, tb = sys.exc_info() #取得Call Stack
                lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                fileName = lastCallStack[0] #取得發生的檔案名稱
                lineNum = lastCallStack[1] #取得發生的行號
                funcName = lastCallStack[2] #取得發生的函數名稱
                errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                print(errMsg)
                # pass
            
            return render(request, 'mutation_test/diff_1.html',{"error":"請回到首頁"})


def diff_1_load(request):
    basedir = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/"
    all_shukudai = []
    
    for i in range(1,4):
        with open(basedir + "test_{num}.py".format(num=i), "r", encoding="UTF-8") as file:
            all_shukudai.append(file.read())
    # for i in all_shukudai:NNNN
        # print(i)
    print(1)

    return JsonResponse({'all_shukudai' : all_shukudai})

#Level-2題目處理
def diff_2(request,bangou=0):
        # 建立不重複的數字list與紀錄對應時間的字典檔
    try:
        print(diff_2.Num_list)
    except AttributeError:
        diff_2.Num_list = []
        diff_2.Num_dic = dict()

        for i in range(1,1001):
            diff_2.Num_list.append(str(i))
        # print(diff_1.Num_list)

    if request.method == 'POST':
        # print(request.POST['input'])
        #分割字串
        # print(request.POST)
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
        print(num_ar)
        if num_ar == []:
            return JsonResponse({"no_input": "請輸入測試資料"})
        output_string, killper, kill_status_record = AssertCode_Processer2.AssertCode(num_ar)
        # output_string, killper, kill_status_record = AssertCode_Processer1.AssertCode([("12234"), ("214124")])
        # print(output_string)
        # print(output_string, killper)
        
        return JsonResponse({'output_string':output_string, 'killper': killper, "kill_status_record": kill_status_record})

    elif request.method == 'GET':
        #bangou=0代表是第一次進入網頁
        if(bangou == 0):
            # Num 是指派給使用者的數字
            Num = diff_2.Num_list[0]
            # 將此數字記錄到字典裡
            diff_2.Num_dic[diff_2.Num_list[0]] = ''
            # print(diff_1.Num_dic)
            del diff_2.Num_list[0]
            return redirect('/diff_2/'+Num)
        else:
        # 抓時間出來
            # print(bangou)
            # print('diff_dic = ',diff_2.Num_dic)
            
            try:
                if diff_2.Num_dic[bangou] == '':
                    diff_2.Num_dic[bangou] = datetime.datetime.now()
                    now = datetime.datetime.now()
                    # print(diff_2.Num_dic[bangou])
                    time_subtract = time.mktime(now.timetuple()) - time.mktime(diff_2.Num_dic[bangou].timetuple())
                    timeArray = time.localtime(time_subtract)
                    timecout = time.strftime("%M:%S", timeArray)
                else:
                    now = datetime.datetime.now()
                    time_subtract = time.mktime(now.timetuple()) - time.mktime(diff_2.Num_dic[bangou].timetuple())
                    timeArray = time.localtime(time_subtract)
                    timecout = time.strftime("%M:%S", timeArray)

                return render(request, 'mutation_test/diff_2.html',{"timecout":timecout, "bangou":bangou})
            except Exception as e:
                error_class = e.__class__.__name__ #取得錯誤類型
                detail = e.args[0] #取得詳細內容
                cl, exc, tb = sys.exc_info() #取得Call Stack
                lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                fileName = lastCallStack[0] #取得發生的檔案名稱
                lineNum = lastCallStack[1] #取得發生的行號
                funcName = lastCallStack[2] #取得發生的函數名稱
                errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                print(errMsg)
                # pass
            
            return render(request, 'mutation_test/diff_2.html',{"error":"請回到首頁"})

def diff_2_load(request):
    basedir = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/"
    all_shukudai = []
    
    for i in range(1,7):
        with open(basedir + "test_{num}.py".format(num=i), "r", encoding="UTF-8") as file:
            all_shukudai.append(file.read())
    # for i in all_shukudai:NNNN
        # print(i)
    print(all_shukudai)

    return JsonResponse({'all_shukudai' : all_shukudai})
#Level-3題目處理
def diff_3(request, bangou=0):
    # 建立不重複的數字list與紀錄對應時間的字典檔
    try:
        print(diff_3.Num_list)
    except AttributeError:
        diff_3.Num_list = []
        diff_3.Num_dic = dict()

        for i in range(1,1001):
            diff_3.Num_list.append(str(i))
        # print(diff_1.Num_list)

    if request.method == 'POST':
        # print(request.POST['input'])
        #分割字串
        # print(request.POST)
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
        print(num_ar)
        if num_ar == []:
            return JsonResponse({"no_input": "請輸入測試資料"})
        output_string, killper, kill_status_record = AssertCode_Processer3.AssertCode(num_ar)
        # output_string, killper, kill_status_record = AssertCode_Processer1.AssertCode([("12234"), ("214124")])
        # print(output_string)
        # print(output_string, killper)
        
        return JsonResponse({'output_string':output_string, 'killper': killper, "kill_status_record": kill_status_record})

    elif request.method == 'GET':
        #bangou=0代表是第一次進入網頁
        if(bangou == 0):
            # Num 是指派給使用者的數字
            Num = diff_3.Num_list[0]
            # 將此數字記錄到字典裡
            diff_3.Num_dic[diff_3.Num_list[0]] = ''
            # print(diff_1.Num_dic)
            del diff_3.Num_list[0]
            return redirect('/diff_3/'+Num)
        else:
        # 抓時間出來
            # print(bangou)
            # print('diff_dic = ',diff_3.Num_dic)
            
            try:
                if diff_3.Num_dic[bangou] == '':
                    diff_3.Num_dic[bangou] = datetime.datetime.now()
                    now = datetime.datetime.now()
                    # print(diff_3.Num_dic[bangou])
                    time_subtract = time.mktime(now.timetuple()) - time.mktime(diff_3.Num_dic[bangou].timetuple())
                    timeArray = time.localtime(time_subtract)
                    timecout = time.strftime("%M:%S", timeArray)

                else:
                    now = datetime.datetime.now()
                    time_subtract = time.mktime(now.timetuple()) - time.mktime(diff_3.Num_dic[bangou].timetuple())
                    timeArray = time.localtime(time_subtract)
                    timecout = time.strftime("%M:%S", timeArray)

                return render(request, 'mutation_test/diff_3.html',{"timecout":timecout, "bangou":bangou})
            except Exception as e:
                error_class = e.__class__.__name__ #取得錯誤類型
                detail = e.args[0] #取得詳細內容
                cl, exc, tb = sys.exc_info() #取得Call Stack
                lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                fileName = lastCallStack[0] #取得發生的檔案名稱
                lineNum = lastCallStack[1] #取得發生的行號
                funcName = lastCallStack[2] #取得發生的函數名稱
                errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                print(errMsg)
                # pass
            
            return render(request, 'mutation_test/diff_3.html',{"error":"請回到首頁"})

def diff_3_load(request):
    basedir = "/mnt/c/Users/st096/Desktop/Python_Test_Project/source_code/mutation_test_game/"
    all_shukudai = []
    
    for i in range(1,10):
        with open(basedir + "test_{num}.py".format(num=i), "r", encoding="UTF-8") as file:
            all_shukudai.append(file.read())
    # for i in all_shukudai:NNNN
        # print(i)

    return JsonResponse({'all_shukudai' : all_shukudai})

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