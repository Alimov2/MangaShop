class Shopping_Cart_Class:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart') 

        if not cart:
            cart = self.session['cart'] = {} 
            self.cart = self.session['cart']

        else: 
            self.cart = cart

    def save_products(self):
        self.session['cart'] = self.cart
        self.session.modified = True 

    def add_product(self, product):
        if (str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                'product_id':product.id, 
                'name':product.name, 
                'price':float(product.price), 
                'quantity':1, 
            } 
        
        else: 
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    value['price'] = float(value['price']) + product.price 
                    break 
        
        self.save_products() 

    def delete_product(self, product): 
        product.id = str(product.id) 

        if product.id in self.cart: 
            del self.cart[product.id] 
            self.save_products() 

    def discount_product(self, product): 
        
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] = value['quantity'] - 1
                value['price'] = float(value['price']) - product.price 
                
                if value['quantity'] < 1:
                    
                    self.delete_product(product)

                break 
            
        self.save_products() 
    
    def clean_shopping_cart(self): 
        self.session['cart'] = {} 

        self.session.modified = True 


