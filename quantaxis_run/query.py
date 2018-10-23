import pymongo


def query_result():
    return [item for item in pymongo.MongoClient().quantaxis.JOB_LOG.find(
        {'status': {'$in': ['failed', 'success']}})]


def query_onejob(filename):
    return [item for item in pymongo.MongoClient().quantaxis.JOB_LOG.find(
        {'filename': filename})]
