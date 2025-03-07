#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

testScoreString = input("Enter the test score: ")
classRankString = input("Enter the class rank: ")

# Step 2: Convert the inputs to integers
testScore = int(testScoreString)
classRank = int(classRankString)

# Test using admission requirements and print Accept or Reject
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
