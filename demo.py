from wikiarticle import *

for element in WikiArticle.get_article('Johnny_Checketts', debug=True).elements:
    print(element)