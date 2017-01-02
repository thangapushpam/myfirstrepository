from django.shortcuts import render, get_object_or_404
from .models import Choice, Question, Answer, Student,  Count, Test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from random import randint
from random import sample

def login(request):
	msg = []
	if request.method == 'POST':
		 username = request.POST['username']
		 password = request.POST['password']
		 user = authenticate(username=username, password=password)
		 if user is not None:
		 	if user.is_active and user.is_superuser:
		 		auth_login(request, user)
		 		return HttpResponseRedirect('/questionservice/view_adminpage/')
		 	if user.is_active:
		 		auth_login(request, user)
		 		return HttpResponseRedirect('/questionservice/view_studentpage/')
		 	else:
		 		msg.append("disabled account")
		 else:
		 	msg.append("invalid login")
		 	
	return render(request, 'login.html', {'errors': msg})

def view_adminpage(request):
	# Display all question to admin 
	questionlist = Question.objects.all()
	return render(request, 'admin.html', {'questionlist':questionlist} )

def get_value(request):
	#get question value  from admin for adding new question in question list
  question_value = request.POST.get("question")
  print question_value
  return render(request, 'get_value.html')

def add(request):
	# admin add question in question list
	#create new question 
	question_value = request.POST.get("question")
	choice_value = request.POST.get('choice')
	choice1_value = request.POST.get('choice1')
	choice2_value = request.POST.get('choice2')
	answer_value = request.POST.get('answer')
	print answer_value
	question = Question.objects.create(question_text = question_value)
	print question.id
	choice = Choice.objects.bulk_create(
		[Choice (question=question, choice_text = choice_value), 
		Choice (question=question,choice_text = choice1_value), 
		Choice (question=question, choice_text = choice2_value)])
	answer = Answer.objects.create(question=question, answer_text = answer_value)
	return render(request, 'add.html')

def view_studentpage(request):
	#get and view_student history 
	user = request.user
	student = Student.objects.get(name=user)
	scorelist = Test.objects.filter(student=student)
	count_value = Count.objects.get(id=1)
	count_value.count = 0
	count_value.score_value = 0
	count_value.save()
	return render(request, 'student.html', {'scorelist':scorelist})

def view_questionpage(request):
	#view random question to student
	msg=""
	count_value = Count.objects.get(id = 1)
	print count_value
	if count_value.count < 5:
	  count_value.count = count_value.count + 1
	  count_value.save()
	  count = Question.objects.all().count()
	  rand_ids = sample(xrange(1, count), 1)
	  rand_ids = [ int(x) for x in rand_ids ]
	  questionlist = Question.objects.all()
	  question_id = questionlist[x]
	  id_value =  question_id.id
	  id = count_value.count + id_value
	  if id <= count:
	       question = Question.objects.get(id = id)
	       return render(request, 'question.html',{'question':question})
	  else:
	  	id = id_value
	  	question = Question.objects.get(id = id)
	  	return render(request, 'question.html',{'question':question})
	else:
		# once completed text score show to the student and redirect to dash board for next text
		user = request.user
		student = Student.objects.get(name=user)
		test_object = Test.objects.create(student=student, score=0)
		object_count = Test.objects.all().count()
		test_queryset = Test.objects.all()
		score_id = test_queryset[object_count-1]
		test_score = Test.objects.get(id=score_id.id)
		count_object = Count.objects.get(id=1)
		test_score.score = count_object.score_value
		test_score.save()
		scr=test_score.score
		msg ="You got"+ str(scr) + "out of 5"
		return render(request, 'count.html',{'msg':msg})

def validate(request, id):
	# validate student answer is correct or not
	msg=[]
	question = Question.objects.get(id = id)
	ans = Answer.objects.get(question=question)
	an=ans.answer_text
	answer = request.POST.get('choice')
	if str(an) == str(answer):
		#If answer correct means score of the student increased by one
		msg.append('Its correct answer')
		score=Count.objects.get(id=1)
		score.score_value =score.score_value + 1
		score.save()
	else:
		msg.append('Its wrong')
	return render(request,'validate.html',{'msg':msg})

def logout_view(request):
    logout(request)
    return render(request, 'login.html')