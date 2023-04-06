from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage 
from .detection import get_tags, ask_food_suggestions, put_and_in_array
from PIL import Image
import os

# Create your views here.
# For the index page (the homepage)
def index(request):
    return render(request, "replate_app/index.html")

# Function to compress a file
def compress(img_path): # Use an absolute path for image in here
    image = Image.open(img_path)
    image.save(img_path,
               "JPEG",
               optimize=True,
               quality = 10)
    return

# For the scanning page
def scan(request):
    # If user uploads a file
    if request.method == "POST":
        # Check the method for image or text
        if request.POST['method'] == 'image':
            # Check if the file is valid
            if request.FILES['file']:
                # Handle file upload, save it to a media directory
                upload = request.FILES['file']
                fss = FileSystemStorage()
                file = fss.save(upload.name, upload)
                og_url = fss.url(file)
                img_url = os.path.abspath(os.getcwd() + og_url)

                is_img = True
                try:
                    # Compress the image before saving
                    compress(img_url)
                except:
                    # If the program gives exception when it's not an image
                    foodlist = [{"name": "File is not an image", "value": 0}]
                    suggestions = "File is not an image, please upload an image file"
                    og_url = '/static/replate_app/error.png'
                    is_img = False

                if is_img == True:
                    # Create a list of food tags by sending the image to the Clarifai AI's API
                    try:
                        foodlist = get_tags(img_url)
                        # Create a list of food items
                        food_items = [food["name"] for food in foodlist]
                        suggestions = ask_food_suggestions(food_items)["content"].replace('\n', '<br>')
                        # Show error if food list does not have relevant food items
                        if len(foodlist) == 0:
                            foodlist = [{"name": "No food found", "value": 0}]
                            suggestions = "Error: unable to find food items in the uploaded image"
                    # If the AI is unable to get a list, show an error
                    except:
                        foodlist = [{"name": "No food found", "value": 0}]
                        suggestions = "Error: unable to find food items in the uploaded image"

                # Render the results with the list of foods and the suggestions
                return render(request, "replate_app/results.html", {
                    'foodlist': foodlist,
                    'suggestions': suggestions,
                    'img_url': og_url,
                    'method': 'image'
                })
        else:
            # For text-based inputs
            food_name = request.POST["food-name"] # Get food name
            suggestions = ask_food_suggestions(food_name)["content"].replace('\n', '<br>') # Get suggestions from ChatGPI API
            return render(request, "replate_app/results.html", {
                'foodname': food_name,
                'suggestions': suggestions,
                'method': 'text'
            })
    # Render the scan page by default
    else:
        return render(request, "replate_app/scan.html")

# Render an about page
def about(request):
    return render(request, "replate_app/about.html")