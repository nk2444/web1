from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import CommentForms
def details(request, slug):
        post = get_object_or_404(Post, slug=slug)
        
        if request.method == 'POST':
                form=CommentForms(request.POST)

                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.post=post
                    comment.save()

                    return redirect('post_details',slug=slug)

        else:
                form = CommentForms()
        
        return render(request,'blog/details.html', {'post':post, 'form':form})

