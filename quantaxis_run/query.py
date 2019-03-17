import pymongo


def query_result():
    return [item for item in pymongo.MongoClient().quantaxis.joblog.find(
        {'status': {'$in': ['failed', 'success']}},{'message':1, '_id':0})]


def query_onejob(job_id):
    return [item for item in pymongo.MongoClient().quantaxis.joblog.find(
        {'job_id': job_id},{'message':1, '_id':0})]


def query_job_by_filename(filename):
    return [item for item in pymongo.MongoClient().quantaxis.joblog.find(
        {'filename': filename},{'message':1, '_id':0})]
