from articles.models import Articles
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            pass
        else:
            article_id = request.GET.get('article')
            article_content = Articles.objects.filter(article_id=article_id).values('article_id', 'article_title',
                                                                                'article_summary', 'article_content',
                                                                                'article_published_date'
                                                                                )[0]
        # print(article_content, 'article')
        return Response(article_content)


article_detail = ArticleView.as_view()


class CreateArticleView(APIView):
    def post(self, request, *args, **kwargs):
        article = {}
        if request.method == 'GET':
            pass
        else:
            for k, v in request.data.items():
                article[k] = v

            Articles.objects.create(
                article_title=article['articleTitle'],
                article_summary=article['articleSummary'],
                article_content=article['articleContent']
            )
            return Response('Ok', status=status.HTTP_200_OK)


create_article = CreateArticleView.as_view()

