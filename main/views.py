from django.shortcuts import render
from . models import todoSchema
from . forms import addTodoForm
from django.http import HttpResponse
from django.views.generic.edit import DeleteView



def todo_list(request):
    todos = todoSchema.objects.all().order_by("-created")
    form = addTodoForm(request.POST)
    if request.method == 'POST':
        form = addTodoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = addTodoForm
    else:
        HttpResponse('couldnt add item')
    return render(request, 'main/index.html',{'todos':todos, 'form':form})

class DeleteTodo(DeleteView):
    model = todoSchema
    success_url = '/'
# def post_blog(request):
#     form = blog_p
#     if request.method == 'POST':
#         form = blog_p(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             form.save()
#             return redirect('news_feed')
#         else:
#             form = blog_p
#     return render(request, 'main/post.html', {'form':form})
