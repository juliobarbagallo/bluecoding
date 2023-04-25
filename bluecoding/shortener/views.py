from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer
import uuid

class ShortenURLView(APIView):
    def post(self, request):
        long_url = request.data.get('long_url')
        if long_url:
            shortened_url = ShortenedURL.objects.filter(long_url=long_url).first()
            if shortened_url:
                short_url = request.build_absolute_uri('/') + shortened_url.short_url
            else:
                short_url = str(uuid.uuid4())[:8]
                shortened_url = ShortenedURL(long_url=long_url, short_url=short_url)
                shortened_url.save()
                short_url = request.build_absolute_uri('/') + shortened_url.short_url
            serializer = ShortenedURLSerializer(shortened_url)
            return Response({'short_url': short_url, 'shortened_url': serializer.data})
        else:
            return Response({'error': 'long_url field is required'}, status=400)
