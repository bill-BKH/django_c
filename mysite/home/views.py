from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home_page(request):
    books = [{'name':'آموزش پایتون', 'price':'200','author':'rostam','image':'https://roberoshd.ir/wp-content/uploads/2020/11/6e4f96489e2498467db28dadccfe019e4292f52d.jpg'},
             {'name':'کتاب C#', 'price':100,'author':'karim','image':'https://fidibo.com/blog/wp-content/uploads/2022/02/Untitled-1-1.jpg'}]

    return render(request, 'home.html',{'data':books})

def BMI(hight, weight):
    bmi = weight / (hight* hight)
    
    if bmi < 18:
        return bmi
    elif bmi < 24:
        return 'normal',bmi
    elif bmi < 29:
        return 'chagi',bmi
    else:
        return 'boro basgah',bmi

def calc_age(request):
    if request.method == 'POST':
        h = request.POST.get('gad') # h='1.83'
        w = request.POST.get('vazn') # w='85'
        javab = BMI(float(h),int(w))

        return render(request,'calc_age.html',{'sen':javab})
    return render(request,'calc_age.html')
    