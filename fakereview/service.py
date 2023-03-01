from fakereview.beans import ProductBean
from fakereview.models import LikeOrDisLikeModel, CommentModel, ProductModel


def getAllProducts():

    products = []

    for product in ProductModel.objects.all():

        product.path = str(product.path).split("/")[1]

        comments = CommentModel.objects.filter(product=product.id)

        likes = 0
        dislikes = 0

        for likeordislike in LikeOrDisLikeModel.objects.filter(product=product.id):

            print(likeordislike.status+"\t status")

            if int(likeordislike.status) == 0:
                dislikes = dislikes + 1
            elif int(likeordislike.status) == 1:
                likes = likes + 1

        bean = ProductBean(product, comments, likes, dislikes,product.description)

        products.append(bean)

    return products