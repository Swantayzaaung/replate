# What is replate
Replate is a responsive web application built in Django that allows users to scan their food via camera, or input the name as text. Then, it sends the information to ChatGPT and lets them get suggestions on what to do with their leftover food, rather than spend time search various ways for each food item. I believe that by creating this simple project, I could help reduce food waste on an individual level as people could more conveniently find out ways to reuse leftover food, which is often in perfectly good condition.

<table>
  <tr>
    <th>Tools used</th>
    <th>How this web app works</th>
  </tr>
  <tr>
    <td>
      <ul>
        <li><b>Web application</b>: Django Framework with Python</li>
        <li><b>Webpages</b>: HTML, CSS, Javascript</li>
        <li><b>Image detection</b>: <a href="https://www.clarifai.com/">Clarifai API</a></li>
        <li><b>Sending answers</b>: <a href="https://openai.com/">ChatGPT API</a></li>
        <li><b>Drawing UI Design</b>: <a href="https://figma.com">Figma</a></li>
      </ul>
    </td>
    <td>
      <ol>
        <li>First, it asks the user to input a picture of food, or enter its name as text.</li>
        <li>If it's an image, then the data is sent to Clarifai API to detect what food it contains. If it's text, then the text is uploaded directly.</li>
        <li>The data for the food is then sent to ChatGPT's API to ask for suggestions on how to reuse the leftover food.</li>
        <li>The suggestions from ChatGPT is output back to the user's browser.</li>
      </ol>
    </td>
  </tr>
</table>

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
