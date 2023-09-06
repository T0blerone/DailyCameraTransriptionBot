import newspaper
from newspaper import Article

class Articles:
    #Class Varibles
    article_title = ""
    article_text = ""
    
    #methods
    def getTitle(self): #Returns the title of the article
        return Articles.article_title
    
    def getText(self): #returns the text contained in the article.
        return Articles.article_text
    
    def __init__(self, givenURL) -> None: #constructor that initializes the article variable with the given url, and parses the article for its information.
        current_article = Article(url = givenURL) #Creates article object.
        current_article.download() #Downloads article.
        current_article.parse() #Takes article info.
        Articles.article_title = current_article.title #Saves article title.
        Articles.article_text = current_article.text #Saves article text.
        pass
