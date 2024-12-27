from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from articles.models import Article 
from .models import Profile


def users(request):
    return render(request, "users/users.html")

# Create your views here.

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    liked_articles = member.like_articles.all()
    authored_articles = Article.objects.filter(author=member)
    
    context = {
        "member" : member,
        "liked_articles": liked_articles,
        "authored_articles": authored_articles,
        
    }
    return render(request, "users/profile.html", context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", username=member.username)    
    return redirect("accounts:login")


