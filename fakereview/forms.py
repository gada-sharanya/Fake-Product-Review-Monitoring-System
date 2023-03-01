from django.forms import Form, CharField, PasswordInput, FileField

class RegistrationForm(Form):

    username =CharField(max_length=50)
    name = CharField(max_length=50)
    password =CharField(max_length=50)
    email =CharField(max_length=50)
    mobile =CharField(max_length=50)
    address =CharField(max_length=50)

class LoginForm(Form):

    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())

class ProductForm(Form):

    name = CharField(max_length=30)
    price = CharField(max_length=30)
    manufacturer =CharField(max_length=30)
    category = CharField(max_length=30)
    description = CharField(max_length=300)
    path = FileField()

class CommentForm(Form):

    text = CharField(max_length=5000)
    product = CharField(max_length=60)

class SearchHistoryForm(Form):

    keyord = CharField(max_length=300)

class LikeOrDisLikeForm(Form):

    likeOrDislike = CharField(max_length=100)
    product = CharField(max_length=60)