listStudent=["Ajay","Aman","vivek","Sam"]
listSubject=["English","Maths","Science","Hindi"]
listRollno=[101,102,103,104]
listMin=[50]
listMax=[100]
dictoutput={}
indx=0
for student in listStudent:
     dictsubject={}
     res1=sum(listMin)+listRollno[indx]
     res2=sum(listMax)+listRollno[indx]
     for subject in listSubject:
      dictsubject.update({subject:{"Minmark":res1,"Maxmark":res2}})
     dictstudent={student:{"Rollno":listRollno[indx],"Subject":dictsubject}}
     dictoutput.update(dictstudent)
     indx=indx+1
print(dictoutput) 
  