alpha=True
while alpha == True:
	print("""        
    __  __      __       __   __  ___                                                  __     _____            __               
   / / / /___  / /____  / /  /  |/  /___ _____  ____ _____ ____  ____ ___  ___  ____  / /_   / ___/__  _______/ /____  ____ ___ 
  / /_/ / __ \/ __/ _ \/ /  / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ __ `__ \/ _ \/ __ \/ __/   \__ \/ / / / ___/ __/ _ \/ __ `__ \ 
 / __  / /_/ / /_/  __/ /  / /  / / /_/ / / / / /_/ / /_/ /  __/ / / / / /  __/ / / / /_    ___/ / /_/ (__  ) /_/  __/ / / / / /
/_/ /_/\____/\__/\___/_/  /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/ /_/ /_/\___/_/ /_/\__/   /____/\__, /____/\__/\___/_/ /_/ /_/ 
                                                   /____/                                       /____/                               
												v 0.3.9 by vignesh sb, saisuraj a,hariraam R """)
	print("""	[*] Searching for the required files.
	[*] Reqesting the MySQL server to connect.""")
	###Back End
	import mysql.connector
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="hacker9090",database="HMS")
	cursor=mydb.cursor(buffered=True)
	print("""	[*] The sql server is connected succesfully.""")									
	print("""
	1.Customer
	2.Management
	3.Billing
	4.Food
	5.Review
	6.exit
""")
	try:
		a= int(input("enter the option (1-6): "))				#main
		while a>= 7:
			a= int(input("only enter the option (1-6): "))
		else:	
			if a==1:												#customer
				print("""
				1.register a new Customer
				2.see the data of a Customer
				3.edit the data of a Customer
				4.delete the data of a Customer
				""")
				a1= int(input("enter the option (1-4): "))
				while a >=5:
					a1= int(input("only enter the option (1-4): "))
				else:	
					if a1==1:
						a1name=(input("enter your name: "))
						try:
							a1ID=int(input("enter your ID: "))
						except:
							a1ID=int(input("enter only your ID: "))
						a1city=(input("enter your city: "))
						a1state=(input("enter your  state: "))
						a1DOB=(input("enter your DOB in the formate(YYYY-MM-DD): ")) #add date of joining also
						a1mail=(input("enter your mail id: "))
						a1CONT=int(input("enter your ph number: "))
						a1conf=input("Are you sure to enter the values?(y/n)")
						if a1conf=="y":
							try:
								insertstatement1=("insert into Customer (name,ID,City,State,DOB,Email,PHnumb)" "values (%s,%s,%s,%s,%s,%s,%s)")
								data1=(a1name,a1ID,a1city,a1state,a1DOB,a1mail,a1CONT)
								cursor.execute(insertstatement1, data1)
								mydb.commit()
								print("values entered succesfully.")
							except:
								print("C001:some error occured in the database.")
						else:
							print("values not entered.")					
					else:
						pass
					if a1==2:
						a1search=int(input("enter the ID to be searched: "))
						searchstatement=("select * from Customer where ID={}".format(a1search))
						a1result=cursor.execute(searchstatement)
						mydb.commit()
						for i in a1result:
							print(i)			
					else:
						pass
					if a1==3:
						try:
							a1edit1=int(input("enter the ID to be edited: "))
						except:
							a1edit1=int(input("enter only the ID to be edited: "))
						try:
							editstatement=("select")
						except:
							print("C003:some error occured in the database.")	
					else:
						pass
					if a1==4:
						a1delete1=int(input("Enter the ID to be deleted: "))
						a1delsatement=("DELETE FROM Customer WHERE ID={}".format(a1delete1))
						cursor.execute(a1delsatement)
						mydb.commit()
						print("Deleted succesfully.")						
			else:
				pass
			if a==2:												#Management
				print("""
				1.register a new staff
				2.see the data of a staff
				3.edit the data of a staff
				4.delete the data of a staff
				""")
				a2= int(input("enter the option (1-4): "))
				if a2==1:
					a2name=(input("enter staff name: "))
					a2ID=int(input("enter staff ID: "))
					a2city=(input("enter staff city: "))
					a2state=(input("enter staff  state: "))
					a2DOB=(input("enter staff DOB in the formate(YYYY-MM-DD): "))#add date of joining
					a2mail=(input("enter staff mail id: "))
					a2CONT=int(input("enter staff ph number: "))
					a2conf=input("Are you sure to enter the values?(y/n) ")
					if a2conf=="y":
						try:
							insertstatement2=("insert into Staff (Name,ID,City,State,DOB,Email,PHnumb)" "values (%s,%s,%s,%s,%s,%s,%s)")
							data2=(a2name,a2ID,a2city,a2state,a2DOB,a2mail,a2CONT)
							cursor.execute(insertstatement2, data2)
							mydb.commit()
							print("values entered succesfully.")
						except:
							print("C001:some error occured in the database.")
					else:
						print("values not entered.")
				else:
					pass
				if a2==2:
					input("enter the ID")
				else:
					pass
				if a2==3:
					input("enter the ID")
				else:
					pass
				if a2==4:
					a2delete1=int(input("Enter the ID to be deleted: "))
					a2delsatement=("DELETE FROM Staff WHERE ID={}".format(a2delete1))
					cursor.execute(a2delsatement)
					mydb.commit()
					print("Deleted succesfully.")

				else:
					pass				
			else:
				pass
			if a==3:												#bill	
				print("""
				1.register a new Bill
				2.see the data of a Bill
				3.edit the data of a Bill
				4.delete the data of a Bill 
				""")
				a3= int(input("enter the option (1-4): "))
				if a3==1:
					a3name=input("Enter the Customer name: ")
					a3ID=input("Enter the bill number: ")
					a3Date=input("Enter the date of billing in the formate(YYYY-MM-DD): ")
					a3Cos=input("Enter the bill amount: ")
					tipcon=input("Do you want to tip the Staffs?(y/n):  ")
					if tipcon=="y":
						a3tip=input("Enter the tip amount: ")
					else:
						a3tip="none"
					a3conf=input("are you sure you want to enter the values (y/n): ")		
					if a3conf=="y":
							try:
								insertstatement3=("insert into Billing (name,ID,Date,ammount,tip)" "values (%s,%s,%s,%s,%s)")
								data3=(a3name,a3ID,a3Date,a3Cos,a3tip)
								cursor.execute(insertstatement3, data3)
								mydb.commit()
								print("values entered succesfully.")
							except:
								print("C001:some error occured in the database.")
					else:
						print("values not entered.")

				else:
					pass	
			else:
				pass
			if a==4:												#food
				print("""
				1.Register new food.
				2.See previous food Details.
				3.See all food available.
				4.Edid food Details.
				5.Delete food Details
				""") 
				a4=int(input("Enter any option (1-5): "))
				if a4==1:
					a4name=input("Enter the food name: ")
					a4ID=input("Enter the ID for food:")
					a4price=input("Enter the price of food: ")
					a4orig=input("Enter the origin of food: ")
					a4ratig=input("Enter the avg food rating: ")
					a4conf=input("Are you sure you want to enter the values?(y/n): ")
					if a2conf=="y":

						try:
							insertstatement4=("insert into Staff (Name,ID,price,origin,rating)" "values (%s,%s,%s,%s,%s)")
							data4=(a4name,a4ID,a4price,a4orig,a4ratig)
							cursor.execute(insertstatement4, data4)
							mydb.commit()
							print("values entered succesfully.")
						except:
							print("C001:some error occured in the database.")
					else:
						print("values not entered.")
				else:
					pass
				if a4==2:
					a4serch=input("Enter the ID to search: ")
				else:
					pass
				if a4==3:
					a4serch=input("Enter the ID to search: ")
				else:
					pass
				if a4==4:
					print("all the food available")
				else:
					pass
				if 	a4==5:
					a4delcon=input("Are you sure you want to delete the food details?(y/n): ")
			else:
				pass
			if a==5:												#review
				print("""review""")
			if a >= 6:												#exit
				a4=(input("Do you want to exit?(y/n): "))
				if a4=="y":
					alpha=False
				else:
					pass
	except:
		print("Eroor occured some where please try again.")			
else:
	print("thankyou!") 