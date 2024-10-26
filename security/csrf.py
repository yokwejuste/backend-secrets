from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        pass
    return render_template('wtf_template.html')


@csrf_exempt
def my_view(request):
    return HttpResponse("This view is CSRF exempt")


if __name__ == "__main__":
    app.run()
