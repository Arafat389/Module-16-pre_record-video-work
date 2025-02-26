from django.shortcuts import render,HttpResponse,redirect

from .import models
from . import forms
from django.contrib import messages
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy

# Create your views here.

# three types of forms in django
"""
1. HTML Form
2.Form API
3. Model Form

"""

#  # this is for HTML form
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')


#         if checkbox == 'on':
#             checkbox = True

#         else:
#             checkbox = False    

#         student = models.Student(name=name, email=email, phone=phone,password=password, checkbox=checkbox, photo=photo)  # Student class er ekta object toiri korlam

#         student.save()  # student table ekta recort toiri korlam
#         return HttpResponse("Student object created successfully")
    
#     return render(request,'student/index.html')




# # this is model Form
# # This field is required. ar kaj
# # for function base CreateStudentView
def create_student(request):
    
    if request.method == 'POST':  # 1 user post request koreche
        form = forms.StudentForm(request.POST,request.FILES) # 2 user post request captcher koretche
        if form.is_valid(): # 3 user input validation kortece
            form.save() # 4 user input save kortece
            messages.add_message(request,messages.SUCCESS,"Student Created Successfully.")
            return redirect('home')
        
    else:
        form = forms.StudentForm()
    return render(request,'student/create_edit_student.html',{'form':form})

# # for Class base CreateStudentView

class CreateStudentData(CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_edit_student.html'

    def form_valid(self, form):
        messages.add_message(self.request,messages.SUCCESS,"Student Created Successfully.")
    
        return super().form_valid(form)

# for function base ListView

def home(request):
    students = models.Student.objects.all()
    return render(request,'student/index.html',{'students':students})


# for class base ListView

class StudentLists(ListView):
    model =models.Student
    template_name = 'student/index.html'
    context_object_name = 'students'


# for function base UpdateView
def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student) # user ar ager data deye form fill up korlam
    # form = forms.StudentForm()
    if request.method == 'POST':  # 1 user post request koreche
        form = forms.StudentForm(request.POST,request.FILES, instance=student) # 2 user post request captcher koretche
        if form.is_valid(): # 3 user input validation kortece
            form.save() # 4 user input save kortece
            messages.add_message(request,messages.SUCCESS,"Student Updated Successfully.")
            return redirect('home')

    return render(request,'student/create_edit_student.html',{'form': form, 'edit': True})


# for class base UpdateView

class UpdateStudentData(UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = 'student/create_edit_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.add_message(self.request,messages.SUCCESS,"Student Updated Successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context
       
       


#  For function base DeleteView

def delete_student(request,id):
    student = models.objects.get(id=id) # id= id wala student ke khoje ber korlam. abong tar object pelam
    student.delete() # oi student object delete korlam
    messages.add_message(request,messages.SUCCESS,"Student Deleted Successfully.")
    return redirect('home') # successful hole take home page redirect kore dao
        

#  For class base DeleteView

class DeleteStudentDate(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'

def delete(self, request, *args, **kwargs):
    messages.add_message(request,messages.SUCCESS,"Student Deleted Successfully.")
    return super().delete(request, *args, **kwargs)