class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title') and self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        
class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not None:
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine_list = []
        for article in self.articles():
            if article.magazine not in magazine_list:
                magazine_list.append(article.magazine)
        return magazine_list

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set([article.magazine.category for article in self.articles()]))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if len(result) > 0 else None
