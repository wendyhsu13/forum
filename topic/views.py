from django.views.generic import *
from django.urls import reverse
from .models import *
from datetime import datetime

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

    def get_context_data(self, **kwargs):
        # 取得回覆資料傳給頁面範本處理
        ctx = super().get_context_data(**kwargs)
        ctx['reply_list'] = Reply.objects.filter(topic=self.object)
        return ctx

# 回覆討論主題
class TopicReply(CreateView):
    model = Reply
    fields = ['content']
    template_name = 'topic/topic_form.html'

    def form_valid(self, form):
        topic = Topic.objects.get(id=self.kwargs['tid'])
        form.instance.topic = topic
        form.instance.author = self.request.user
        topic.replied = datetime.now()  # 更新討論主題回覆時間
        topic.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('topic_view', args=[self.kwargs['tid']])