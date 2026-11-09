def analyze_user(user):

age = user["age"]
weight = user["weight"]
height = user["height"]
goal = user["goal"]

if age <= 0 or weight <= 0 or height <= 0:
  return "البيانات غير صحيحة"
 result = {
   "age":age,
   "weight":weight,
   "height":height,
   "goal":goal,
 }
return result
