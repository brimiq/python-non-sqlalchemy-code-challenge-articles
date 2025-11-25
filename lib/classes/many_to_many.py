class Article:
    all = []
    #Creating different instance variables
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
        
        if self._title:
            return
        
        #verifying whether the title is a string and is withing the given length
        if isinstance(value, str) and 5 <= len(value.strip()) <= 50:
            self._title = value.strip()


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Prevent resetting after initialization
        if self._name:
            return
        
        # Using bool validation to check for different strings
        if isinstance(value, str) and bool(value.strip()):
            self._name = value.strip()

    def articles(self):
        
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        mags = []
        for art in self.articles():
            if art.magazine not in mags:
                mags.append(art.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        arts = self.articles()
        if not arts:
            return None
        
       #Returning the list as a set
        return list({a.magazine.category for a in arts})


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        if isinstance(value, str) and 2 <= len(value.strip()) <= 16:
            self._name = value.strip()
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        # ensures at least one visible character
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value.strip()

    def articles(self):
        # Simple filter using list comp
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        # Use set comprehension again
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        # Count articles per author
        counts = {}
        for art in self.articles():
            counts[art.author] = counts.get(art.author, 0) + 1
        
        # Authors with >2 articles
        many = [author for author, c in counts.items() if c > 2]
        
        return many or None
