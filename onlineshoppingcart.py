#product_details
product_list=['chips','pepsi','dairymilk','cookies','kiwi','apple']
product_qnt=[50,30,30,20,10,20]
product_price=[20,35,65,30,99,35]
#customer transaction
user_cart=[]
user_qnt=[]
user_amt=[]
#user selection
u_s=['View Products','Add to Cart','Remove from Cart','View Cart','checkout','EXIT']
#Admin selection
a_s=['Add product','Update product','Remove product','View product','view USERS','EXIT']
#user details
users=[]
user_history=[]
user_total=[]
phone=[]
#role selection
while True:
    
    char=input('enter your Role ""admin///user""..')
    if char=='admin':
        while True:
            print('*'*14,'SHOPPING CART SYSTEM','*'*14)
            print('-'*50)
            print('*'*14,'YOUR IN ADMIN PANEL','*'*14)
            print('-'*50)
            n=1
            for i in a_s:
                print(n,'->',i)
                n+=1
            print('-'*50)
            
            ch=int(input('select any number(1/6) for above process '))
            
            if ch==1:
                while True:
                    print('-'*50)
                    p=input('Please Enter product Name To Add (or)To stop adding enter "NO"')
                    if p=='NO':
                        break
                    product_list.append(p)
                    q=int(input('Please Enter Product Quantity/pieces..'))
                    product_qnt.append(q)
                    pr=float(input('enter product price..'))
                    product_price.append(pr)
                    print(p,'IS SUCCESSFULLY ADDED ')
                    print('-'*50)
            elif ch==2:
                print('-'*50)
                print('Updating Product Details...')
                print('-'*50)
                print('Product_Name \*** Product_Quantity \* Product_Price')
                print('-'*50)
                for i in zip(product_list,product_qnt,product_price):
                    print(f'{i[0]: <18}{i[1]: <20}{i[2]: <12}')
                print('-'*50)    
                while True:
                    c=input('Please Enter Product Name to Update (or)TO STOP UPDATING Enter "NO"')
                    if c=='NO':
                        break
                    if c in product_list:
                        ind=product_list.index(c)
                        q=int(input('enter New Update QUANTITY'))
                        product_qnt[ind]=q
                        pr=float(input('Please Enter new PRICE...'))
                        product_price[ind]=pr
                        print(c,'IS SUCCESSFULLY UPDATED')
                        print('-'*50)
                    else:
                        print('PLEASE enter Valid product to update')
            elif ch==3:
                n=1
                print('-'*50)
                for i in product_list:
                     print(n,'->',i)
                     n+=1
                print('-'*50)
                while True:
                    ch=input('Please enter Product NAme to Remove.. or TO STOP enter "NO"')
                    if ch=='NO':
                        break
                    if ch in product_list:
                        ind=product_list.index(ch)
                        product_list.remove(ch)
                        product_qnt.pop(ind)
                        product_price.pop(ind)
                        print(ch,'IS SUCCESSFULLY REMOVED')
                        print('-'*50)

                    else:
                        print('Please enter Only Available product..')
            elif ch==4:
                print('-'*50)
                print("AVAILABLE PRODUCTS IN STORE....")
                print('-'*50)
                print('Product_Name \*** Product_Quantity \* Product_Price')
                print('-'*50)
                for i in zip(product_list,product_qnt,product_price):
                    print(f'{i[0]: <18}{i[1]: <20}{i[2]: <12}')
                print('-'*50)
            elif ch==5:
                if len(user_history)==0:
                    print('NO SALES TODAY')
                    print('-'*50)
                else:
                    for i in range(len(users)):
                        print('*'*50)
                        print("USER_NAME    :-",users[i])
                        print("MOBILE_NUMBER:-",phone[i])
                        print('-'*50)
                        print('Product_Name.....\Product_Quantity..\Total_P_price')
                        for j in range(len(user_history[i][0])):
                            print(f'{user_history[i][0][j]: <18}{user_history[i][1][j]: <19}{user_history[i][2][j]}')
                        print('-'*50)
                        print(' '*30,'TOTAL_AMOUNT:-',user_total[i])
                print('-'*50)
                print('TOTAL_SALE:----',sum(user_total))
                print('-'*50)
                
            elif ch==6:
                print('ADMIN EXITED------')
                break
                
            else:
                print('Please Enter 1/6 only for above Operations')
    elif char=='user':
        name=input('enter ur name')
        while True:
            phn=int(input('enter ur number'))
            if phn>=1000000000 and phn<=9999999999:
                break
            else:
                print('WRONG MOBILE NUMBER')
        while True:
            print('*'*14,'SHOPPING CART SYSTEM','*'*14)
            print('-'*50)
            print('*'*14,'YOUR IN USER PANEL','*'*15)
            print('-'*50)
            n=1
            for i in u_s:
                print(n,'->',i)
                n+=1
            print('-'*50)
            ch=int(input('select any number(1/6) for above process'))
            
            if ch==1:
                print('-'*50)
                print('AVAILABLE PRODUCTS.........')
                print('-'*50)
                print('PRODUCT_NAME**','PRICE**','AVAILABLE_STOCK')
                print('-'*50)
                for i in zip(product_list,product_price,product_qnt):
                    print(f'{i[0]: <15}{i[1]: <7}{i[2]: >5}')
                print('-'*50)
                
            elif ch==2:
                while True:
                    print('-'*50)
                    p=input('enter product for ADD to Cart..(or) enter "Done" after adding products')
                    if p=='Done':
                        break
                    if p in product_list:
                        q=int(input('enter Number of pieces..'))
                        ind=product_list.index(p)
                        if q<=product_qnt[ind]:
                            amt=q*product_price[ind]
                            if p in user_cart:
                                user_qnt[ind]+=q
                                user_amt[ind]+=amt
                            else:   
                                user_cart.append(p)
                                user_qnt.append(q)
                                user_amt.append(amt)
                            product_qnt[ind]-=q
                            if product_qnt[ind]==0:
                                product_list.pop(ind)
                                product_qnt.pop(ind)
                                product_price.pop(ind)
                            print(p,'is Successfully ADDED')
                            

                        else:
                            print('OUT OF STOCK... the available STOCK ->',product_qnt[ind])

                    else:
                        print('sorry',p,'is not Available')
            elif ch==3:
                print('-'*50)
                print("YOUR CART>>>>>>")
                print('-'*50)
                print('Product_Name****\Product_Quantity**\product_price*')
                print('-'*50)
                for i in zip(user_cart,user_qnt,user_amt):
                    print(f'{i[0]: <17}{i[1]: <18}{i[2]: <14}')
                print('-'*50)
                while True:
                    
                    p=input('enter product name to remove (OR) complete removing enter "Done"')
                    if p=='Done':
                        break
                    if p in user_cart:
                        ind=user_cart.index(p)
                        user_cart.remove(p)
                        user_qnt.pop(ind)
                        user_amt.pop(ind)
                        print(p,'has been successfully Removed')
                        print('-'*50)
                    else:
                        print("Please only enter product in your cart to remove")
            elif ch==4:
                print('-'*50)
                print("YOUR CART>>>>>>")
                print('-'*50)
                print('Product_Name****\Product_Quantity**\product_price*')
                print('-'*50)
                
                for i in zip(user_cart,user_qnt,user_amt):
                    print(f'{i[0]: <17}{i[1]: <18}{i[2]: <14}')
                print('-'*50)
                print(' '*30,'TOTAL AMOUNT=',sum(user_amt))
                print('-'*50)
                      

            elif ch==5:
                if len(user_cart)>0:
                    users.append((name))
                    phone.append((phn))
                    user_history.append((user_cart,user_qnt,user_amt))
                    
                    user_total.append((sum(user_amt)))
                print('-'*50)
                print("ORDER CONFIRMED ")
                print('-'*50)
                print('Product_Name****\Product_Quantity**\product_price*')
                print('-'*50)
                for i in zip(user_cart,user_qnt,user_amt):
                    print(f'{i[0]: <17}{i[1]: <18}{i[2]: <14}')
                print('-'*50)
                print(' '*30,'TOTAL AMOUNT=',sum(user_amt))
                print('-'*50)
                
                print('ORDER DELIVERED')
                print('-'*50)
                
                
                user_cart=[]
                user_qnt=[]
                user_amt=[]
                
            elif ch==6:
                print('-'*50)
                print("USER EXITED")
                print('-'*50)
                break
                
                    
        

    else:
        print('enter valid role...(or)enter in lowercase')
