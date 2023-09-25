# from news.models import *
# u1 = User.objects.create_user(username= 'Dima')
# u2 = User.objects.create_user(username= 'Alex')
# Author.objects.create(authorUser=u1)
# Author.objects.create(authorUser=u2)
# Category.objects.create(name='Политика')
# Category.objects.create(name='Экономика')
# Category.objects.create(name='Искусство')
# Category.objects.create(name='Наука')
# a1 = Author.objects.get(pk=1)
# a2 = Author.objects.get(pk=2)
# Post.objects.create(author = a1,categoryType='AR', title='Здоровое питание',text="В здоровом питании самое главное сбалансированные приемы пищи.")
# Post.objects.create(author = a2,categoryType='AR', title='Жестокость в современном мире',text="Люди стали жестокими, пропало милосердие...")
# Post.objects.create(author = a1,categoryType='NW', title='Землятресение в Турции',text="Ужасная трагедия случилась в Турции.")
# Post.objects.get(pk=1).postCategory.add(Category.objects.get(pk=4))
# Post.objects.get(pk=1).postCategory.add(Category.objects.get(pk=2))
# Post.objects.get(pk=2).postCategory.add(Category.objects.get(pk=4))
# Post.objects.get(pk=3).postCategory.add(Category.objects.get(pk=1))
# Post.objects.get(pk=3).postCategory.add(Category.objects.get(pk=2))
# Comment.objects.create(commentPost=Post.objects.get(pk=1),commentUser=Author.objects.get(pk=1).authorUser,text='бла-бла, буль!')
# Comment.objects.create(commentPost=Post.objects.get(pk=2),commentUser=Author.objects.get(pk=1).authorUser,text='буль-буль. Бдышь')
# Comment.objects.create(commentPost=Post.objects.get(pk=3),commentUser=Author.objects.get(pk=2).authorUser,text='Как жалко.Ужасная трагедия.')
# Comment.objects.create(commentPost=Post.objects.get(pk=3),commentUser=Author.objects.get(pk=1).authorUser,text='Турция примите соболезнования!')
# Comment.objects.create(commentPost=Post.objects.get(pk=1),commentUser=Author.objects.get(pk=1).authorUser,text='Ту-ту-ту-ра-ра!')
# Comment.objects.get(pk=4).like()
# Comment.objects.get(pk=4).like()
# Comment.objects.get(pk=4).like()
# Comment.objects.get(pk=4).rating
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=1).like()
# Post.objects.get(pk=1).dislike()
# Post.objects.get(pk=1).rating
# Comment.objects.get(pk=1).dislike()
# Comment.objects.get(pk=1).rating
# Comment.objects.get(pk=2).dislike()
# Comment.objects.get(pk=2).dislike()
# Comment.objects.get(pk=2).rating
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=2).rating
# a1.update_rating()
# a1.ratingAuthor
# a2.update_rating()
# a2.ratingAuthor
# bestAuthor = Author.objects.order_by('-ratingAuthor')[:1]
# bestAuthor[0].authorUser
# bestAuthor[0].ratingAuthor
# bestPost = Post.objects.order_by('-rating')[:1]
# bestPost[0].dateCreation
# bestPost[0].author.authorUser
# bestPost[0].rating #рейтинг
# bestPost[0].title
# bestPost[0].preview()
# #  список  комментариев - comm
# comm = Comment.objects.filter(commentPost=bestPost[0])
# comm.values('dateCreation')
# # авторы комментариев
# for i in range(len(comm)):
#     comm[i].commentUser.get_full_name
#
# comm.values('rating')
# comm.values('text')
ProductMaterial.objects.create(product=Product.objects.get(pk=2), material=Material.objects.get(pk=3))
Post.objects.get(pk=1).categoryType