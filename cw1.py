import random 
# store the volume of each juice 
apple = 15.5
orange= 20
grape = 10.25
#calculate the total volume 
total = apple + orange + grape
# print the total volume
print ("total volume solid :", total)
# convert total volume to integer
total_int= int(total)
print("total volume as integer:",total_int)
#convert total volume to an string
total_str= str(total)
print("total volume as string:"+total_str +"liters")
# generate a random bonus between 5 and 10
bonus=random.randint(5,10)
#calculate the final total
final_total= total+bonus
#prnt the final total
print("bonus liters:", bonus)
print("final total volume:",final_total)