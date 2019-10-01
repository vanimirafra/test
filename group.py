import requests
import json as JSON
import unittest 
BASE_USER_GROUP_INFO='http://192.168.1.24:8001/api/groups'
BASE_USER_GROUP_NAME_INFO='http://192.168.1.24:8001/api/groups/xy'
create_group_data = {
   "group_name": "abc",
   "ass_emps": ["emp1", "emp2"]
}
create_group_data1 = {
   "group_name": "G3",
   "ass_emps": ""
}
create_group_data2 = {
   "group_name": "",
   "ass_emps": [""]
}

delete_group_data = {
    "group_name": "abc"
}

delete_group_data1 = {
    "group_name": "Group5"
}


update_group_name_data = {
    "ass_emps": ["emp4",]
}

delete_group_name_data = {
    "ass_emps": ["emp4",]
}







class SimpleTest(unittest.TestCase):
    def test1(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.get(url)
            self.assertEqual(res.status_code, 200)

        except ConnectionError:
            print('error')

    def test2(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.post(url, data=create_group_data)
            self.assertEqual(res.status_code, 201)
            # print(res)

        except ConnectionError:
            print('error')

    def test3(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.post(url, data=create_group_data1)
            self.assertEqual(res.status_code, 400)
            # print(res)

        except ConnectionError:
            print('error')


    def test4(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.post(url, data=create_group_data2)
            self.assertEqual(res.status_code, 400)
            # print(res)

        except ConnectionError:
            print('error')


    def test5(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.delete(url, data=delete_group_data)
            self.assertEqual(res.status_code, 204)
            # print(res)

        except ConnectionError:
            print('error')

    def test6(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.delete(url, data=delete_group_data)
            self.assertEqual(res.status_code, 404)
            # print(res)

        except ConnectionError:
            print('error')

    def test7(self):
        url = BASE_USER_GROUP_INFO
        try:
            res = requests.delete(url, data=delete_group_data1)
            self.assertEqual(res.status_code, 404)
            # print(res)

        except ConnectionError:
            print('error')


    def test8(self):
        url = BASE_USER_GROUP_NAME_INFO
        try:
            res = requests.get(url)
            self.assertEqual(res.status_code, 200)

        except ConnectionError:
            print('error')





    def test9(self):
        url = BASE_USER_GROUP_NAME_INFO
        try:
            res = requests.put(url, data=update_group_name_data)
            self.assertEqual(res.status_code, 200)
            # print(res)

        except ConnectionError:
            print('error')


    def test10(self):
        url = BASE_USER_GROUP_NAME_INFO
        try:
            res = requests.delete(url, data=delete_group_name_data)
            self.assertEqual(res.status_code, 204)
            # print(res)

        except ConnectionError:
            print('error')


    '''def test11(self):
        url = BASE_USER_GROUP_NAME_INFO
        try:
            res = requests.delete(url, data=delete_group_name_data)
            self.assertEqual(res.status_code, 404)
            # print(res)

        except ConnectionError:
            print('error')

    def test12(self):
        url = BASE_USER_GROUP_NAME_INFO
        try:
            res = requests.put(url, data=update_group_name_data)
            self.assertEqual(res.status_code, 404)
            # print(res)

        except ConnectionError:
            print('error')'''
