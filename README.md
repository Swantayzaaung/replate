# What is replate
Replate is a responsive web application built in Django that allows users to scan their food via camera, or input the name as text. Then, it sends the information to ChatGPT and lets them get suggestions on what to do with their leftover food, rather than spend time search various ways for each food item. I believe that by creating this simple project, I could help reduce food waste on an individual level as people could more conveniently find out ways to reuse leftover food, which is often in perfectly good condition.

# How to run this web application
As of now, due to time constraints, I haven't been able to deploy the web application on an Internet website. If I get the time, I will make sure to deploy it and share the URL here.

In order to deploy the web application locally on your device, please install the necessary python libraries:

```pip install -r requirements.txt```

If that doesn't work properly, you may install each package individually
```
pip install clarifai_grpc
pip install Django
pip install django-admin
pip install openai
pip install Pillow
```

Once you have installed the necessary libraries, you may run the web application on your local computer by running:

```python manage.py runserver```

You may then click on the IP address provided in the Django output and open it in your web browser to access the web application.
