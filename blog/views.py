from django.shortcuts import render

# ここにあなたのビューを書く。
def post_list(request):
    return render(request, 'blog/post_list.html', {})
