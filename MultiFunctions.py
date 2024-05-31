class multipleFunctions():
     def Subfields():
        subFieldsInAI = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print("Sub-fields in AI are:")
        for item in subFieldsInAI:
            print(item)
        return
    
     def OddEven(number):
        if(number%2 == 0):
            message = "Even number"
        else:
            message = "Odd number"
        return message
    
     def Eligible():
        gender = input("Your Gender : ")
        age = int(input("Your Age : "))
        if(gender == "Male" and age >= 21):
                msg = "ELIGIBLE"
        elif(gender == "Female" and age >= 18):
                msg = "ELIGIBLE"
        else:
            msg = "NOT ELIGIBLE"
        return msg
    
     def percentage():
        sub1 = int(input("Subject 1 = "))
        sub2 = int(input("Subject 2 = "))
        sub3 = int(input("Subject 3 = "))
        sub4 = int(input("Subject 4 = "))
        sub5 = int(input("Subject 5 = "))
        Total = sub1 + sub2 + sub3 + sub4 + sub5
        print("Total : ", Total)

        perct = (Total / 500) * 100
        print("Percentage : ", perct)
        return
    
     def triangle():
        breadth = int(input("Breadth : "))
        height = int(input("Height : "))
        area = (height * breadth)/2
        print("Area Formula : ((Height*Breadth)/ 2)")
        print("Area of Triangle : ", area)
        
        height1 = int(input("Height1 : "))
        height2 = int(input("Height2 : "))
        breadth = int(input("Breadth : "))
        perimeter = height1 + height2 + breadth
        print("Perimeter Formula : Height1 + Height2 + Breadth")
        print("Perimeter of Triangle : ", perimeter)
        return