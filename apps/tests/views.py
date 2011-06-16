from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from apps.tests.models import Test, Comment
from apps.tests.forms import TestForm
from django.contrib.auth.decorators import login_required

def list(request):
    tests = Test.objects.all()#SELECT * FROM TEST;
    
    rc = RequestContext(request,{'tests':tests,'title':'List of Tests'})
    return render_to_response('tests/list.html',rc)

@login_required
def create_test(request):
    test = Test(author=request.user)
    if request.method == 'POST':
        form = TestForm(request.POST,instance=test)
        if form.is_valid():
            form.save()
            test.save()
            return HttpResponseRedirect(reverse('list'))
    else:
        form  = TestForm(instance=test)
        
    rc = RequestContext(request,{'form':form})
    return render_to_response('tests/create.html',rc)

def edit_test(request,test_id):
    test = get_object_or_404(Test,pk=test_id)
    if request.method == 'POST':
        form = TestForm(request.POST,instance=test)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('view',args=test_id))
    else:
        form  = TestForm(instance=test)
        
    rc = RequestContext(request,{'form':form,'test':test})
    return render_to_response('tests/edit.html',rc)

def view_test(request,test_id):
    test = get_object_or_404(Test,pk=test_id)
    
    if request.method == 'POST':
        comment = Comment(
            test=test,
            author=request.user,
            comment=request.POST['comment'],
        )
        # if this is a reply to a comment, not to a post
        if request.POST['parent_id'] != '':
            comment.parent = Comment.objects.get(id=request.POST['parent_id'])
        comment.save()
    
    comments = Comment.objects.filter(test=test)
    
    rc = RequestContext(request,{'test':test,'comments':comments})
    return render_to_response('tests/view.html',rc)

def remove_test(request,test_id):
    test = get_object_or_404(Test,pk=test_id)
    test.delete()
    return HttpResponseRedirect(reverse('list'))