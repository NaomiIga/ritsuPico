#!/usr/bin/env python
# coding: utf-8
# Create your views here.

from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from models import *
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
import datetime
import json
import time
from django.utils.encoding import *
from django.http.response import JsonResponse
from django.core import serializers
import csv
import datetime
import unicodedata
#from PIL import Image
import base64
import sys
sys.stdout = sys.stderr
# Create your views here.

#テスト用
"""
@csrf_exempt
def post_test(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		new_data = Data.objects.create(
			userdata = datas.keys(),
			datavalue = datas.values(),
		)
		new_data.save() #デーベ保存

		return HttpResponse(u'post succeed')
	else:
		response = HttpResponse()
		response['msg'] = 'NG'
"""

#ユーザ登録(ダブり確認)する関数、今のままだとこの瞬間が開始時刻
@csrf_exempt
def pico_login(request):
	if request.method == 'POST':
		datas = json.loads(request.body)  #追記
		name = datas["name"]
		temp = Hint.objects.get(treasure_num = 100)
		temp.hint_num += 1
		temp.save()

		try:
			testname = User.objects.get(username = name)
			return HttpResponse(u'error')
		except User.DoesNotExist:
			new_data = User.objects.create(
			user_id = temp.hint_num,
			username = name,
			starttime = datetime.datetime.now(),
			treasures = '0,0,0,0,0,0',
			)
			new_data.save()

			new_data = UsedHint.objects.create(
			username = name,
			)
			new_data.save()
			return HttpResponse(name)

	else:
		response = HttpResponse()
		response['msg'] = 'NG'

#鍵ゲットのとき
@csrf_exempt
def key_get(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		name = datas["name"]   # ダブルクオート内はディクショナリーのキー
		#major = datas["major"]
		#minor = datas["minor"]
		#beacon = str(major) + "-" + str(minor)
		beacon = datas["beaconMM"]
		get_time = datetime.datetime.now()
		get_time_str = get_time.strftime("%Y-%m-%d %H:%M")
		key = "{" + beacon + ":" + get_time_str + "}"

		update_data = User.objects.get(username = name)
		if update_data.key == "key":
			keys = key
		else:
			key_data = update_data.key
			keys = key_data + ", " + key
		update_data.key = keys
		update_data.key_num += 1
		update_data.save()
	return HttpResponse("OK")


#宝ゲットのとき
@csrf_exempt
def treasure_check(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		name = datas["name"]   # ダブルクオート内はディクショナリーのキー
		major = datas["major"]
		minor = datas["minor"]
		treasure_number = treasure_num(major,minor)

		update_data = User.objects.get(username = name)
		watched_hint = UsedHint.objects.get(username = name)

		if treasure_number == 1:
			if update_data.treasure1 == None:
				update_data.treasure1 = datetime.datetime.now()
				if watched_hint.hint1_3 != None:
					update_data.points += 1
					getpointnow = 1
				elif watched_hint.hint1_2 != None:
					update_data.points += 2
					getpointnow = 2
				else:
					update_data.points += 3
					getpointnow = 3
			else:
				getpointnow = 0
		elif treasure_number == 2:
			if update_data.treasure2 == None:
				update_data.treasure2 = datetime.datetime.now()
				if watched_hint.hint2_3 != None:
					update_data.points += 1
					getpointnow = 1
				elif watched_hint.hint2_2 != None:
					update_data.points += 2
					getpointnow = 2
				else:
					update_data.points += 3
					getpointnow = 3
			else:
				getpointnow = 0
		elif treasure_number == 3:
			if update_data.treasure3 == None:
				update_data.treasure3 = datetime.datetime.now()
				if watched_hint.hint3_3 != None:
					update_data.points += 1
					getpointnow = 1
				elif watched_hint.hint3_2 != None:
					update_data.points += 2
					getpointnow = 2
				else:
					update_data.points += 3
					getpointnow = 3
			else:
				getpointnow = 0
		elif treasure_number == 4:
			if update_data.treasure4 == None:
				update_data.treasure4 = datetime.datetime.now()
				if watched_hint.hint4_3 != None:
					update_data.points += 1
					getpointnow = 1
				elif watched_hint.hint4_2 != None:
					update_data.points += 2
					getpointnow = 2
				else:
					update_data.points += 3
					getpointnow = 3
			else:
				getpointnow = 0
		elif treasure_number == 5:
			if update_data.treasure5 == None:
				update_data.treasure5 = datetime.datetime.now()
				if watched_hint.hint5_3 != None:
					update_data.points += 1
					getpointnow = 1
				elif watched_hint.hint5_2 != None:
					update_data.points += 2
					getpointnow = 2
				else:
					update_data.points += 3
					getpointnow = 3
			else:
				getpointnow = 0
		elif treasure_number == 6:
			if update_data.treasure6 == None:
				update_data.treasure6 = datetime.datetime.now()
				if watched_hint.hint6_3 != None:
					update_data.points += 1
					getpointnow = 1
				elif watched_hint.hint6_2 != None:
					update_data.points += 2
					getpointnow = 2
				else:
					update_data.points += 3
					getpointnow = 3
			else:
				getpointnow = 0

		#update_data.treasure[treasure_number - 1] = getpointnow
		treasure_list = update_data.treasures.split(',')
		if treasure_list[treasure_number - 1] == '0' and getpointnow != 0:
			treasure_list[treasure_number - 1] = str(getpointnow)
			update_data.key_num -= 1

		print "getpointnow"
		print getpointnow
		print treasure_list
		treasure_list = ','.join(treasure_list)
		update_data.treasures = treasure_list

		update_data.save()

		#ここにポイント計算のこと書く？
		return JsonResponse({"totalpoint":update_data.points, "getpoint":getpointnow}, safe=False)
	else:
		response = HttpResponse()
		response['msg'] = 'NG'

#とんできたビーコンの番号から、どの宝かを識別

def treasure_num(get_major, get_minor):
	data = Treasure_Beacon.objects.get(major=get_major, minor=get_minor)
	treasure_number = data.treasure
	return treasure_number

# 初めてヒント見たときに呼ばれる
'''
@csrf_exempt
def first(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		name = datas["name"]   # ダブルクオート内はディクショナリーのキー
		tag = datas["treasureNo"]

		# DBに使用時間を格納
		usedhintdatas = UsedHint.objects.get(username = name)
		if tag == 1:
			usedhintdatas.hint1_1 = datetime.datetime.now()
		elif tag == 2:
			usedhintdatas.hint2_1 = datetime.datetime.now()
		elif tag == 3:
			usedhintdatas.hint3_1 = datetime.datetime.now()
		usedhintdatas.save()

		hintdatas = Hint.objects.get(treasure_num = tag, hint_num = 1)
		first_hint = hintdatas.hint_sent
		first_hint = u'ヒント1\n' + first_hint + u'\n'
		return JsonResponse({"hint1":first_hint})
	else:
		response = HttpResponse()
		response['msg'] = 'NG'
'''

#ヒント使うときによばれる
@csrf_exempt
def hint(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		name = datas["name"]   # ダブルクオート内はディクショナリーのキー
		tag = datas["treasureNo"]
		treasureNo = 'treasure' + str(tag)
		next_watch = datas["next_watch"]

		hint, hint_num = hint_check(name, tag, next_watch)

		return JsonResponse({"hint":hint, "hint_num":hint_num})
	else:
		response = HttpResponse()
		response['msg'] = 'NG'

#どれだけヒント使ってきたかをチェック

def hint_check(name, treasureNo, next_watch):
	data = UsedHint.objects.get(username = name)

	#次を見るがtrueかfalseかを受け取るnext_watch
	if treasureNo == 1:
		#とりあえず飛んできた瞬間にhintにhint1を追加
		hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 1)
		hint = u'ヒント1\n' + hintdatas.hint_sent + u'\n\n'
		#次を見るって押されてかつ2つ目のhintがNoneなら時間追加してhint_2を返す
		if next_watch == True and data.hint1_2 == None:
			hint_num = 2
			data.hint1_2 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
		#次を見るって押されてかつ3つ目のhintがNoneなら時間追加してhint_2とhint_3を返す
		elif next_watch == True and data.hint1_3 == None:
			hint_num = 3
			data.hint1_3 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
			hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n'
		elif next_watch == False:
			if data.hint1_2 == None:
				if data.hint1_1 == None:
					data.hint1_1 = datetime.datetime.now()
					data.save()
				hint_num = 1
				hint = hint
			elif data.hint1_3 == None:
				hint_num = 2
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			else:
				hint_num = 3
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
				hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n\n'

	elif treasureNo == 2:
		hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 1)
		hint = u'ヒント1\n' + hintdatas.hint_sent + u'\n\n'
		if next_watch == True and data.hint2_2 == None:
			hint_num = 2
			data.hint2_2 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
		elif next_watch == True and data.hint2_3 == None:
			hint_num = 3
			data.hint2_3 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
			hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n'
		elif next_watch == False:
			if data.hint2_2 == None:
				if data.hint2_1 == None:
					data.hint2_1 = datetime.datetime.now()
					data.save()
				hint_num = 1
				hint = hint
			elif data.hint2_3 == None:
				hint_num = 2
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			else:
				hint_num = 3
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
				hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n\n'

	elif treasureNo == 3:
		hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 1)
		hint = u'ヒント1\n' + hintdatas.hint_sent + u'\n\n'
		if next_watch == True and data.hint3_2 == None:
			hint_num = 2
			data.hint3_2 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
		elif next_watch == True and data.hint3_3 == None:
			hint_num = 3
			data.hint3_3 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
			hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n'
		elif next_watch == False:
			if data.hint3_2 == None:
				if data.hint3_1 == None:
					data.hint3_1 = datetime.datetime.now()
					data.save()
				hint_num = 1
				hint = hint
			elif data.hint3_3 == None:
				hint_num = 2
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			else:
				hint_num = 3
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
				hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n\n'

	elif treasureNo == 4:
		hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 1)
		hint = u'ヒント1\n' + hintdatas.hint_sent + u'\n\n'
		if next_watch == True and data.hint4_2 == None:
			hint_num = 2
			data.hint4_2 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
		elif next_watch == True and data.hint4_3 == None:
			hint_num = 3
			data.hint4_3 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
			hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n'
		elif next_watch == False:
			if data.hint4_2 == None:
				if data.hint4_1 == None:
					data.hint4_1 = datetime.datetime.now()
					data.save()
				hint_num = 1
				hint = hint
			elif data.hint4_3 == None:
				hint_num = 2
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			else:
				hint_num = 3
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
				hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n\n'

	elif treasureNo == 5:
		hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 1)
		hint = u'ヒント1\n' + hintdatas.hint_sent + u'\n\n'
		if next_watch == True and data.hint5_2 == None:
			hint_num = 2
			data.hint5_2 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
		elif next_watch == True and data.hint5_3 == None:
			hint_num = 3
			data.hint5_3 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
			hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n'
		elif next_watch == False:
			if data.hint5_2 == None:
				if data.hint5_1 == None:
					data.hint5_1 = datetime.datetime.now()
					data.save()
				hint_num = 1
				hint = hint
			elif data.hint5_3 == None:
				hint_num = 2
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			else:
				hint_num = 3
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
				hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n\n'

	elif treasureNo == 6:
		hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 1)
		hint = u'ヒント1\n' + hintdatas.hint_sent + u'\n\n'
		if next_watch == True and data.hint6_2 == None:
			hint_num = 2
			data.hint6_2 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
		elif next_watch == True and data.hint6_3 == None:
			hint_num = 3
			data.hint6_3 = datetime.datetime.now()
			data.save()
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
			hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
			hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n'
		elif next_watch == False:
			if data.hint6_2 == None:
				if data.hint6_1 == None:
					data.hint6_1 = datetime.datetime.now()
					data.save()
				hint_num = 1
				hint = hint
			elif data.hint6_3 == None:
				hint_num = 2
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
			else:
				hint_num = 3
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 2)
				hint = hint + u'ヒント2\n' + hintdatas.hint_sent + u'\n\n'
				hintdatas = Hint.objects.get(treasure_num = treasureNo, hint_num = 3)
				hint = hint + u'ヒント3\n' + hintdatas.hint_sent + u'\n\n'
	else:
		print 'error'

	return hint, hint_num


#終了ページでアンケート用にUserIDとPointを返す
@csrf_exempt
def finish(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		name = datas["name"]   # ダブルクオート内はディクショナリーのキー
		User_Data = User.objects.get(username = name)
		UserId = User_Data.user_id
		Point = User_Data.points
		User_Data.finishtime = datetime.datetime.now()
		User_Data.save()

		return JsonResponse({'''"id":UserId,''' "point":Point})
	else:
		response = HttpResponse()
		response['msg'] = 'NG'

#復元できるデータがあるかチェック
@csrf_exempt
def recover_check(request):
	if request.method == 'POST':
		datas = json.loads(request.body)
		name = datas["name"]

		try:
			testname = User.objects.get(username = name)
			return JsonResponse({"result":"exist"})
		except User.DoesNotExist:
			return JsonResponse({"result":"error"})

#復元するデータを送る
'''
@csrf_exempt
def recover_data(request):
	if request.method == 'POST':

		shop_beacon = []

		datas = json.loads(request.body)
		name = datas["name"]

		UserData = User.objects.get(username = name)
		point = UserData.points
		treasure = UserData.treasures
		check_list = treasure.split(',')
		treasure_beacon = []
		for i in range(0, 10):
			if check_list[i] != '0':
				print i
				temp = Treasure_Beacon.objects.get(treasure = i+1)
				treasure_beacon.append([temp.major, temp.minor])

		#選んだ店の配列を作る
		shop_ = UserData.shopname.split(',')
		make_map(name, shop_)

		for i in shop_:
			#print "logging"
			#print i
			shop_data = Shop_Beacon.objects.get(shopname = i)
			## ここから変更 8/26 夜
			#shopbeacon.append({"major": shop_data.major, "minor": shop_data.minor})
			shop_beacon.append(str(shop_data.major) + "-" + str(shop_data.minor))
			## ここまで

		#KeyTime = datas[key_time]
		KeyTime = UserData.key_time
		## ここから書き換え(8/26)
		print "debug"
		print len(UserData.key.split(','))
		y = [x for x in check_list if x != '0']
		print y
		print len(y)
		if UserData.key == 'key':
			key_num = 0
			key_num = key_num + 1
		else:
			key_num = len(UserData.key.split(',')) - len(y)
			key_num = key_num + 1

		print key_num
		key_num = key_num - 10

		## 書き換えここまで

		#print point
		#print treasure
		print treasure_beacon

		#return JsonResponse({"point":point, "treasure":treasure, "treasure_beacon":treasure_beacon, "shop_beacon":shop_beacon, "KeyTime":KeyTime})
		return JsonResponse({"point":point, "treasure":treasure, "treasure_beacon":treasure_beacon, "shop_beacon":shop_beacon, "KeyTime":KeyTime, "recover_key":key_num})
'''
@csrf_exempt
def recover_data2(request):
	if request.method == 'POST':
		#shop_beacon = []

		datas = json.loads(request.body)
		name = datas["name"]

		UserData = User.objects.get(username = name)
		point = UserData.points
		treasure = UserData.treasures
		check_list = treasure.split(',')
		treasure_beacon = []
		for i in range(0, 6):
			if check_list[i] != '0':
				print i
				temp = Treasure_Beacon.objects.get(treasure = i+1)
				treasure_beacon.append([temp.major, temp.minor])

		'''
		#選んだ店の配列を作る
		#shop_ = UserData.shopname.split(',')
		#make_map(name, shop_)

		for i in shop_:
			#print "logging"
			#print i
			shop_data = Shop_Beacon.objects.get(shopname = i)
			## ここから変更 8/26 夜
			#shopbeacon.append({"major": shop_data.major, "minor": shop_data.minor})
			shop_beacon.append(str(shop_data.major) + "-" + str(shop_data.minor))
			## ここまで
		'''

		#KeyTime = datas[key_time]
		#KeyTime = UserData.key_time

		key_number = UserData.key_num + 1
		print "key_num"
		print key_number
		#sys.stderr.write("message")
		#sys.stderr.write(key_number)

		#print point
		#print treasure
		print treasure_beacon

		#return JsonResponse({"point":point, "treasure":treasure, "treasure_beacon":treasure_beacon, "shop_beacon":shop_beacon, "KeyTime":KeyTime})
		return JsonResponse({"point":point, "treasure":treasure, "treasure_beacon":treasure_beacon, "recover_key":key_number})


#csvとして出力する
@csrf_exempt
def export_csv(request):
	userdata = User.objects.all()

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="userdata.csv"'

	writer = csv.writer(response)

	for i in userdata:
		writer.writerow([
			"%s" % unicodedata.normalize('NFKC', i.username).encode('sjis','ignore'),
			"%d" % i.points,
			"%s" % i.starttime,
			"%s" % i.finishtime,
			"%s" % i.treasure1,
			"%s" % i.treasure2,
			"%s" % i.treasure3,
			"%s" % i.treasure4,
			"%s" % i.treasure5,
			"%s" % i.treasure6,
			"%s" % i.treasure7,
			"%s" % i.treasure8,
			"%s" % i.treasure9,
			"%s" % i.treasure10,
			"%s" % i.key,
			"%s" % unicodedata.normalize('NFKC', i.shopname).encode('sjis','ignore'),
		])

	return response
