import urllib.request
import json

def main():

    try:
        # Get Data for Body Number from ICS Query Service

        qu1 = "http://10.200.2.139/icsQueryService/api/Query/Results/?format=JSON&query_name=BASIC_VEHICLE&SERVICE_KEY=134XR8NZCALF9JJBCXITO0&extra_info=&BODY=12999"

        # print(qu1)

        dataz = None

        tag1 = None

        tag2 = None

        tagw = None

        with urllib.request.urlopen(qu1) as url:
            dataz = json.loads(url.read().decode())

            # print(dataz)

            # print(type(dataz))

            # print(dataz["ICS_DATA"])

            # print(dataz["ICS_DATA"][0]["DATA"])

            print("Body Number :", dataz["ICS_DATA"][0]["DATA"]["BODY_NUM"])

            print("Seq Number :", dataz["ICS_DATA"][0]["DATA"]["SEQ_NUM"])

            print("Vin :", dataz["ICS_DATA"][0]["DATA"]["VIN"])

            print("Katashiki :", dataz["ICS_DATA"][0]["DATA"]["KATASHIKI"])

            print("Success")
    except:
        print("Failed")

    finally:
        exit()

if __name__ == "__main__":
    main()