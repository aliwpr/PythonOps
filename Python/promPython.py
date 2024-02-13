# for htto Req
import requests

def queryPrometheus(apiUrl, query, startTime=None, endTime=None):
    """query Prometheus for metrics using the API.

    parameters:
    - query: query expression
    - startTime: start time for the query range
    - apiUrl: "http://192.168.168.103:9090/api/v1/query")
    - endTime: end time for the query range

    returns:
    - query result as a dict"""

    params = {'query': query}

    if startTime:
        params['start'] = startTime
    if endTime:
        params['end'] = endTime

    response = requests.get(apiUrl, params=params)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"failed to query Prometheus {response.status_code}")
        return None
# example
if __name__ == "__main__":
    prometheusApiUrl = "http://192.168.168.103:9090/api/v1/query"
    prometheusQuery = "up"
    result = queryPrometheus(prometheusApiUrl, prometheusQuery)

    if result:
        print("Query Result:")
        print(result)
