import openai
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from io import BytesIO
from PIL import Image

# Set up OpenAI API key (ensure this is kept secure and not exposed in code)
openai.api_key = "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"

# Home view to respond to the root URL
def home(request):
    return HttpResponse("Welcome to the Image Generator API")

# Generate image using OpenAI API
@csrf_exempt  # Disable CSRF for simplicity, but consider enabling it for production
def generate_image(request):
    if request.method == "POST":
        try:
            # Parse the request body
            body = json.loads(request.body)
            prompt = body.get("prompt")

            if not prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)

            # Call OpenAI API to generate an image
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )

            # Get the generated image URL
            image_url = response['data'][0]['url']
            return JsonResponse({"image_url": image_url})

        except openai.error.OpenAIError as e:
            return JsonResponse({"error": f"OpenAI API Error: {str(e)}"}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected Error: {str(e)}"}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=400)
