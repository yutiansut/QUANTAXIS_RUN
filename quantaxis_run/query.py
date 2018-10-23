import pymongo


def query_result():
    return [item for item in pymongo.MongoClient().quantaxis.JOB_LOG.find(
        {'status': {'$in': ['failed', 'success']}})]


def query_onejob(job_id):
    return [item for item in pymongo.MongoClient().quantaxis.JOB_LOG.find(
        {'job_id': job_id})]
