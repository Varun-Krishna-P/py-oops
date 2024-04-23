class Book:
    
    default_discount = 0.25
    max_stock = 230
    
    def __init__(self, title, author, num_pages, is_published):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.is_published = is_published
        
        
# Write your code below:
discount = Book.default_discount
max_stock = Book.max_stock