from django.views.generic import *
from django.urls import reverse
from .models import *

# 討論主題列表
class TopicList(ListView):
    model = Topic
    ordering = ['-created']
    paginate_by = 20        # 每頁主題數

# 新增討論主題
class TopicNew(CreateView):
    model = Topic
    fields = ['subject', 'content']

    def get_success_url(self):
        return reverse('topic_list')

    def form_valid(self, form):
        # 自動將目前使用者填入討論主題的作者欄
        form.instance.author = self.request.user
        return super().form_valid(form)

# 檢視討論主題
class TopicView(DetailView):
    model = Topic