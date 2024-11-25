import json
import re
from pprint import pprint
import pymysql

# 1、打开数据库连接
conn = pymysql.connect(host='127.0.0.1',  # host属性
                       port=3306,  # 端口号
                       user='root',  # 用户名
                       password='root',  # 此处填登录数据库的密码
                       db='medical_system'  # 数据库名
                       )

# 使用cursor()方法获取操作游标
cursor = conn.cursor()

count_key = 0
count_list = 0
count_yb = 0
count_not_yb = 0


def isCorrect(dic, keyword):
    """判断关键字是否存在于表中并判断是否为空"""
    global count_key
    global count_list
    try:
        if dic[keyword]:
            # 有键无内容
            return dic[keyword]
        else:
            count_key += 1
            print('list:' + paper['name'])
            return False
    except KeyError:
        # pass
        # 没有这个键
        count_key += 1
        print('name:' + paper['name'])
        return False


def setName(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "name")
    if str(resp):
        result = resp
    return result


def setCure_lasttime(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "cure_lasttime")
    if str(resp):
        result = resp
    return result


def setAcompany(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "acompany")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    print(result)
    return result


def setSymptom(dic):
    result = ''
    resp = isCorrect(dic, "symptom")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    else:
        result = '无详细病症'
    print(result)
    return result


def setCure_department(dic):
    result = ''
    resp = isCorrect(dic, "cure_department")
    # print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    # print(result)
    return result


def setCure_way(dic):
    result = ''
    resp = isCorrect(dic, "cure_way")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    print(result)
    return result


def setDo_eat(dic):
    result = ''
    resp = isCorrect(dic, "do_eat")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    else:
        result = '暂无推荐食物'
    print(result)
    return result


def setNot_eat(dic):
    result = ''
    resp = isCorrect(dic, "not_eat")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    else:
        result = '暂无忌食信息'
    print(result)
    return result


def setYibao_status(dic):
    """获得cleaned_papers的数据"""
    result = ''
    global count_yb
    global count_not_yb
    resp = isCorrect(dic, "yibao_status")
    if str(resp):
        if resp == "是":
            count_yb += 1
        elif resp == "否":
            count_not_yb += 1
        result = resp
    return result


def setEasy_get(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "easy_get")
    if str(resp):
        result = resp

    return result


def setGet_way(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "get_way")
    if str(resp):
        result = resp
    return result


def setCheck(dic):
    result = ''
    resp = isCorrect(dic, "check")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    print(result)
    return result


def setDrug_detail(dic):
    result = ''
    resp = isCorrect(dic, "drug_detail")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    else:
        result = '暂无药品细节'
    print(result)
    return result


def setRecommand_drug(dic):
    result = ''
    resp = isCorrect(dic, "recommand_drug")
    print(resp)
    if resp:
        resp = list(resp)
        for i in range(len(resp)):
            result += resp[i]
            if i != len(resp) - 1:
                result += ','
    else:
        result = '暂无推荐药品'
    print(result)
    return result


def setCuredProb(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "cured_prob")
    if resp:
        resp = str(resp)
        s1 = re.compile(r'(?P<num>\d+.?|\d\.\d+.?)%')
        resp_l = re.findall(s1, resp)
        print(resp_l)
        if resp_l:
            result = float(resp_l[-1])
    return result


def setCuredProbNote(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "cured_prob")
    if str(resp):
        result = resp
    return result


def setGetProb(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "get_prob")
    if resp:
        resp = str(resp)
        s1 = re.compile(r'(?P<num>\d\.\d+.?|\d+.?)%')
        resp_l = re.findall(s1, resp)
        s2 = re.compile(r'(?P<num>\d\.\d+.?|\d+.?)‰')
        resp_s = re.findall(s2, resp)
        print(resp_l)
        # if dic['name'] == '新生儿发热':
        #     print(dic)
        if resp_l:
            result = resp_l[0]
        elif resp_s:
            result = str(float(resp_s[0]) * 0.1)
    return result


def setGetProb1000(floatStr):
    """传float数字进行计算"""
    result = ''
    p_num = 1000
    if floatStr:
        result = round((1 - (1 - float(floatStr) * 0.01) ** p_num) * 100, 2)
    return result


def setGetProbNote(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "get_prob")
    if str(resp):
        result = resp
    return result


def setDesc(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "desc")
    if str(resp):
        resp = resp.replace('\n', '')
        resp = resp.replace('\t', '')
        resp = resp.replace('(', '（')
        resp = resp.replace(')', '）')
        result = resp.replace("'", "‘")
        if "'" in result:
            print('hello!')
        # print(result)
    return result


def setCause(dic):
    """获得cleaned_papers的数据"""
    result = ''
    resp = isCorrect(dic, "desc")
    if str(resp):
        result = resp.replace('\n', '')
        # print(result)
    return result


if __name__ == '__main__':
    # 得到文件与清理好的文件
    papers = []
    cleaned_papers = []
    # 关键词注明：清理后的文件属性
    str_l = ['name', 'desc']
    # 获取文件信息存入papers
    json_file = open('test_text.json', mode='r', encoding='utf-8')
    for line in json_file.readlines():
        j_dic = json.loads(line)
        papers.append(j_dic)
    print(len(papers))
    # 报错信息记录变量
    c_name = []
    for paper in papers:
        result = setCure_department(paper)
        print(result)

        if result not in c_name:
            print(result)
            c_name.append(result)
    pprint(c_name)
    for c in c_name:
        insert_query = "INSERT INTO `doc_class` (`cure_department`) VALUES (%s)"
        print(cursor.execute(insert_query,c))
        cursor.connection.commit()
    # for paper in cleaned_papers:
    #     insert_query = "INSERT INTO `illness` (`clicked_count`,`subscribe_count`,`name`,`get_prob`,`get_prob_1000`," \
    #                    "`get_prob_note`,`desc`," \
    #                    "`acompany`,`cure_lasttime`,`symptom`, `cause`, `cure_department`,`cure_way`,`do_eat`," \
    #                    "`not_eat`,`yibao_status`,`easy_get`,`get_way`,`check`,`drug_detail`,`recommand_drug`," \
    #                    "`cured_prob`,`cured_prob_note` ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
    #                    "%s,%s,%s,%s,%s,%s)"
    #     print(cursor.execute(insert_query, (0,0,paper['name'], paper['get_prob'], paper['get_prob_1000'], paper['get_prob_note'],
    #                                   paper['desc'], paper['acompany'], paper['cure_lasttime'], paper['symptom'],
    #                                   paper['cause'], paper['cure_department'], paper['cure_way'], paper['do_eat'],
    #                                   paper['not_eat'], paper['yibao_status'], paper['easy_get'], paper['get_way'],
    #                                   paper['check'], paper['drug_detail'], paper['recommand_drug'], paper['cured_prob']
    #                                   , paper['cured_prob_note'])))
    #     cursor.connection.commit()
    #     count += 1

# print(count_yb)
# print(count_not_yb)
# print(count)
cursor.close()
conn.close()
