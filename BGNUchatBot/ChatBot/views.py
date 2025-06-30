from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import search_similar_chunks
from .deepseek_api import ask_deepseek

class AskBot(APIView):
    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "No question provided"}, status=400)

        try:
            context = search_similar_chunks(question)
            answer = ask_deepseek(question, context)
            return Response({"answer": answer})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
