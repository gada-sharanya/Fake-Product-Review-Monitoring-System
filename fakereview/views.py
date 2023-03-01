from django.shortcuts import render

from fakereview.fakereviewanalysis import isTruthFullComment
from fakereview.forms import RegistrationForm, LoginForm, ProductForm, CommentForm, LikeOrDisLikeForm
from fakereview.models import RegistrationModel, ProductModel, CommentModel, LikeOrDisLikeModel, SearchHistoryModel, \
    TransactionModel
from fakereview.service import getAllProducts


def registration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = RegistrationForm(request.POST)

        if registrationForm.is_valid():

            regModel = RegistrationModel()
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]

            user = RegistrationModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'index.html', locals())
    else:
        response = render(request, 'registration.html', {"message": "User All Ready Exist"})

    return response

def login(request):
    uname = ""
    upass = ""
    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]

            if uname == "admin" and upass == "admin":
                request.session['username'] = "admin"
                request.session['role'] = "admin"

                return render(request, "products.html", {"products": getAllProducts()})

        user = RegistrationModel.objects.filter(username=uname, password=upass).first()

        if user is not None:
            request.session['username'] = uname
            request.session['role'] = "user"
            return render(request, "products.html", {"products":getAllProducts()})
        else:
            response = render(request, 'index.html', {"message": "Invalid Credentials"})

    return response

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})


def postProduct(request):

    status = False

    productForm = ProductForm(request.POST, request.FILES)

    if productForm.is_valid():

        name = productForm.cleaned_data['name']
        price = productForm.cleaned_data['price']
        manufacturer = productForm.cleaned_data['manufacturer']
        category = productForm.cleaned_data['category']
        description = productForm.cleaned_data['description']
        path = productForm.cleaned_data['path']

        new_product = ProductModel(name=name,price=price,manufacturer=manufacturer,category=category,description=description,path=path)

        try:
            new_product.save()
            status = True
        except:
            status = False

    if status:
        return render(request, "products.html", {"products":getAllProducts()})
    else:
        response = render(request, 'postproduct.html', {"message": "Product Upload Failed"})

    return response

def getProducts(request):
    return render(request, "products.html", {"products":getAllProducts()})

def search(request):

    str = request.GET["query"]

    resultProducts=[]

    if str!="":

        for productBean in getAllProducts():

            if str in productBean.product.name or str in productBean.product.description:
                resultProducts.append(productBean)

        history=SearchHistoryModel(keyword=str,user=request.session['username'])
        history.save()

    return render(request, 'products.html', {'products': resultProducts})

def postComment(request):

    form = CommentForm(request.POST)

    if form.is_valid():

        text = form.cleaned_data['text']
        product_id = request.POST['product']

        istruthfull=isTruthFullComment(text)

        print("is truthfull:",istruthfull)

        new_comment = CommentModel(text=text, user=request.session['username'], product=product_id,istruthfull=istruthfull)
        new_comment.save()

        return render(request, "products.html", {"products":getAllProducts()})

    return render(request, "products.html", {"products": getAllProducts()})

def likeOrDisLike(request):

    form = LikeOrDisLikeForm(request.GET)

    if form.is_valid():

        ld = form.cleaned_data['likeOrDislike']
        product_id = form.cleaned_data['product']

        islikedOrDisLiked = LikeOrDisLikeModel.objects.filter(user=request.session['username'],
                                                              product=product_id).count()

        if islikedOrDisLiked == 1:
            LikeOrDisLikeModel.objects.filter(user=request.session['username'],
                                              product=product_id).update(status=ld)
        else:
            new_likeOrDisLike = LikeOrDisLikeModel(status=ld, user=request.session['username'], product=product_id)
            new_likeOrDisLike.save()

        return render(request, "products.html", {"products": getAllProducts()})

def getRecomendedProducts(request):

    searches=SearchHistoryModel.objects.filter(user=request.session['username'])

    resultProducts = set()

    for search in searches:

        for productBean in getAllProducts():

            if search.keyword in productBean.product.name or search.keyword in productBean.product.description:

                resultProducts.add(productBean)

    return render(request, 'products.html', {'products': resultProducts})

def getRecentProducts(request):

    resultProducts = []

    most_recent_products = ProductModel.objects.order_by('-datetime')[:8]

    recentList=[]

    for recent in most_recent_products:
        recentList.append(recent.id)

    for productBean in getAllProducts():
        if productBean.product.id in recentList:
            resultProducts.append(productBean)

    return render(request, 'products.html', {'products': resultProducts})

def deleteProduct(request):

    product_id= request.GET['product']

    ProductModel.objects.filter(id=product_id).delete()

    for comment in CommentModel.objects.filter(product=product_id):
        CommentModel.objects.filter(id=comment.id).delete()

    for likedislike in LikeOrDisLikeModel.objects.filter(product=product_id):
        LikeOrDisLikeModel.objects.filter(id=likedislike.id).delete()

    return render(request, 'products.html', {'products': getAllProducts()})

def buyProduct(request):
    product=ProductModel.objects.get(id=request.GET['product'])
    product.path = str(product.path).split("/")[1]
    return render(request, 'buyproduct.html', {'product':product})

def buyProductAction(request):
    transaction=TransactionModel(userid=request.session['username'],productid=request.GET['product'],status="pending")
    transaction.save()
    return render(request, 'products.html', {'message':"we will deliver you product soon","products": getAllProducts()})

def getTrasactions(request):
    return render(request, "transactions.html", {"transactions":TransactionModel.objects.all()})

def updatetrasaction(request):
    tid = request.GET['tid']
    status=request.GET['status']
    TransactionModel.objects.filter(id=tid).update(status=status)
    return render(request, 'transactions.html', {"transactions":TransactionModel.objects.all()})
